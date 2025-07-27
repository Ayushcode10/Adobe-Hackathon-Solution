# Challenge 1B – Persona-Driven Document Intelligence

This solution performs intelligent, persona-aware content extraction from a collection of PDFs using semantic search. It ranks the most relevant document sections based on a user’s role and goal, providing actionable insights in a structured JSON output.

---

## 🔍 Problem Statement

Given:
- A collection of PDFs
- A `challenge1b_input.json` file containing:
  - A **persona** (e.g., "Travel Planner")
  - A **job-to-be-done** (e.g., "Plan a trip for 10 people")

Your task is to extract the **10 most relevant chunks** from across the PDF collection that help the persona achieve their goal.

---

## 🧠 Solution Overview

- 🔹 **Semantic Search**: Converts user intent and document text into embeddings.
- 🔹 **Enhanced Query Generation**: Combines persona + task into a meaningful query.
- 🔹 **Chunking**: Splits PDF text into paragraph-level chunks.
- 🔹 **Relevance Ranking**: Uses cosine similarity to rank and extract the top 10 results.

---
