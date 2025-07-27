# Adobe India Hackathon 2025: Connecting the Dots

**Team:** Code Prix
  --- 
**Date:** July 28, 2025

## 1. Project Overview

This repository contains the complete solution for Round 1 of the Adobe India Hackathon 2025: "Connecting the Dots" challenge. The project is divided into two main parts, corresponding to the challenges 1A and 1B.

* **Challenge 1A:** A robust system for extracting a structured outline (title and headings) from any given PDF document.
* **Challenge 1B:** An intelligent, persona-driven system that performs semantic search across a collection of documents to find and rank the most relevant sections based on a user's specific job-to-be-done.

## 2. Key Features

### Challenge 1A: Document Structure Analysis

* **Dynamic Heading Detection:** The solution does not rely on hardcoded font sizes. It dynamically analyzes the font properties of each document to identify the most likely body text size and then classifies headings based on their relative size.
* **Positional Awareness:** The title is identified not just by its size, but also by its vertical position, prioritizing text that appears at the top of the first page for higher relevance.
* **Robust Line Assembly:** Intelligently groups text "spans" with different formatting into complete, coherent lines of text, preserving proper spacing.
* **Automated JSON Output:** Automatically generates a correctly formatted JSON file for each processed PDF.

### The Journey Ahead

**Round 1:**
Kick things off by building the brains — extract structured outlines from raw PDFs with blazing speed and pinpoint accuracy. Then, power it up with on-device intelligence that understands sections and links related ideas together.

**Round 2:**
It's showtime! Build a beautiful, intuitive reading webapp using Adobe's PDF Embed API. You will be using your Round 1 work to design a futuristic webapp.

### Why This Matters

In a world flooded with documents, what wins is not more content — it's context. You're not just building tools — you're building the future of how we read, learn, and connect. No matter your background — ML hacker, UI builder, or insight whisperer — this is your stage.

Are you in?

It's time to read between the lines. Connect the dots. And build a PDF experience that feels like magic. Let's go.

---

## Challenge Solutions

### [Challenge 1a: PDF Processing Solution](./Challenge_1a/README.md)
Basic PDF processing with Docker containerization and structured data extraction.

### [Challenge 1b: Multi-Collection PDF Analysis](./Challenge_1b/README.md)
Advanced persona-based content analysis across multiple document collections.

---

**Note**: Each challenge directory contains detailed documentation and implementation details. Please refer to the individual README files for comprehensive information about each solution.