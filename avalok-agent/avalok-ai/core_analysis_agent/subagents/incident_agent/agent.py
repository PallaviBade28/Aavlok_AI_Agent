from google.adk.agents import LlmAgent
from .tools.firestore_tools import firestore_read, firestore_write
root_agent = LlmAgent(
    name="incident_agent",
    model="gemini-2.5-pro",
    description="Detect fight, fire, collapse in clip",
    instruction="""You are an incident detection agent analyzing drone footage from an event.
Your task is to analyze the provided video and audio clip to detect critical anomalies.

1.  Analyze the clip to identify events such as fights, fire, smoke, crowd surges, or medical emergencies (like a collapse or fall).
2.  Return a structured JSON response summarizing any incident found.
3.  Write the full result to the 'raw_incidents' collection in Firestore.
4.  If an incident is detected with confidence greater than 0.8, also log it as a high-priority alert in the 'live_alerts' collection.

Output Format:
{
  "incident_type": "string (e.g., fire, fight, none)",
  "confidence": float,
  "zone_id": "string",
  "timestamp": "string (ISO 8601)"
}
""",
    tools=[firestore_read, firestore_write],
)