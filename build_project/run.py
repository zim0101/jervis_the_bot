from build_project.project_builder import ProjectBuilder


def build_project_and_init_git(venv_root_directory: str, project_name: str,
                               language: str, framework: str) -> dict:
    """

    :param venv_root_directory:
    :param framework:
    :param language:
    :param project_name:
    :return:
    """
    project_builder = ProjectBuilder(venv_root_directory, project_name,
                                     language, framework)
    venv_response = project_builder.build_venv()
    if not venv_response["success"]:
        return venv_response
    git_response = project_builder.git_init()
    if not git_response["success"]:
        return git_response

    return dict(success=True, message=dict(
        venv_message=venv_response["message"],
        git_message=git_response["message"]
    ))
