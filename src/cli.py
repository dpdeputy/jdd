import subprocess
import typer

app = typer.Typer()

DBT_PROJECT_DIR = "dbt/jaffle_shop"

def run_dbt_command(command: list[str]):
    """
    Runs a dbt command.
    """
    dbt_command = [
        "dbt",
        *command,
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

    if result.returncode != 0:
        typer.secho(f"Error running dbt {command[0]}:", fg=typer.colors.RED)
        typer.echo(result.stderr)
        raise typer.Exit(code=result.returncode)

    typer.echo(result.stdout)

@app.command()
def build():
    """
    Runs dbt build.
    """
    run_dbt_command(["build"])

@app.command()
def test():
    """
    Runs dbt test.
    """
    run_dbt_command(["test"])

@app.command()
def run():
    """
    Runs dbt run.
    """
    run_dbt_command(["run"])

@app.command()
def seed():
    """
    Runs dbt seed.
    """
    run_dbt_command(["seed"])

@app.command()
def deps():
    """
    Runs dbt deps.
    """
    run_dbt_command(["deps"])

if __name__ == "__main__":
    app()
