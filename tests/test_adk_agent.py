import pytest
from unittest.mock import patch, MagicMock
from src.adk_agent.main import list_gcs_buckets

# Define a mock bucket class to simulate the GCS bucket object
class MockBucket:
    def __init__(self, name):
        self.name = name

@patch('src.adk_agent.main.storage.Client')
def test_list_gcs_buckets_success(mock_storage_client):
    """
    Tests the list_gcs_buckets function when buckets are found successfully.
    """
    # Arrange: Configure the mock to return a list of mock buckets
    mock_buckets = [MockBucket('bucket-1'), MockBucket('bucket-2')]
    mock_instance = mock_storage_client.return_value
    mock_instance.list_buckets.return_value = mock_buckets

    # Act: Call the function
    result = list_gcs_buckets()

    # Assert: Check if the output is the expected comma-separated string
    assert result == "bucket-1, bucket-2"
    mock_instance.list_buckets.assert_called_once()

@patch('src.adk_agent.main.storage.Client')
def test_list_gcs_buckets_no_buckets(mock_storage_client):
    """
    Tests the list_gcs_buckets function when no buckets are found.
    """
    # Arrange: Configure the mock to return an empty list
    mock_instance = mock_storage_client.return_value
    mock_instance.list_buckets.return_value = []

    # Act: Call the function
    result = list_gcs_buckets()

    # Assert: Check if the output is the 'no buckets' message
    assert result == "No buckets found in the project."
    mock_instance.list_buckets.assert_called_once()

@patch('src.adk_agent.main.storage.Client')
def test_list_gcs_buckets_error(mock_storage_client):
    """
    Tests the list_gcs_buckets function when an exception occurs.
    """
    # Arrange: Configure the mock to raise an exception
    error_message = "Test exception"
    mock_instance = mock_storage_client.return_value
    mock_instance.list_buckets.side_effect = Exception(error_message)

    # Act: Call the function
    result = list_gcs_buckets()

    # Assert: Check if the output is the expected error message
    assert f"An error occurred: {error_message}" in result
    mock_instance.list_buckets.assert_called_once()