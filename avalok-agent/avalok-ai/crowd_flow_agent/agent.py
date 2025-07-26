from google.adk.agents import LlmAgent
from .tools.firestore_tools import firestore_read, firestore_write
root_agent = LlmAgent(
    name="crowd_flow_agent",
    model="gemini-2.5-flash",
    description="Estimate current density and forecast 15min ahead per zone",
    instruction="""You are an autonomous forecasting agent that analyzes crowd density.
For each drone video clip you receive, you must:

1.  Use vision analysis to detect the number of people within different zones.
2.  Generate a time series of the estimated crowd density for each zone.
3.  Use forecasting models to predict the crowd density for the next 15 minutes.
4.  Store the complete forecast data in a Firestore document.

Output Format:
{
  "current_density": integer,
  "forecast_density": [integer],
  "confidence": float,
  "zone_id": "string"
}
""",
    tools=[firestore_read, firestore_write],
)