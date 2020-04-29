from build_venv.run import build_venv
from git_local.run import run_git_process


def build_python_project_with_git(root_path: str, env_name: str,
                                  project_name: str, path: str):
    """

    :param root_path: str
    :param env_name: str
    :param project_name: str
    :param path: str
    :return: dict
    """
    venv_building_response = build_venv(root_path, env_name, project_name)
    if not venv_building_response["success"]:
        return dict(success=False, message=venv_building_response["message"])

    local_git_response = run_git_process(path)
    if not local_git_response["success"]:
        return dict(success=False, message=local_git_response["message"])


if __name__ == '__main__':
    # These variables will be given by user later in the GUI
    work_path: str = "/home/zim/Development/Jervis_project_bot_testing"
    venv: str = "x_env"
    project: str = "project"
    git_path: str = work_path + '/' + venv + '/' + project

    # This single function is responsible for building venv and initiating git
    build_python_project_with_git(work_path, venv, project, git_path)
