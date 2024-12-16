import subprocess

if "{{cookiecutter.vcs}}" == "True":
    print("Initializing git repository...")
    subprocess.call(["git", "init"])
