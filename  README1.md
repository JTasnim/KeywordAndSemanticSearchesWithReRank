# **ReRank: Enhancing Semantic Search with Keyword and Dense Retrieval**

## **Overview**

ReRank is a project designed to improve semantic search by combining keyword-based and dense retrieval methods with re-ranking techniques. Using Cohere’s ReRank API and Weaviate for vector-based search, this implementation demonstrates how to reorder search results based on their relevance to a given query.

---

## **Features**

- **Keyword Search:** Traditional keyword matching with enhanced precision using ReRank.
- **Dense Retrieval:** Semantic-based search using dense embeddings for richer context understanding.
- **ReRank Integration:** Assign relevance scores to search results and reorder them to prioritize relevant documents.
- **Testing and Evaluation:** Analyze and compare search precision, recall, and ranking metrics.

---

## **How It Works**

### **1. Setup**

- Load environment variables for Cohere and Weaviate API keys.
- Import necessary libraries.

### **2. Keyword Search**

- Perform a keyword-based search using Weaviate.
- Retrieve multiple results and apply Cohere’s ReRank API to reorder based on relevance.

### **3. Dense Retrieval**

- Use dense embeddings to perform a semantic search.
- Enhance the retrieval results using ReRank to prioritize accurate responses.

### **4. Evaluation**

- Compare performance metrics like precision, recall, and MRR (Mean Reciprocal Rank) for different retrieval methods.

---

## **Installation**

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/your-username/ReRank.git
cd ReRank
```

### **Step 2: Add API Keys**

    Create a .env file in the root directory, Add the following:
    - COHERE_API_KEY=<your_cohere_api_key>
    - WEAVIATE_API_KEY=<your_weaviate_api_key>
    - WEAVIATE_API_URL=<your_weaviate_api_url>

---

## Screenshot of execution results

![My Project Screenshot](assets/Screenshot1.png)

---

## To learn more

[Google Slide](/assets/KeywordAndSemanticSearchesWithReRank.pptx)
