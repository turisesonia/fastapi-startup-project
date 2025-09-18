import os
import shutil

# /absolute/path/to/{{cookiecutter.project_slug}}
project_path = os.getcwd()
app_path = f"{project_path}/app"


def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


# copy .env from .env.example
shutil.copyfile(f"{project_path}/.env.example", f"{project_path}/.env")
