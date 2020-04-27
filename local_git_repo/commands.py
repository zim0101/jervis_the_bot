import os


def git_init(directory_path: str) -> dict:
    """
    Initiate a local git repo
    :param directory_path: str
    :return: dict
    """
    try:
        command = 'cd ' + directory_path + ' && ' + 'git init'
        os.system(command)

        return dict(success=True, message="Initialized git")
    except Exception as e:

        return dict(success=False, message=str(e))


def create_readme_and_git_ignore(directory_path: str) -> dict:
    """
    Create README.md and gitignore file
    :param directory_path: str
    :return: dict
    """
    try:
        add_readme_command = 'cd ' + directory_path + ' && ' + 'touch README.md'
        add_gitignore_command = 'cd ' + directory_path + ' && ' \
                                + 'touch .gitignore'
        os.system(add_readme_command)
        os.system(add_gitignore_command)

        return dict(success=True, message="Added readme and gitignore")
    except Exception as e:

        return dict(success=False, message=str(e))


def git_add(directory_path: str) -> dict:
    """
    Add files to git
    :param directory_path:
    :return:
    """
    try:
        command = 'cd ' + directory_path + ' && ' + 'git add .'
        os.system(command)

        return dict(success=True, message="Added files to git")
    except Exception as e:

        return dict(success=False, message=str(e))


def git_commit(directory_path: str) -> dict:
    """
    Commit all changes to git
    :param directory_path:
    :return:
    """
    try:
        command = 'cd ' + directory_path + ' && ' \
                  + 'git commit -m "Initial commit"'
        os.system(command)

        return dict(success=True, message="Committed all changes to git")
    except Exception as e:

        return dict(success=False, message=str(e))


def git_process(directory_path: str) -> dict:
    try:
        git_init_response = git_init(directory_path)
        if not git_init_response["success"]:

            return dict(success=False, message=git_init_response["message"])

        add_files_response = create_readme_and_git_ignore(directory_path)
        if not add_files_response["success"]:

            return dict(success=False, message=add_files_response["message"])

        git_add_response = git_add(directory_path)
        if not git_add_response["success"]:

            return dict(success=False, message=git_add_response["message"])

        git_commit_response = git_commit(directory_path)
        if not git_commit_response["success"]:

            return dict(success=False, message=git_commit_response["message"])

        return dict(success=True, message="Local git process successful")
    except Exception as e:
        
        return dict(success=False, message=str(e))