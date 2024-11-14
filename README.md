# Doc Multi-Agents Project

This project implements a Retrieval-Augmented Generation (RAG) agent using LlamaIndex and Meta's Llama 3.2 models. 

## Workflow Diagram

![Workflow diagram](Multi-Agents_Workflow.png)

## Goals:
- Train and index key aspects of your documentation as specialized bot agents (e.g.: one for conceptual content, another for tutorials and how-tos, and others for terms and glossaries, etc).
- When a user asks a question, the system analyzes the prompt to identify the type of query.
- The right agent (or multiple agents, if needed) is selected to answer specific parts of the prompt.
- The responses from each agent are sent to the LLM, which creates a cohesive, final response.

## Setup
Windows OS:
1. Install Python 3.12.
2. Run `pip install -r requirements.txt` to install dependencies.
3. Create a new virtual environemnt: `python -m venv multiagentsenv`.
4. Activate the virtual environment: `multiagentsenv/Scripts/activate`.
5. Log into HuggingFace `huggingface-cli login --token $env:HUGGINGFACE_TOKEN`
6. Run the Flask agent: `python flask_app.py`...follow instructions in terminal to find the web endpoint for the Agent's Web UI. Start chatting with the Doc Bot Agent from there.

## Features
- Web content ingestion using BeautifulSoup.
- Multiple RAG agents implementation using LlamaIndex.
- LLM using Meta Llama3.2 hosted through HuggingFace Hub
- Web UI (Chat Bot) powered by Flask

## Remarks
- To help speed things up during execution, run `process_data.py` by itself first. This file takes a list of content URLs and scrape the content. The raw text will be placed under the folder `data/raw`
- Right now, `load_data.py` will try to load the vectorized indexes from the `data/processed` folder if they exists. Otherwise, it will read in the raw content files and index the content. This process can take awhile if you have a large set of files to process. So, you may also want to separate out the index processing into it's own file (similar to `process_data.py`) so that you can run that part of the process by itself. Once the raw files are indexed, reading them into the agent is relatively fast.
- For your convenient, I uploaded the raw and processed files to this project to help save you time. But, if you make any modifications to the raw content, you will need to re-run the indexing.
- LlamaIndex's ReAct Agent does what i wanted so the individual `agents/` are no longer needed. In a ReAct Agent, they are turned into tools. But, I am keeping the `agents/` for referencing. They are not used in the current setup.