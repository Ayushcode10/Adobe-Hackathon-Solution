# Approach Explanation for Challenge 1B: Persona-Driven Document Intelligence
Team: [Code Prix]

### 1. Introduction and Core Philosophy
The central challenge of Round 1B was to move beyond simple keyword matching and build a system that could understand the intent behind a user's request. My approach was to develop a complete, end-to-end semantic search pipeline. The core philosophy is that the relevance of a document section is determined by its conceptual similarity to a user's goal, not just the words it contains. This allows the system to function like an intelligent research assistant, finding meaningful connections across a large corpus of documents.

### 2. Methodology: A Semantic Search Pipeline
The solution is implemented as a four-stage pipeline:

#### Stage 1: Query Understanding and Enhancement
The system begins by processing the input request.json. Instead of using the "persona" and "job-to-be-done" fields as separate, raw inputs, they are combined and enhanced into a more descriptive, natural language query. For example, a "Travel Planner" persona and a "Plan a trip" task are transformed into a richer query like: "As a Travel Planner, I need to Plan a trip of 4 days for a group of 10 college friends. Find the most relevant information about activities, locations, food, and logistics for this trip." This "prompt engineering" step provides crucial context to the language model, leading to significantly more relevant search results.

#### Stage 2: Document Ingestion and Chunking
Next, the system processes the entire collection of PDF documents. Each PDF is read using the PyMuPDF library, and its text content is segmented into smaller, coherent chunks. These chunks are designed to approximate paragraphs, ensuring that each unit of text contains a complete idea. This chunking strategy is vital for creating a granular, searchable index of the document library.

#### Stage 3: Text-to-Vector Transformation (Embeddings)
This is the core of the AI-powered solution. The lightweight yet powerful all-MiniLM-L6-v2 sentence-transformer model is used to convert both the enhanced user query and every document chunk into 384-dimensional numerical vectors, or "embeddings." These embeddings are a mathematical representation of the text's semantic meaning. This model was chosen for its excellent balance of performance and size, easily fitting within the challenge constraints.

#### Stage 4: Similarity Ranking and Output Generation
With the query and all document chunks represented as vectors, the final stage is to find the best matches. Cosine Similarity is used to calculate the "distance" between the query vector and every chunk vector in the library. A higher cosine similarity score indicates a closer conceptual match. The system then ranks all chunks based on their scores and selects the top 10 most relevant results. This ranked list is then formatted into the required JSON structure, providing the user with a prioritized list of actionable insights to accomplish their task. This fully automated pipeline provides a robust, flexible, and intelligent solution to the document analysis problem.