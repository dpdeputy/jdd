import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES_DOCS = ["https://www.googleapis.com/auth/documents"]
SCOPES_SLIDES = ["https://www.googleapis.com/auth/presentations"]

def get_credentials(scopes):
    """
    Gets user credentials for the Google API.
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", scopes)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", scopes
            )
            creds = flow.run_local_server(port=0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds

def get_docs_service():
    """
    Returns a Google Docs service object.
    """
    creds = get_credentials(SCOPES_DOCS)
    return build("docs", "v1", credentials=creds)

def get_slides_service():
    """
    Returns a Google Slides service object.
    """
    creds = get_credentials(SCOPES_SLIDES)
    return build("slides", "v1", credentials=creds)
