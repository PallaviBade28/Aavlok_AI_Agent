from google.adk.agents import ParallelAgent, LlmAgent
from .subagents.incident_agent import root_agent as incident_agent
from .subagents.sentiment_agent import root_agent as sentiment_agent
from .subagents.coverage_agent import root_agent as coverage_agent
from .subagents.crowd_flow_agent import root_agent as crowd_flow_agent
from .tools.firestore_tools import firestore_read, firestore_write
root_agent = ParallelAgent(
    name="core_analysis_agent",
    sub_agents=[incident_agent, sentiment_agent, coverage_agent, crowd_flow_agent],
    description="Run Incident, Sentiment , crowd flow, and Blind-Spot Dispatch analysis in parallel on each clip",
    tools=[firestore_read, firestore_write],
)