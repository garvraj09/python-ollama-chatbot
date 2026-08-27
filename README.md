# python-ollama-chatbot

A simple command-line AI chatbot built with **Python** and **Ollama**, using the **Llama 3.2** large language model.

The chatbot allows users to have a continuous conversation with the local Llama 3.2 model. It maintains the conversation history during the current session so that the model can use previous messages to understand the context of the conversation.

## Features

- Interactive command-line chatbot
- Powered by the Llama 3.2 LLM
- Uses Ollama to run the model locally
- Maintains conversation history during the session
- Runs locally without requiring a cloud-based LLM API
- Simple terminal-based interface
- Type `exit` to end the conversation

## Technologies Used

- **Python**
- **Ollama**
- **Llama 3.2**

## How It Works

The application follows a simple conversation flow:

```text
User
  ↓
Enter Message
  ↓
Python Application
  ↓
Ollama
  ↓
Llama 3.2
  ↓
Generate Response
  ↓
Display Response
  ↓
Store Conversation History
  ↓
Next User Message
```

The chatbot stores both user messages and assistant responses in a `messages` list. This conversation history is sent to Ollama with each new request, allowing the model to maintain context throughout the session.

## Prerequisites

Before running the project, make sure you have:

- Python 3 installed
- Ollama installed and running
- Llama 3.2 model downloaded

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/garvraj09/python-ollama-chatbot.git
```

### 2. Navigate to the project directory

```bash
cd python-ollama-chatbot
```

### 3. Create a virtual environment

It is recommended to use a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

## Ollama Setup

Install Ollama on your system and download the Llama 3.2 model:

```bash
ollama pull llama3.2
```

You can verify that the model is available by running:

```bash
ollama list
```

Make sure Ollama is running before starting the chatbot.

## Running the Chatbot

Run the Python file:

```bash
python chat.py
```

Replace `chat.py` with the actual name of your Python file.

You should see:

```text
Chat with Llama3.2 (type 'exit' to quit)
----------------------------------------
You:
```

You can then start chatting with the model.

To exit the chatbot, type:

```text
exit
```

## Example

```text
Chat with Llama3.2 (type 'exit' to quit)
----------------------------------------

You: What is artificial intelligence?

Llama: Artificial intelligence (AI) refers to...

You: What are its applications?

Llama: AI is used in many areas such as...

You: exit

Goodbye!
```

## Project Structure

```text
python-ollama-chatbot/
│
├── your_file_name.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Dependencies

The project uses the official Python Ollama package.

`requirements.txt`:

```text
ollama
```

## Privacy

Since the Llama 3.2 model is run locally through Ollama, the chatbot does not require a cloud-based LLM API key.

The conversation is processed through the local Ollama setup on your computer.

## Learning Objectives

This project was created to understand the fundamentals of:

- Large Language Models (LLMs)
- Local LLM execution
- Ollama
- Python integration with LLMs
- Sending prompts to an LLM
- Maintaining conversation history
- Building a basic AI application
