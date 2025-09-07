from .clients import get_docs_service

def create_doc(title, content):
    """
    Creates a new Google Doc with the given title and content.
    """
    service = get_docs_service()
    body = {"title": title}
    doc = service.documents().create(body=body).execute()
    document_id = doc.get("documentId")
    requests = [
        {
            "insertText": {
                "location": {
                    "index": 1,
                },
                "text": content,
            }
        }
    ]
    service.documents().batchUpdate(
        documentId=document_id, body={"requests": requests}
    ).execute()
    return doc
