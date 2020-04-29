import os
import subprocess


def build_venv():
    venv_name = "xyz"
    project_name = "x"
    root_dir = os.path.dirname(os.path.realpath(__file__)).rsplit(os.sep, 1)[0]
    print(root_dir)
    shell_script = os.path.join(root_dir, "build_venv.sh")
    print(shell_script)
    output = subprocess.check_output(
        [shell_script, str(venv_name), str(project_name)])
    print(output)


if __name__ == '__main__':
    build_venv()
