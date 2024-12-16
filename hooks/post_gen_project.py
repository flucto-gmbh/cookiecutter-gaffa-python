import subprocess

if "{{cookiecutter.vcs}}":
    print("Initializing git repository...")
    subprocess.call(["git", "init"])
