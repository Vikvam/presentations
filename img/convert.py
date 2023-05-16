import os
import subprocess


if __name__ == "__main__":
    files = filter(lambda file: True, os.listdir())
    for file in files:
        command = f"convert {file} -transparent white {file}"
        name, extension = os.path.splitext(os.path.basename(file))
        if extension == ".png":
            continue
            print(name, extension)
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            print(result.stdout)
        else:
            print(name, extension)