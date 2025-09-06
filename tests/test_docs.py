import subprocess
import shutil

def test_mkdocs_build():
    """
    Tests that the mkdocs build command runs successfully.
    """
    # The build command will create a 'site' directory.
    # We should clean it up before running the test to ensure a clean build.
    shutil.rmtree("site", ignore_errors=True)

    result = subprocess.run(
        ["mkdocs", "build"],
        capture_output=True,
        text=True
    )

    # Assert that the command completed successfully.
    assert result.returncode == 0, f"mkdocs build failed with output:\n{result.stderr}"

    # Clean up the 'site' directory after the test.
    shutil.rmtree("site", ignore_errors=True)
