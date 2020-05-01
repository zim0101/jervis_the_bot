from build_project.run import build_project
# from git_local.run import run_git_process


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
    venv_building_response = build_project(work_directory, project_name,
                                           language, framework)

    return venv_building_response


if __name__ == '__main__':
    # These variables will be given by user later in the GUI
    work_path: str = "/home/trex/Development/PYTHON_PROJECTS"
    project: str = "project"
    git_path: str = work_path + '/' + project + "_venv" + '/' + project
    project_language = 'python'
    project_framework = None

    # This single function is responsible for building venv and initiating git
    build_project_with_git(work_path, git_path, project, project_language,
                           project_framework)
