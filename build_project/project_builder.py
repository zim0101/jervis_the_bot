import subprocess
from utils.helpers import get_shell_script


class ProjectBuilder:
    __build_venv_shell_script: str = "build_venv.sh"

    """
        Build project with name, language and framework
    """

    def __init__(self, venv_root_directory, project_name: str, language: str,
                 framework: str):
        """

        :param venv_root_directory:
        :param project_name:
        :param language:
        :param framework:
        """
        self.venv_root_directory = venv_root_directory
        self.framework = framework
        self.language = language
        self.project_name = project_name

    def __get_venv(self):
        return self.project_name + '_venv'

    def __get_git_directory(self):
        return self.venv_root_directory + '/'+self.__get_venv() \
               + '/'+self.project_name

    def build_venv(self) -> dict:
        """
        For python project we will create venv
        :return: dict
        """
        venv_name: str = self.__get_venv()
        try:
            shell_script = get_shell_script(self.__build_venv_shell_script)
            if not shell_script["success"]:
                return dict(success=False, message="Shell script not found")
            # execute and get the output of the shell script
            output = subprocess.check_output([
                shell_script["script"],
                str(self.venv_root_directory),
                str(venv_name),
                str(self.project_name)
            ])
            print(output.decode())

            return dict(success=True, message="Venv has been built")
        except Exception as e:

            print(e)
            return dict(success=False, message="Venv build failed",
                        error_message=str(e))

    def git_init(self) -> dict:
        """
        :return:
        """
        git_directory = self.__get_git_directory()
        git_init_shell_script = "git_init.sh"
        try:
            shell_script = get_shell_script(git_init_shell_script)
            if not shell_script["success"]:
                return dict(success=False, message="Shell script not found")
            # execute and get the output of the shell script
            output = subprocess.check_output([
                shell_script["script"],
                str(git_directory)
            ])
            print(output.decode())

            return dict(success=True, message="Venv has been built")
        except Exception as e:

            print(e)
            return dict(success=False, message="Venv build failed",
                        error_message=str(e))
