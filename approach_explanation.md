# Approach Explanation for Challenge 1B: Persona-Driven Document Intelligence  
**Team:** Code Prix  

---

## 1. Objective

The goal of Challenge 1B was to build an intelligent system that identifies and ranks the most relevant sections across a collection of PDFs based on a persona and a task. Instead of relying on simple keyword matching, I implemented a semantic understanding pipeline that mimics how a human researcher would find useful insights.

---

## 2. Overview of Solution

The solution is a four-stage pipeline:

### Stage 1: Query Understanding
The system enhances the given persona and job-to-be-done into a natural language query. For example:  
> _Persona_: "Travel Planner"  
> _Task_: "Plan a trip of 4 days for 10 college friends"  
is converted into:  
> _“As a Travel Planner, I need to plan a 4-day trip for a group of 10 college friends. Find the most relevant information about activities, locations, food, and logistics.”_  

This step provides valuable context to the semantic model.

---

### Stage 2: PDF Parsing and Chunking
All PDFs are parsed using PyMuPDF. Text is extracted block-wise and filtered into coherent chunks (~1 paragraph), ensuring contextual integrity. Each chunk is tagged with its page number and source document.

---

### Stage 3: Embedding Generation
Using the lightweight `all-MiniLM-L6-v2` model from SentenceTransformers (384D vector space), both the enhanced query and each chunk are encoded into semantic embeddings. This model balances quality, size (<100MB), and speed, complying with challenge constraints.

---

### Stage 4: Semantic Similarity & Ranking
Using cosine similarity, the query vector is compared with all chunk vectors. The top 10 highest scoring chunks are selected as the most relevant. The output is then formatted into the required JSON structure, including document name, page number, and importance rank.

---

## 3. Outcome

This modular, offline-friendly pipeline can generalize to any domain or persona. It delivers accurate, ranked insights by truly understanding what the user needs — not just what words appear in the documents.

