import subprocess
import sys

def run_gcloud_command(command):
    """Runs a gcloud command and returns the output."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8'
        )
        return result.stdout.strip()
    except FileNotFoundError:
        print("Error: 'gcloud' command not found. Please ensure the Google Cloud SDK is installed and in your PATH.")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"Error executing gcloud command: {e}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)

def list_projects():
    """Lists all GCP projects."""
    print("Listing GCP projects:")
    projects = run_gcloud_command(["gcloud", "projects", "list"])
    print(projects)

if __name__ == "__main__":
    list_projects()
