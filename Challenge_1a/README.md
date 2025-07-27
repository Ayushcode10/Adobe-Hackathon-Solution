# Challenge 1A – Structured PDF Outline Extraction

This solution extracts structured outlines (Title, H1, H2, H3 headings) from PDF documents.

## How It Works
- Uses PyMuPDF to analyze font size and vertical position of text
- Dynamically classifies heading levels based on relative size
- Detects title from topmost large text
- Outputs JSON with `title` and `outline` array

## Run Instructions (Docker)
Place PDF files in `input/`, create `output/` folder.

```bash
docker build -t Adobe-India-Hackathon .
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output adobe-1a
```