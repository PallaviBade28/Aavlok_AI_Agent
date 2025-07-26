import os
import json
from typing import Any, Dict
from google.cloud import firestore
from google.oauth2 import service_account

# Load service account key
KEY_PATH = os.path.join(os.path.dirname(__file__), "project-avalok-dd7e4ec192cb.json")
with open(KEY_PATH) as f:
    key_data = json.load(f)

# Initialize Firestore client
credentials = service_account.Credentials.from_service_account_info(key_data)
db = firestore.Client(credentials=credentials, project=key_data["project_id"])
print("[Firestore Init] Authenticated for incident_agent.")

def _initialize_collections():
    """
    Ensure the primary collection for this agent exists by
    writing a dummy '_init' document if needed.
    """
    primary = "raw_incidents"
    init_ref = db.collection(primary).document("_init")
    init_ref.set({"_initialized": True, "timestamp": firestore.SERVER_TIMESTAMP})
    print(f"[Firestore Init] Collection '{primary}' initialized.")

_initialize_collections()

def firestore_read(collection: str, document_id: str) -> Dict[str, Any]:
    """
    Read a document from Firestore.
    """
    try:
        doc = db.collection(collection).document(document_id).get()
        return doc.to_dict() if doc.exists else {"error": "Not found"}
    except Exception as e:
        return {"error": str(e)}


def firestore_write(document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Write data to the agent's primary Firestore collection.
    """
    collection = "raw_incidents"
    try:
        doc_ref = db.collection(collection).add(data)
        return {
            "success": True,
            "collection": collection,
            "document_id": doc_ref[1].id
        }
    except Exception as e:
        return {"error": str(e)}