import os
import json
from typing import Any, Dict
from google.cloud import firestore
from google.oauth2 import service_account

# Path to the service account key file
KEY_FILENAME = "project-avalok-dd7e4ec192cb.json"
KEY_PATH = os.path.join(os.path.dirname(__file__), "project-avalok-dd7e4ec192cb.json")

# --- 1) Initialize Firestore client with explicit credentials ---
try:
    with open(KEY_PATH) as f:
        key_data = json.load(f)
    credentials = service_account.Credentials.from_service_account_info(key_data)
    db = firestore.Client(credentials=credentials, project=key_data["project_id"])
    print("[Firestore Init] Authenticated with service account.")
except Exception as e:
    print(f"[Firestore Init] FAILED to authenticate: {e}")
    db = None

# --- 2) Ensure required collections exist by writing a single "init" doc ---
def _initialize_collections():
    if db is None:
        return

    required_collections = ["live_updates", "response_units"]
    for collection_name in required_collections:
        try:
            # Check if there's at least one document in the collection
            docs = list(db.collection(collection_name).limit(1).stream())
            if not docs:
                # No documents exist, create a dummy initialization document
                db.collection(collection_name).document("_init").set({"_initialized": True})
                print(f"[Firestore Init] Created collection '{collection_name}' with _init document.")
        except Exception as e:
            print(f"[Firestore Init] Failed to initialize '{collection_name}': {e}")

_initialize_collections()

def firestore_read(collection: str, document_id: str) -> Dict[str, Any]:
    """
    Read a document from Firestore.
    
    Args:
        collection: The Firestore collection name
        document_id: The document ID to read
        
    Returns:
        The document data as a dictionary, or an error message if failed
    """
    if db is None:
        return {"error": "Firestore client not initialized. Check your Google Cloud credentials."}
        
    try:
        doc_ref = db.collection(collection).document(document_id)
        doc = doc_ref.get()
        
        if doc.exists:
            return doc.to_dict()
        else:
            return {"error": f"Document {document_id} not found in collection {collection}"}
            
    except Exception as e:
        return {"error": str(e)}

def firestore_write(document_id: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Write data to the agent's primary Firestore collection.
    """
    collection = "response_units"
    try:
        doc_ref = db.collection(collection).add(data)
        return {
            "success": True,
            "collection": collection,
            "document_id": doc_ref[1].id
        }
    except Exception as e:
        return {"error": str(e)}

# Make functions available when importing from this module
__all__ = ['firestore_read', 'firestore_write']