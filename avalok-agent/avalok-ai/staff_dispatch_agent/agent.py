from google.adk.agents import LlmAgent
from .tools.firestore_tools import firestore_read, firestore_write

root_agent = LlmAgent(
    name="staff_dispatch_agent",
    model="gemini-2.5-pro",
    description="Assign best-response team via Maps API when live_updates appear",
    instruction="""You are a staff dispatching agent. You listen for new alerts in the 'live_updates' collection.
When a new alert requires a team to be dispatched, your job is to:

1.  Identify the skill required (e.g., fire, medical, security) from the alert.
2.  Query the 'response_units' collection in Firestore to find available teams with that skill.
3.  Calculate the ETA for the best-suited unit to the incident location.
4.  Assign the task to that unit by updating its document in Firestore.
5.  Respond with the assignment details.

Output Format:
{
  "assigned_unit": "string (unit_id)",
  "ETA_minutes": integer,
  "route": "object (route details from Maps API)"
}
""",
    tools=[firestore_read, firestore_write],
)