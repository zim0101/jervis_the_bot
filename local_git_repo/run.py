from local_git_repo.commands import git_process


def run_git_process(directory_path: str) -> dict:
    response = git_process(directory_path)
    if not response["success"]:
        return dict(success=False, message=response["message"])

    return dict(success=True, message=response["message"])


if __name__ == '__main__':
    path = '/home/zim/Development/Python/x_env/project'
    run_git_process(path)
