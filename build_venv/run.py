from build_venv.commands import build_venv_and_project_directory


def build_venv() -> dict:
    root_path: str = "/home/zim/Development/Python"
    env_name: str = "x_env"
    project_name: str = "project"
    response = build_venv_and_project_directory(root_path, env_name,
                                                project_name)
    if not response["success"]:
        print(response["message"])
        return dict(success=False, message=response["message"])
    return dict(success=False, message=response["message"])


if __name__ == '__main__':
    build_venv()
