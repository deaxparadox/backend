import os

match int(os.environ.get("DOCKER", '0')):
    case 1:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_dj.settings.docker')
        print("\n#################### DOCKER ###########################\n")
    case _: 
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend_dj.settings.local')
