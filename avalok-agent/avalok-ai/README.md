# Project Drishti AI – ADK Agents

## Setup

1. Create `.venv`, activate, and install:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Copy `.env.example` to `.env` in each agent folder and set:
```
GOOGLE_API_KEY=your_api_key
GOOGLE_GENAI_USE_VERTEXAI=TRUE
```

## Running

```bash
# From project root
adk web
```

Select any agent from the dropdown to test its behavior.

## Agents

- **LostFoundAgent** – on-demand visual matching
- **CrowdFlowAgent** – density + forecasting
- **CoreAnalysisAgent** – Incident, Sentiment, Coverage in parallel
- **LiveUpdateSynthesizer** – meta-agent summarizing alerts
- **StaffDispatcherAgent** – auto-assign response teams