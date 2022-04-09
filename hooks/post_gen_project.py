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


if "{{cookiecutter.sql}}" == "n":
    # remove models folder if not use sql database
    remove(f"{app_path}/models")

if "{{cookiecutter.mongo}}" == "n":
    # remove mongo models if not use mongodb
    remove(f"{app_path}/mongo_models")
