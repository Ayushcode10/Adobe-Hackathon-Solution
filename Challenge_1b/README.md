# Adobe India Hackathon 2025: Connecting the Dots

**Author:** [CODE-PRIX]
**Date:** July 21, 2025

## 1. Project Overview

This repository contains the complete solution for Round 1 of the Adobe India Hackathon 2025: "Connecting the Dots" challenge. The project is divided into two main parts, corresponding to the challenges 1A and 1B.

* **Challenge 1A:** A robust system for extracting a structured outline (title and headings) from any given PDF document.
* **Challenge 1B:** An intelligent, persona-driven system that performs semantic search across a collection of documents to find and rank the most relevant sections based on a user's specific job-to-be-done.

## 2. Key Features

### Challenge 1A: Document Structure Analysis

* **Dynamic Heading Detection:** The solution does not rely on hardcoded font sizes. It dynamically analyzes the font properties of each document to identify the most likely body text size and then classifies headings based on their relative size and position on the page.
* **Positional Awareness:** The title is identified not just by its size, but also by its vertical position, prioritizing text that appears at the top of the first page.
* **Robust Line Assembly:** Intelligently groups text "spans" with different formatting into complete, coherent lines of text, preserving proper spacing.
* **Automated JSON Output:** Automatically generates a correctly formatted JSON file for each processed PDF.

### Challenge 1B: Persona-Driven Document Intelligence

* **Semantic Search Engine:** Implements a full semantic search pipeline instead of simple keyword matching. This allows the system to understand the *meaning* and *intent* behind a user's request.
* **Text Embeddings:** Uses the powerful `all-MiniLM-L6-v2` sentence-transformer model to convert both the user's query and the document text into meaningful numerical vectors (embeddings).
* **Content Chunking:** Automatically reads and parses multiple PDFs, breaking them down into logical, paragraph-sized text chunks for analysis.
* **Relevance Ranking:** Uses Cosine Similarity to mathematically compare the user's query vector to all document chunk vectors, providing a precise relevance score for ranking.
* **Improved Query Generation:** Enhances the user's "persona" and "task" into a more descriptive, natural language query to achieve more accurate and relevant results.

## 3. Tech Stack

* **Language:** Python 3.11+
* **Core Libraries:**
    * `PyMuPDF (fitz)`: For fast and detailed PDF parsing.
    * `sentence-transformers`: For generating text embeddings.
    * `PyTorch`: As the backend for sentence-transformers and tensor operations.
* **Containerization:** Docker

## 4. Setup and How to Run

### A. Local Setup (for testing)

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/](https://github.com/)[YourUsername]/[Your-Repo-Name].git
    cd [Your-Repo-Name]
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### B. Running the Scripts Locally

* **To run the Challenge 1A solution:**
    ```bash
    # Navigate to the Challenge_1a directory
    cd Challenge_1a
    # Run the script
    python process_pdfs.py
    ```

* **To run the Challenge 1B solution:**
    ```bash
    # Navigate to the Challenge_1b directory
    cd Challenge_1b
    # Run the script, providing the collection name as an argument
    python solution_1b.py "Collection 1"
    ```

### C. Running with Docker (Official Submission Method)

The project is configured to be built and run via Docker as per the hackathon requirements.

1.  **Build the Docker image:**
    From the root directory of the project, run:
    ```bash
    docker build -t adobe-hackathon-solution .
    ```

2.  **Run the container:**
    The judges will use a `docker run` command similar to the one specified in the problem statement to mount the input/output directories and execute the scripts. For example, to run the Challenge 1A solution:
    ```bash
    docker run --rm -v $(pwd)/Challenge_1a/sample_dataset/pdfs:/app/input -v $(pwd)/Challenge_1a/sample_dataset/outputs:/app/output adobe-hackathon-solution python Challenge_1a/process_pdfs.py
    ```

## 5. Approach Explanation for Challenge 1B

A detailed, 300-500 word explanation of the methodology used for the persona-driven intelligence task can be found in the `approach_explanation.md` file.
