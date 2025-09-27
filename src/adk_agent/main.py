from google.adk.agents import LlmAgent
from google.adk.tools.function_tool import FunctionTool
from google.cloud import storage

def list_gcs_buckets() -> str:
    """
    Lists all Google Cloud Storage buckets in the project.

    Returns:
        A string containing a comma-separated list of bucket names.
    """
    try:
        storage_client = storage.Client()
        buckets = storage_client.list_buckets()
        bucket_names = [bucket.name for bucket in buckets]
        if not bucket_names:
            return "No buckets found in the project."
        return ", ".join(bucket_names)
    except Exception as e:
        return f"An error occurred: {e}"

def run_agent():
    """
    Initializes and runs the GCS bucket-listing agent.
    """
    # Create a tool from the function
    gcs_tool = FunctionTool(func=list_gcs_buckets)

    # Create an agent with the GCS bucket listing tool
    agent = LlmAgent(
        tools=[gcs_tool]
    )

    # The prompt for the agent
    prompt = "Please list all of the Google Cloud Storage buckets in the project."

    # Run the agent with the prompt
    print(f"-> User Prompt: {prompt}")
    response = agent.run(prompt)
    print(f"<- Agent Response: {response}")

if __name__ == "__main__":
    print("Starting GCS Bucket Listing Agent...")
    run_agent()