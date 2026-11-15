# WhatToCook-AI

WhatToCook-AI is a Python command-line prototype that accepts a food image, asks a configured chat model to identify visible ingredients, and uses Tavily web search to find recipe sources. The application is built with LangChain and supports OpenAI-compatible model endpoints through `langchain-openai`.

## Features

- Select an image with a desktop file picker, or enter its path when a GUI is unavailable.
- Decode and convert the selected image to JPEG before constructing a multimodal message.
- Ask the model to identify ingredients and recommend a recipe.
- Expose Tavily search as an agent tool for recipe discovery.

The project is an early prototype. It has no database, HTTP server/API, user accounts, or automated test suite. See the consolidated [Project Guide](docs/PROJECT_GUIDE.md) for architecture, setup, module details, limitations, and troubleshooting.

## Prerequisites

- Python 3.12 or newer (`pyproject.toml` declares `requires-python = ">=3.12"`).
- `uv` for the project’s declared build and dependency workflow, or another PEP 517-compatible installer.
- Credentials for a compatible chat model endpoint and Tavily.
- A desktop environment for the image picker; without one, the app prompts for an image path.

## Setup

```bash
git clone <repository-url>
cd WhatToCook-AI
uv sync
cp .env.example .env
```

Edit `.env` with the values described in the [Project Guide](docs/PROJECT_GUIDE.md#configuration). Never commit `.env` or real credentials.

## Quick start

Run the current application entry script from the repository root:

```bash
uv run python main.py
```

Select an image in the dialog. If Tk cannot open a display, type the image path when prompted. The standalone vision diagnostic accepts an optional path:

```bash
uv run python test_vision.py /path/to/food-image.jpg
```

`test_vision.py` makes a live model API call; it is a diagnostic script, not an automated test suite. The declared `whattocook-ai` console script currently points to the scaffold module rather than `main.py`; see [Troubleshooting](docs/PROJECT_GUIDE.md#troubleshooting).

## Documentation

- [Project Guide](docs/PROJECT_GUIDE.md)
