from fastapi.testclient import TestClient
from unittest.mock import patch
from src.app import app

client = TestClient(app)

@patch("src.app.create_doc")
@patch("src.app.create_presentation")
def test_create_presentation_endpoint(mock_create_presentation, mock_create_doc):
    mock_create_doc.return_value = {"documentId": "fake_doc_id"}
    mock_create_presentation.return_value = {"presentationId": "fake_presentation_id"}

    response = client.post(
        "/presentations",
        json={"title": "Test Title", "content": "Test Content"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "document_id": "fake_doc_id",
        "presentation_id": "fake_presentation_id",
    }
    mock_create_doc.assert_called_once_with("Test Title", "Test Content")
    mock_create_presentation.assert_called_once_with("Test Title", "Test Content")
