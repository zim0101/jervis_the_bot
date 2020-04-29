import os


def git_init(directory_path: str) -> dict:
    """
    Initiate a local git repo
    :param directory_path: str
    :return: dict
    """
    command = 'cd ' + directory_path + ' && ' + 'git init'
    result = os.system(command)
    print(result)
    return dict(success=True, message="Initialized git") if result == 0 \
        else dict(success=False, message="Git init failed")


def create_readme_and_git_ignore(directory_path: str) -> dict:
    """
    Create README.md and gitignore file
    :param directory_path: str
    :return: dict
    """
    add_readme_command = 'cd ' + directory_path + ' && ' + 'touch README.md'
    add_gitignore_command = ' && touch .gitignore'
    command = add_readme_command + add_gitignore_command
    result = os.system(command)
    print(result)

    return dict(success=True, message="Initialized git") if result == 0 \
        else dict(success=False, message="Git init failed")


def git_add(directory_path: str) -> dict:
    """
    Add files to git
    :param directory_path:
    :return:
    """
    command = 'cd ' + directory_path + ' && ' + 'git add .'
    result = os.system(command)
    print(result)

    return dict(success=True, message="Initialized git") if result == 0 \
        else dict(success=False, message="Git init failed")


def git_commit(directory_path: str) -> dict:
    """
    Commit all changes to git
    :param directory_path:
    :return:
    """
    command = 'cd ' + directory_path + ' && ' + 'git commit -m "Initial commit"'
    result = os.system(command)
    print(result)

    return dict(success=True, message="Initialized git") if result == 0 \
        else dict(success=False, message="Git init failed")


def git_process(directory_path: str) -> dict:
    """

    :param directory_path: str
    :return: dict
    """
    try:
        print("Inside git_process method")
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
