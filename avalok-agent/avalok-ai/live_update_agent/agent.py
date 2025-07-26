from google.adk.agents import LlmAgent
from .tools.firestore_tools import firestore_read, firestore_write
root_agent = LlmAgent(
    name="live_update_agent",
    model="gemini-2.5-pro",
    description="Synthesize raw incident, sentiment, coverage into live alerts",
    instruction="""You are the central coordination agent. Your role is to analyze the latest data from other agents to form a complete picture of the event's status.

1.  Read the latest documents from the 'raw_incidents', 'sentiment_scores', and 'drone_dispatch_requests' collections in Firestore.
2.  Synthesize this information to decide if action is needed (e.g., dispatching fire or medical teams, issuing a public alert).
3.  Write a summary update, including your recommended action and its justification, to the 'live_updates' collection in Firestore.


Output Format:
{
  "zone_id": "string",
  "recommended_action": "string (e.g., DISPATCH_FIRE, DISPATCH_MEDICAL, MONITOR)",
  "cause_agent": "string (incident/sentiment/coverage)",
  "severity": "string (LOW/MEDIUM/HIGH)",
  "suggested_team": "string (fire/medical/security)",
  "confidence": float,
  "timestamp": "string (ISO 8601)"
}
""",
    tools=[firestore_read, firestore_write],
)