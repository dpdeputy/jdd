import unittest
from unittest.mock import patch, MagicMock

from src.google_services.clients import get_docs_service, get_slides_service
from src.google_services.docs import create_doc
from src.google_services.slides import create_presentation


class TestGoogleServices(unittest.TestCase):

    @patch("src.google_services.clients.get_credentials")
    @patch("src.google_services.clients.build")
    def test_get_docs_service(self, mock_build, mock_get_credentials):
        mock_get_credentials.return_value = "fake_credentials"
        get_docs_service()
        mock_build.assert_called_once_with("docs", "v1", credentials="fake_credentials")

    @patch("src.google_services.clients.get_credentials")
    @patch("src.google_services.clients.build")
    def test_get_slides_service(self, mock_build, mock_get_credentials):
        mock_get_credentials.return_value = "fake_credentials"
        get_slides_service()
        mock_build.assert_called_once_with("slides", "v1", credentials="fake_credentials")

    @patch("src.google_services.docs.get_docs_service")
    def test_create_doc(self, mock_get_docs_service):
        mock_service = MagicMock()
        mock_get_docs_service.return_value = mock_service
        mock_service.documents().create().execute.return_value = {"documentId": "fake_doc_id"}

        doc = create_doc("Test Title", "Test Content")
        self.assertEqual(doc, {"documentId": "fake_doc_id"})
        mock_service.documents().create(body={"title": "Test Title"}).execute.assert_called_once()
        mock_service.documents().batchUpdate(
            documentId="fake_doc_id",
            body={
                "requests": [
                    {
                        "insertText": {
                            "location": {"index": 1},
                            "text": "Test Content",
                        }
                    }
                ]
            },
        ).execute.assert_called_once()

    @patch("src.google_services.slides.get_slides_service")
    def test_create_presentation(self, mock_get_slides_service):
        mock_service = MagicMock()
        mock_get_slides_service.return_value = mock_service
        mock_service.presentations().create().execute.return_value = {
            "presentationId": "fake_presentation_id",
            "slides": [{"objectId": "fake_slide_id"}],
        }

        presentation = create_presentation("Test Title", "Test Content")
        self.assertEqual(
            presentation,
            {
                "presentationId": "fake_presentation_id",
                "slides": [{"objectId": "fake_slide_id"}],
            },
        )
        mock_service.presentations().create(
            body={"title": "Test Title"}
        ).execute.assert_called_once()
        mock_service.presentations().batchUpdate.assert_called_once()

if __name__ == "__main__":
    unittest.main()
