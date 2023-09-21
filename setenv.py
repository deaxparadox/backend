import os 
import subprocess
import sys
import argparse



REQUIREMENTS_DJANGO: str = "assets/requirements_django.txt"
REQUIREMENTS_FASTAPI: str = "assets/requirements_fastapi.txt"

def command_line_arguments() -> argparse.Namespace:
    """
    Create command line arguments
    """
    _description: str = ("Backend environment setup tool, "
                     "specify which framework environment you want"
                     "and it will create and you are good to go develop and learn."
                    )
    parser = argparse.ArgumentParser(
        description=_description
    )
    parser.add_argument("NAME", help="environment name")
    parser.add_argument("--django", action="store_true", help="set up environment for django")
    parser.add_argument("--fastapi", action="store_true", help="set up environment for fastapi")
    
    return parser.parse_args()


def _linux_command_run(args):
    print(args)
    return subprocess.run(
        args=(*args,),
        capture_output=True,
        # shell=True,
        # executable="/bin/bash"
    )

def linux_command_run(args, /, message: str|None = None) -> None:
    """
    Run linux command, and display input message
    """
    output = _linux_command_run(args)
    if output.returncode != 0:
        print(output.stderr.decode("utf-8"))
    else:
        print(message)
    return 

if __name__ == "__main__":

    # create environment 
    # activate environment
    # update pip
    # install packages

    # get command line arguments
    arguments = command_line_arguments()


    
    # output variable to store and reuse 
    output: None|bytes|str = None

    # 
    # create environment
    # 
    print("Settings up python environments")
    # 
    # environment command
    create_envrionment = f"python -m venv venv/{arguments.NAME}"
    # 
    # running environment command
    output = _linux_command_run(create_envrionment.split(" "))
    if output.returncode == 0:
        print("Environment created successfully", end=" ==> ")
        print(f"\nTo activate environment: source venv/{arguments.NAME}/bin/activate\n")
    else:
        print(output.stderr.decode("utf-8"))
            
    # 
    # COMMAND
    # 
    # activating environment command
    activating_environment = f"source venv/{arguments.NAME}/bin/activate"
    # 
    # update pip command
    update_pip = f"pip install --upgrade pip"
    # 
    # permission to activate environment
    # chmod_activate = f"chmod +x venv/{arguments.NAME}/bin/activate"
    # print("Changing permission to activate environment => ", end=" ==> ")
    # linux_command_run(chmod_activate.split(" "), "changed permission")

    # if arguments.django:
    #     # 
    #     # environment package file : requirements_django.txt
    #     package_install = f"pip install -r {REQUIREMENTS_DJANGO}"

    #     # 
    #     # activating environment
    #     print("Activating environment...", end=" ==> ")
    #     linux_command_run(activating_environment.split(" "), "environment activated")
    #     # 
    #     # update pip package
    #     print("Updating pip...", end=" ==> ")
    #     linux_command_run(update_pip.split(" "), "pip updated")
    #     # 
    #     # installing packages
    #     print("Installing package...", end=" ==> ")
    #     linux_command_run(package_install.split(" "), "packages installed")

    #     print(f"\nTo activate environment: source venv/{arguments.NAME}/bin/activate\n")
    

    # elif arguments.fastapi:
    #     # set up environments for fastapi
    #     pass
        