from build_project.run import build_project_and_init_git
from github.run import create_repo_and_push_local_changes


def build_project_with_git(work_directory: str, path: str, project_name: str,
                           language: str, framework: str = None):
    """
    :param work_directory:
    :param path:
    :param project_name:
    :param language:
    :param framework:
    :return:
    """
    venv_building_response = build_project_and_init_git(work_directory,
                                                        project_name, language,
                                                        framework)
    if not venv_building_response["success"]:
        return venv_building_response

    github_repo_response = create_repo_and_push_local_changes(project_name,
                                                              path)
    if not github_repo_response["success"]:
        return github_repo_response

    return dict(success=True, message=dict(
        venv_building_response=venv_building_response["message"],
        github_repo_response=github_repo_response["message"]
    ))


if __name__ == '__main__':
    # These variables will be given by user later in the GUI
    work_path: str = "/home/trex/Development/PYTHON_PROJECTS"
    project: str = "github_api_python"
    git_path: str = work_path + '/' + project + "_venv" + '/' + project
    project_language = 'python'
    project_framework = None

    # This single function is responsible for building venv and initiating git
    build_project_with_git(work_path, git_path, project, project_language,
                           project_framework)
