# Rerank Your Data Across Multiple Sources for QnA

This sample demonstrates Q&A application, enabled by reranking data from multiple sources and powered by GPT. It utilizes indexed files and the rerank tool from Azure Machine Learning to provide grounded answers. You can ask a wide range of questions and receive responses based on a wide set of stored data. The process involves taking the query, extracting pre-existing documents across multiple sources, reranking said documents for the most relevant context, and then using GPT to chat with you, given those documents.

## What you will learn

In this flow, you will learn

* how to compose a Q&A system flow.
* how to use index lookup tool to retrieve data via Azure Connections and Vector Indices.
* how to use the rerank tool to find the most relevant context given your query.

## Prerequisites

- Connection: Azure OpenAI or OpenAI connection, with the availability of chat/completion and embedding models/deployments.

## Tools used in this flow

* LLM tool
* Vector Index Lookup tool
* Rerank tool
* Python tool
