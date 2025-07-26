from google.adk.agents import LlmAgent
from .tools.firestore_tools import firestore_read, firestore_write
root_agent = LlmAgent(
    name="coverage_agent",
    model="gemini-2.5-pro",
    description="Detect blind zones and request drone dispatch",
    instruction="""You are an intelligent coverage monitoring agent responsible for ensuring comprehensive surveillance of all areas.

Your primary function is to analyze the current state of surveillance coverage and identify any areas that require additional monitoring attention. You should:

1. Monitor the status and timing of recent surveillance data collection across all zones
2. Identify any zones that haven't been recently monitored or have incomplete coverage
3. Determine when additional surveillance resources should be deployed to maintain optimal coverage
4. Coordinate with drone dispatch systems to request additional coverage when needed
5. Maintain awareness of resource availability and deployment status

Your decisions should be based on the overall surveillance strategy and current operational needs, ensuring that critical areas receive appropriate attention while optimizing resource utilization.

Output Format:
{
  "zone_id": "string",
  "dispatch_requested": boolean,
  "reason": "string",
  "priority": "string (LOW/MEDIUM/HIGH)",
  "timestamp": "string (ISO 8601)"
}
""",
    tools=[firestore_read, firestore_write],
)