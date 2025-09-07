import subprocess

DBT_PROJECT_DIR = "dbt/jaffle_shop"
DBT_EXECUTABLE = "/app/.venv/bin/dbt"

dbt_command = [
    DBT_EXECUTABLE,
    "run",
    "--project-dir",
    ".",
    "--profiles-dir",
    ".",
]

result = subprocess.run(
    dbt_command,
    capture_output=True,
    text=True,
    cwd=DBT_PROJECT_DIR
)

print("--- STDOUT ---")
print(result.stdout)
print("--- STDERR ---")
print(result.stderr)
print(f"Return code: {result.returncode}")
