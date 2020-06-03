import os


def MakeDir(dir_name: str) -> str:
    if not os.path.isdir(os.getcwd() + "/" + dir_name):
        os.makedirs(os.getcwd() + "/" + dir_name)
    os.chdir(os.getcwd() + "/" + dir_name)

    return os.getcwd()
