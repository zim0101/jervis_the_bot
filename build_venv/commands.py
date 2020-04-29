import subprocess


def build_virtual_environment(path: str, venv_name: str) -> dict:
    """
    Build a new virtual environment for your project, this is where we run this
    command:
    python3 -m venv venv_name
    :param path:
    :param venv_name: str
    :return: dict
    """
    try:
        command: str = 'cd '+path+' && '+'python3 -m venv ' + venv_name
        subprocess.run(command, shell=True)

        return dict(success=True, message="Virtual environment has been built")
    except Exception as e:
        print(e)
        return dict(success=False, message=str(e))


def install_wheel(path: str, venv_name: str) -> dict:
    """
    Activate venv then install wheel for future package installation then
    deactivate venv again
    :param path: str
    :param venv_name: str
    :return: dict
    """
    try:
        command: str = path+'/'+venv_name+'/bin/python3 -m'+' pip install wheel'
        subprocess.run(command, shell=True)

        return dict(success=True, message="Virtual environment activated")
    except Exception as e:
        print(e)
        return dict(success=False, message=str(e))


def build_project_directory(path: str, venv_name: str,
                            project_name: str) -> dict:
    """
    Will create a new directory for project
    :param venv_name: str
    :param path: str
    :param project_name: str
    :return: dict
    """

    go_to_root_directory = 'cd ' + path + '/' + venv_name
    make_directory = ' && mkdir ' + project_name
    commands = go_to_root_directory + make_directory
    try:
        subprocess.run(commands, shell=True)

        return dict(success=True, message="Project directory created")
    except Exception as e:

        return dict(success=False, message=str(e))


def delete_virtual_environment(path: str, venv_name: str):
    """
    Delete virtual environment
    :param path: str
    :param venv_name: str
    """
    command = 'cd '+path+' && rm -rf '+venv_name
    subprocess.run(command, shell=True)


def build_venv_and_project_directory(path: str, venv_name: str,
                                     project_path: str):
    """
    :param path: str
    :param venv_name: str
    :param project_path: str
    :return: dict
    """
    try:
        build_venv = build_virtual_environment(path, venv_name)
        if not build_venv["success"]:
            return dict(success=False, message=build_venv["message"])

        installation = install_wheel(path, venv_name)
        build_project = build_project_directory(path, venv_name, project_path)

        if not installation["success"] or not build_project["success"]:
            delete_virtual_environment(path, venv_name)

            return dict(success=False, message=dict(
                wheel_installation_message=installation["message"],
                build_project_message=build_project["message"]
            ))

        return dict(success=True, message="OK")
    except Exception as e:

        return dict(success=False, message=str(e))
