import os


def git_init(directory_path: str) -> dict:
    try:


        return dict(success=True, message="Venv has been built")
    except Exception as e:

        print(e)
        return dict(success=False, message="Venv build failed",
                    error_message=str(e))
