from git_local.commands import git_process


def run_git_process(directory_path: str) -> dict:
    print("Inside run_git_process method")
    response = git_process(directory_path)
    if not response["success"]:
        return dict(success=False, message=response["message"])

    return dict(success=True, message=response["message"])

