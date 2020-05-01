from build_project.commands import ProjectBuilder


def build_project(venv_root_directory: str, project_name: str, language: str,
                  framework: str) -> dict:
    """

    :param venv_root_directory:
    :param framework:
    :param language:
    :param project_name:
    :return:
    """
    project_builder = ProjectBuilder(venv_root_directory, project_name,
                                     language, framework)
    response = project_builder.build_venv()

    return response
