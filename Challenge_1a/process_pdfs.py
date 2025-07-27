import os
import json
from pathlib import Path
from collections import Counter
import fitz # PyMuPDF

def analyze_pdf_structure(pdf_path):
    """
    Opens a PDF and captures text, size, page, and vertical position.
    """
    try:
        doc = fitz.open(pdf_path)
        text_data = []
        font_sizes = []
        for page_num, page in enumerate(doc):
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                if "lines" in block:
                    for line in block["lines"]:
                        spans = [s for s in line["spans"] if s['text'].strip()]
                        if not spans:
                            continue
                        
                        full_line_text = " ".join(s["text"].strip() for s in spans)
                        line_size = round(spans[0]["size"])
                        # Get the vertical position of the first span
                        y_position = spans[0]['bbox'][1] 

                        font_sizes.append(line_size)
                        text_data.append({
                            "text": full_line_text,
                            "size": line_size,
                            "page": page_num + 1,
                            "y_pos": y_position # Add y-position to our data
                        })
        doc.close()
        size_counts = Counter(font_sizes)
        unique_sizes = sorted(size_counts.keys(), reverse=True)
        return text_data, unique_sizes, size_counts
    except Exception as e:
        print(f"An error occurred during analysis: {e}")
        return None, None, None

def classify_headings(text_data, sorted_sizes, size_counts):
    """
    Classifies headings only if they are significantly larger than the body text.
    """
    if not size_counts:
        return []
        
    body_size = size_counts.most_common(1)[0][0]
    heading_sizes = [s for s in sorted_sizes if s > body_size * 1.2]

    size_to_level = {}
    heading_levels = ["Title", "H1", "H2", "H3"]
    for i, size in enumerate(heading_sizes):
        if i < len(heading_levels):
            size_to_level[size] = heading_levels[i]
        else:
            break

    outline = []
    for item in text_data:
        size = item['size']
        if size in size_to_level:
            level_name = size_to_level[size]
            if level_name != "Title":
                outline.append({
                    "level": level_name,
                    "text": item["text"],
                    "page": item["page"]
                })
    return outline

def get_title(text_data, sorted_sizes):
    """
    Finds the title by looking for the largest text that is
    closest to the top of the page.
    """
    if not sorted_sizes:
        return ""
    
    title_size = sorted_sizes[0]
    # Get all lines that have the largest font size
    potential_titles = [item for item in text_data if item['size'] == title_size]
    
    if not potential_titles:
        return ""
        
    # Of those potential titles, find the one with the smallest y_pos (highest on the page)
    title_item = min(potential_titles, key=lambda x: x['y_pos'])
    return title_item['text']

def process_all_pdfs():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    pdf_files = list(input_dir.glob("*.pdf"))

    for pdf_file in pdf_files:
        print(f"\n--- Processing {pdf_file.name} ---")
        text_data, sorted_sizes, size_counts = analyze_pdf_structure(pdf_file)

        if text_data:
            title = get_title(text_data, sorted_sizes)
            outline = classify_headings(text_data, sorted_sizes, size_counts)
            
            if len(sorted_sizes) > 5 and len(text_data) < 30:
                title = get_title(text_data, sorted_sizes)
                outline = []

            final_json_data = {"title": title, "outline": outline}
            
            output_filename = output_dir / f"{pdf_file.stem}.json"
            with open(output_filename, 'w') as f:
                json.dump(final_json_data, f, indent=4)
            print(f"Successfully created JSON output: {output_filename.name}")

if __name__ == "__main__":
    print("Starting PDF processing...")
    process_all_pdfs()
    print("\nCompleted PDF processing.")