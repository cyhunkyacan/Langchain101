# Langchain101

This repo is a workspace where I document my LangChain learning journey step by step.

My goal here is not to build one big project all at once. I want to learn the core concepts through small scripts, in order, with each file adding something on top of the previous one.

The README will follow the same logic: as I add new topics and keep committing to the repo, this document will be updated to reflect the current stage of the journey.

## How This Repo Progresses

The numbers at the beginning of the file names show the learning order:

- `01_...` basic LangChain and model invocation
- `02_...` adding an output parser on top of the previous step
- `03_...` preparing the transition into prompt templates

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

This file was created as the transition point into prompt templates.

At the moment:

- `ChatPromptTemplate` has been imported
- the current flow still works with the same logic as `02_output_parser.py`

That also matches the nature of this repo as a learning log: sometimes I prepare the ground for the next topic before fully applying it.

## Technologies

- Python
- LangChain
- LangChain OpenAI
- OpenAI API
- python-dotenv

## Purpose Of This Repo

This repo exists to:

- document my progress while learning LangChain
- break core concepts into small and readable examples
- build a visible record of how my understanding evolves over time

## Notes

- `.env` is intentionally kept outside the repo
- the files are learning-focused, not production-focused
- the code may be refactored over time; the main value here is the progress record
