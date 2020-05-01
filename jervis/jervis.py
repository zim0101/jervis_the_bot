from build_project.run import build_project
from git_local.run import run_git_process


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
    if not venv_building_response["success"]:
        return venv_building_response
    local_git_response = run_git_process(path)
    if not local_git_response["success"]:
        return local_git_response

    return dict(success=True, message=[venv_building_response["message"],
                                       local_git_response["message"]])


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
