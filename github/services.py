import subprocess
import requests
from settings import GITHUB_ACCESS_TOKEN, GITHUB_USERNAME
from utils.helpers import get_shell_script


class GithubService:
    """
        Github service
    """

    __github_push_shell_script: str = "github_push.sh"
    __repo_creation_end_point: str = "https://api.github.com/user/repos"
    __headers = {
        'Authorization': 'token ' + GITHUB_ACCESS_TOKEN
    }

    def __init__(self, repo_name, git_directory):
        """

        :param repo_name:
        :param git_directory:
        """
        self.repo_name = repo_name
        self.git_directory = git_directory

    def __github_repo_remote_origin(self):
        """

        :return:
        """
        return "git@github.com:"+GITHUB_USERNAME+'/'+self.repo_name+'.git'

    def create_repo(self) -> dict:
        """

        :return:
        """
        try:
            with requests.Session() as s:
                s.headers.update(self.__headers)
                resp = s.post(self.__repo_creation_end_point, json={
                    "name": self.repo_name
                })
                print(resp.content.decode())

                return dict(success=True,
                            message="Github repository has been created")
        except Exception as e:

            return dict(success=False, message=str(e))

    def git_add_remote_origin_and_push_master(self):
        """

        :return:
        """
        try:
            shell_script = get_shell_script(self.__github_push_shell_script)
            if not shell_script["success"]:
                return dict(success=False, message="Shell script not found")
            # execute and get the output of the shell script
            output = subprocess.check_output([
                shell_script["script"],
                str(self.git_directory),
                str(self.__github_repo_remote_origin()),
            ])
            print(output.decode())

            return dict(success=True, message="Venv has been built")
        except Exception as e:

            print(e)
            return dict(success=False, message="Venv build failed",
                        error_message=str(e))
