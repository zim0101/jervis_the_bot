```
The tasks this tool will automate:
-----------------------------------
1. Create a new venv for your python project.
2. Create a python project inside the venv
3. Will init git in the project and create a README.md file
4. Commit the changes
5. Create a repository with the project name in github
6. Add remote origin in your local git directory

```

```
Purpose:
--------
I had to do all this every time I start a python project. 
I want my life to be more easier.

```

```
Future improvement:
-------------------
1. Same automated tasks for PHP Laravel projects
2. integrating Gitlab API as I have integrated only Github API.

```

```
Requirements:
-------------
1. python3
2. pip
3. venv
4. git
5. OS must be Linux. I have no place for windows in my
heart.

```

```
Project Tree:
-------------


.
├── build_project
│   ├── __init__.py
│   ├── project_builder.py
│   └── run.py
├── github
│   ├── __init__.py
│   ├── run.py
│   └── services.py
├── jervis
│   ├── __init__.py
│   └── jervis.py
├── README.md
├── requirements.txt
├── settings.py
├── .env
├── shell_scripts
│   ├── build_venv.sh
│   ├── github_push.sh
│   └── git_init.sh
└── utils
    ├── helpers.py
    ├── __init__.py

```

```
Installation:
--------------
1. lets make a new directory somewhere in your computer. You know, just to make 
things clean. Run:

$ mkdir python_projects && cd python_projects

2. Assure you have python3, pip and venv. There is tons of resource to install 
those. Go get your tigers

3. now run this command bellow to make a virtualenv for your project.

$ python3 -m venv jervis_bot_env

4. Activate your venv

$ . jervis_bot_env/bin/activate

5. Lets get into our venv 
 
$ cd jervis_bot_env

6. Clone the repo and Install all dependencies from our requirements.txt file

$ pip3 install -r requirements.txt

7. create .env file and set this variables:
GITHUB_ACCESS_TOKEN=< your github personal accerss token >
GITHUB_USERNAME=<your github username>

8. Run jervis.py file from jervis package.
```