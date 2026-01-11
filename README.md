# AutoStream-Agent

## Overview
This project implements a conversational AI agent for AutoStream, a fictional SaaS product that provides automated video editing tools for content creators.

The agent is designed to:
- Answer product and pricing questions
- Identify high-intent users
- Collect user details
- Trigger a lead capture tool

## Tech Stack
- Python 3
- Rule-based intent detection
- Local knowledge base (RAG-style retrieval)
- Command-line conversational interface

## How to Run Locally
1. Clone the repository
2. Install dependencies:
   pip install -r requirements.txt
3. Run the agent:
   python app.py

## Architecture Explanation
The agent follows a simple agentic workflow. User messages are first analyzed using an intent detection module to classify the intent as greeting, product inquiry, or high-intent lead.  
Product-related queries are answered using a local knowledge base file containing pricing and policy information, simulating a Retrieval-Augmented Generation (RAG) approach.  
When high intent is detected, the agent collects user details (name, email, platform) and triggers a mock lead capture tool.  
State is maintained through the conversational flow by sequential input handling.

## WhatsApp Deployment (Conceptual)
The agent can be integrated with WhatsApp using the WhatsApp Business API. Incoming user messages can be received through webhooks, processed by the agent backend, and responses can be sent back to users via WhatsApp APIs.

## Demo
A short screen-recorded demo video demonstrates pricing queries, high-intent detection, user detail collection, and successful lead capture.
