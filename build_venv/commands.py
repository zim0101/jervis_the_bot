import os


def goto_root_directory(root_path: str) -> dict:
    """
    Jervis will go to the root directory for the project
    :param root_path: str
    :return: dict
    """
    try:
        os.chdir(root_path)
        print("goto_root_directory " + os.getcwd())

        return dict(success=True, message="Jervis reached the directory")
    except FileNotFoundError as e:

        return dict(success=False, message=str(e))


def build_virtual_environment(env_name: str) -> dict:
    """
    Build a new virtual environment for your project, this is where we run this
    command:
    python3 -m venv env_name
    :param env_name: str
    :return: dict
    """
    try:
        command = 'python3 -m venv ' + env_name
        os.system(command)

        return dict(success=True, message="Virtual environment has been built")
    except Exception as e:
        return dict(success=False, message=str(e))


def activate_virtual_environment(env_name: str):
    """
    Activate the venv from outside of venv
    :param env_name:
    :return:
    """
    try:
        command = '. ' + env_name + '/bin/activate'
        activation = os.system(command)
        print("Activate result"+str(activation))
        return dict(success=True, message="Virtual environment activated")
    except Exception as e:
        return dict(success=False, message=str(e))


def goto_venv_directory(root_path: str, env_name: str) -> dict:
    """
    Go to the venv directory
    :param root_path:
    :param env_name:
    :return:
    """
    try:
        os.chdir(root_path + '/' + env_name)
        print("goto_venv_directory " + os.getcwd())

        return dict(success=True, message="Jervis reached the directory")
    except FileNotFoundError as e:

        return dict(success=False, message=str(e))


def deactivate_virtual_environment(root_path: str, env_name: str) -> dict:
    """
    Deactivate the venv
    :return: dict
    """
    try:
        print("deactivate_virtual_environment " + os.getcwd())
        command = "cd "+root_path+'/'+env_name+' && deactivate'
        os.system(command)

        return dict(success=True, message="Virtual environment deactivated")
    except Exception as e:
        return dict(success=False, message=str(e))


def install_wheel() -> dict:
    """
    Activate venv then install wheel for future package installation then
    deactivate venv again
    :return: dict
    """
    try:

        command = 'pip3 install wheel'
        os.system(command)

        return dict(success=True, message="Virtual environment activated")
    except Exception as e:
        print(e)
        return dict(success=False, message=str(e))


def build_project_directory(project_name: str) -> dict:
    """
    Will create a new directory for project
    :param project_name: str
    :return: dict
    """
    try:
        print("build_project_directory " + os.getcwd())
        os.mkdir(project_name)

        return dict(success=True, message="Project directory created")
    except Exception as e:

        return dict(success=False, message=str(e))


def goto_project_directory(root_path: str, directory_name: str) -> dict:
    """
    Will enter in project directory from virtual environment root directory
    :param root_path: str
    :param directory_name: str
    :return: dict
    """
    try:
        os.chdir(root_path + '/' + directory_name)
        print(os.getcwd())

        return dict(success=True, message="Jervis is in project directory")
    except FileNotFoundError as e:

        return dict(success=False, message=str(e))


def build_venv_and_project_directory(root_path: str, env_name: str,
                                     project_path: str):
    try:
        goto_root_directory(root_path)
        build_virtual_environment(env_name)
        activate_virtual_environment(env_name)
        goto_venv_directory(root_path, env_name)
        install_wheel()
        deactivate_virtual_environment(root_path, env_name)
        build_project_directory(project_path)
        goto_project_directory(root_path, project_path)

        return dict(success=True, message="OK")
    except Exception as e:
        print(e)
        return dict(success=False, message="Not OK")
