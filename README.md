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

## Setup

Create and activate a virtual environment, then install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Add your OpenAI key to `.env`:

```env
OPENAI_API_KEY=your_key_here
```

Run the examples:

```bash
python 01_get_first_message.py
python 02_output_parser.py
python 03_prompt_templates.py
python 04_langserve.py
```

When `04_langserve.py` is running, the LangServe route is available at:

```text
http://localhost:8000/chain
```

## Technologies

- Python
- LangChain
- LangChain OpenAI
- OpenAI API
- python-dotenv
- FastAPI
- LangServe

## Purpose Of This Repo

This repo exists to:

- document my progress while learning LangChain
- break core concepts into small and readable examples
- build a visible record of how my understanding evolves over time

## Notes

- `.env` is intentionally kept outside the repo
- the files are learning-focused, not production-focused
- the code may be refactored over time; the main value here is the progress record
