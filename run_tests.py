import subprocess


def tests():
    subprocess.run(["python", "-u", "-m", "pytest"])
