import os


def get_shell_script(file_name: str) -> dict:
    """
    Get shell script from shell_scripts folder
    :param file_name:
    :return:
    """
    try:
        # Get the root directory
        root_dir = os.path.dirname(
            os.path.realpath(__file__)).rsplit(os.sep, 1)[0]
        # Get the shell script, which will create the venv
        shell_script = os.path.join(root_dir, "shell_scripts", file_name)

        return dict(success=True, script=shell_script)
    except Exception as e:

        return dict(success=False, message=str(e))
