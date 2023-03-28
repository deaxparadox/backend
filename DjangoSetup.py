import os 
import sys 
import argparse
from argparse import Namespace
import typing 
import multiprocessing
from contextlib import contextmanager
import subprocess
from subprocess import CompletedProcess



def path(req: str):
    ...

def argument() -> Namespace:
    args = argparse.ArgumentParser(description="Django Project setup application")
    args.add_argument(
        "NAME", help="<NAME> of the project folder, It will not be used as default project directory. Project name will be backend",
    )
    args.add_argument(
        "-r", "--requirements", help="Specify the requirement.txt file", default=""
    )
    return args.parse_args() 

class attach:
    pass 


def create_folder(dir: str) -> bool:
    """
    This is the default step, creating folder
    """
    os.mkdir(dir)
    print("Creating Project folder")
    return True

def create_env(name: set) -> bool:
    os.chdir(name)
    print(os.getcwd())
    env: CompletedProcess = subprocess.run(['python', '-m', 'venv', f"venv/{name}"])
    return True if env.returncode == 0 else False


def complete_it(name) -> bool:
    bash = subprocess.run(['bash', '../django_setup.sh', name])
    return True

def steps():
    name: str = getattr(attach, "name")

    # create folder
    create_folder(name)
    
    # create env
    create_env(name)

    complete_it(name)


@contextmanager
def run(arg: Namespace) -> None:
    try:
        setattr(attach, "name", arg.NAME)
        if arg.requirements:
            setattr(attach, "requirements", arg.requirements)            
        steps()
        yield
    finally:
        print("Closing run")


def main() -> None:
    arg = argument()
    with run(arg) as r:
        print(r)


if __name__ == "__main__":
    main()