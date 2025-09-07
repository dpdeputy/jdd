from .clients import get_slides_service

def create_presentation(title, content):
    """
    Creates a new Google Slides presentation with the given title and content.
    """
    service = get_slides_service()
    body = {"title": title}
    presentation = service.presentations().create(body=body).execute()
    presentation_id = presentation.get("presentationId")
    slide_id = presentation.get("slides")[0].get("objectId")

    element_id = f"TextBox_{slide_id}"
    requests = [
        {
            "createShape": {
                "objectId": element_id,
                "shapeType": "TEXT_BOX",
                "elementProperties": {
                    "pageObjectId": slide_id,
                    "size": {"height": {"magnitude": 100, "unit": "PT"}, "width": {"magnitude": 300, "unit": "PT"}},
                    "transform": {"scaleX": 1, "scaleY": 1, "translateX": 350, "translateY": 100, "unit": "PT"},
                },
            }
        },
        {
            "insertText": {
                "objectId": element_id,
                "insertionIndex": 0,
                "text": content,
            }
        },
    ]
    service.presentations().batchUpdate(
        presentationId=presentation_id, body={"requests": requests}
    ).execute()
    return presentation
