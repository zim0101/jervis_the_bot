from git_local.commands import git_init


def run_git_process(directory_path: str) -> dict:
    response = git_init(directory_path)

    return response

