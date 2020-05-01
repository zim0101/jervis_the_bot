import subprocess
from utils.helpers import get_shell_script


def git_init(git_directory: str) -> dict:
    try:
        git_init_shell_script = "git_init.sh"
        shell_script = get_shell_script(git_init_shell_script)
        if not shell_script["success"]:
            return dict(success=False, message="Shell script not found")
        # execute and get the output of the shell script
        output = subprocess.check_output([
            shell_script["script"],
            str(git_directory)
        ])
        print(output.decode())

        return dict(success=True, message="Venv has been built")
    except Exception as e:

        print(e)
        return dict(success=False, message="Venv build failed",
                    error_message=str(e))
