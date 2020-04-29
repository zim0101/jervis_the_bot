from build_venv.commands import build_venv_and_project_directory


def build_venv(root_path: str, env_name: str, project_name: str) -> dict:
    """

    :param root_path:
    :param env_name:
    :param project_name:
    :return:
    """
    response = build_venv_and_project_directory(root_path, env_name,
                                                project_name)
    if not response["success"]:
        print(response["message"])
        return dict(success=False, message=response["message"])

    return dict(success=True, message=response["message"])

