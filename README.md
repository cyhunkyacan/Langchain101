# Langchain101

This repo is a workspace where I document my LangChain learning journey step by step.

My goal here is not to build one big project all at once. I want to learn the core concepts through small scripts, in order, with each file adding something on top of the previous one.

The README will follow the same logic: as I add new topics and keep committing to the repo, this document will be updated to reflect the current stage of the journey.

## How This Repo Progresses

The numbers at the beginning of the file names show the learning order:

- `01_...` basic LangChain and model invocation
- `02_...` adding an output parser on top of the previous step
- `03_...` moving from static messages to prompt templates
- `04_...` serving the chain through LangServe and FastAPI
- `05_...` adding conversation memory with message history
- `06_...` storing documents as embeddings and retrieving context with a vector store

Each new file should be read as a continuation of the previous one.

## Progress So Far

### `01_get_first_message.py`

The first basic experiment.

In this file:

- the API key is loaded from `.env`
- a `ChatOpenAI` model is created
- a simple message flow is built with `SystemMessage` and `HumanMessage`
- the model is called with `invoke()` and the result is printed

What I learned here:

- how to connect a model with LangChain
- how to pass message-based input
- the difference between `SystemMessage` and `HumanMessage`

### `02_output_parser.py`

In this step, `StrOutputParser` is added on top of the previous example.

In this file:

- the model output is converted into a plain string through a parser
- a simple chain is built with `model | parser`

What I learned here:

- the logic behind LangChain Expression Language (LCEL)
- how to connect components with the pipe (`|`) operator
- how to get cleaner model output

### `03_prompt_templates.py`

This step moves the flow away from hardcoded messages and into reusable prompt templates.

In this file:

- a `system_prompt` with variables is defined
- `ChatPromptTemplate.from_messages(...)` is used to build the prompt
- the chain now accepts structured input like `language` and `text`
- the parser is still composed with the model through LCEL

What I learned here:

- how to replace fixed chat messages with dynamic prompt variables
- how to pass dictionary input into a chain
- how prompt templates fit naturally into the LCEL pipeline

### `04_langserve.py`

This step exposes the same translation chain as an HTTP service.

In this file:

- the existing prompt-template-based chain is reused
- a FastAPI app is created
- `langserve.add_routes(...)` mounts the chain under `/chain`
- the app can be started locally with Uvicorn

What I learned here:

- how to turn a LangChain chain into an API endpoint
- how LangServe integrates with FastAPI
- how to move from local scripts toward a service-oriented workflow

### `05_messaging_history.py`

This step adds conversation memory so the chain can keep track of previous messages inside the same session.

In this file:

- `InMemoryChatMessageHistory` is used as a simple in-memory store
- `get_session_history(...)` creates or returns chat history per session
- `MessagesPlaceholder` injects prior conversation into the prompt
- `RunnableWithMessageHistory` wraps the chain and keeps the interaction state
- the script runs in a loop and streams responses for an ongoing chat session

What I learned here:

- how to attach memory to a runnable chain
- how session-based chat history works in LangChain
- how to include prior messages in the prompt flow with `MessagesPlaceholder`

### `06_vector_store.py`

This step moves from chat memory into retrieval.

In this file:

- a few sample `Document` objects are created as a tiny knowledge base
- `OpenAIEmbeddings` converts those documents into vector representations
- `Chroma.from_documents(...)` stores the embedded documents in a vector store
- `similarity_search` is wrapped as a retriever and plugged into the chain
- the prompt tells the model to answer using the retrieved context only

What I learned here:

- the difference between raw prompt input and retrieved context
- how embeddings make semantic search possible
- how a retriever can be composed into an LCEL chain
- the first building block behind retrieval-augmented generation workflows

## Technologies

- Python
- LangChain
- LangChain OpenAI
- LangChain Chroma
- OpenAI API
- python-dotenv
- FastAPI
- LangServe
- Chroma vector store

## Purpose Of This Repo

This repo exists to:

- document my progress while learning LangChain
- break core concepts into small and readable examples
- build a visible record of how my understanding evolves over time
- keep my personal study notes in code form instead of treating this as a polished product

## Notes

- `.env` is intentionally kept outside the repo
- the files are learning-focused, not production-focused
- this repo is basically my personal LangChain study notebook
- the code may be refactored over time; the main value here is the progress record
