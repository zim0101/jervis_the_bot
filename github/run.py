from github.services import GithubService


def create_repo_and_push_local_changes(repo_name: str, git_directory: str):
    github_service = GithubService(repo_name, git_directory)
    repository_api_response = github_service.create_repo()
    if not repository_api_response["success"]:
        return repository_api_response
    push_response = github_service.git_add_remote_origin_and_push_master()
    if not push_response["success"]:
        return push_response

    return dict(success=True, message=dict(
        repository_api_response=repository_api_response["message"],
        push_response=push_response["message"],
    ))
