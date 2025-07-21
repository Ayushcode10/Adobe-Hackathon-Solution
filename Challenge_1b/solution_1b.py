import json
from pathlib import Path
from sentence_transformers import SentenceTransformer, util
import fitz # PyMuPDF
import torch
import sys

def read_and_chunk_pdf(pdf_path):
    """Reads a PDF and splits it into text chunks."""
    try:
        doc = fitz.open(pdf_path)
        chunks = []
        for page_num, page in enumerate(doc):
            blocks = page.get_text("blocks")
            for block in blocks:
                text = block[4]
                if len(text.split()) > 15:
                    chunks.append({"page": page_num + 1, "text": text.replace('\n', ' ').strip()})
        doc.close()
        return chunks
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return []

def main():
    if len(sys.argv) < 2:
        print("Usage: python solution_1b.py \"<collection_directory_name>\"")
        print("Example: python solution_1b.py \"Collection 1\"")
        return

    collection_name = sys.argv[1]
    collection_dir = Path(collection_name)

    if not collection_dir.is_dir():
        print(f"Error: Directory '{collection_dir}' not found.")
        return

    request_file = collection_dir / "challenge1b_input.json"
    pdfs_dir = collection_dir / "PDFs"
    output_file = Path(f"{collection_dir.name}_output.json")

    print("Loading embedding model...")
    model = SentenceTransformer('all-MiniLM-L6-v2')
    print("Model loaded.")
    
    with open(request_file, 'r') as f:
        request_data = json.load(f)
    
    # --- IMPROVED QUERY GENERATION ---
    persona = request_data['persona']['role']
    task = request_data['job_to_be_done']['task']
    query = f"As a {persona}, I need to {task}. Find the most relevant information about activities, locations, food, and logistics for this trip."
    print(f"\nImproved User Query: {query}")
    # --- END IMPROVEMENT ---

    all_chunks = []
    pdf_files = list(pdfs_dir.glob("*.pdf"))
    print(f"\nProcessing {len(pdf_files)} PDF(s) from {collection_dir.name}...")
    for pdf_file in pdf_files:
        chunks = read_and_chunk_pdf(pdf_file)
        for chunk in chunks:
            chunk['source_file'] = pdf_file.name
        all_chunks.extend(chunks)
    
    if not all_chunks:
        print("No text chunks extracted. Exiting.")
        return

    print(f"Creating embeddings for {len(all_chunks)} text chunks...")
    chunk_texts = [chunk['text'] for chunk in all_chunks]
    chunk_embeddings = model.encode(chunk_texts, convert_to_tensor=True, show_progress_bar=True)

    query_embedding = model.encode(query, convert_to_tensor=True)
    cosine_scores = util.cos_sim(query_embedding, chunk_embeddings)[0]
    top_results = torch.topk(cosine_scores, k=min(10, len(all_chunks)))

    extracted_sections = []
    for i, (score, idx) in enumerate(zip(top_results[0], top_results[1])):
        chunk = all_chunks[idx]
        extracted_sections.append({
            "document": chunk['source_file'],
            "page_number": chunk['page'],
            "text": chunk['text'],
            "importance_rank": i + 1
        })
    
    final_output = {
        "metadata": request_data,
        "extracted_sections": extracted_sections
    }

    with open(output_file, 'w') as f:
        json.dump(final_output, f, indent=4)
    print(f"\nSuccessfully created the final output file: {output_file}")

if __name__ == "__main__":
    main()