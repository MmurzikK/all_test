import os
import shutil
import pathlib
import subprocess

os.chdir(pathlib.Path(__file__).parent)
subprocess.Popen(
    "pwd", shell=True).wait()
subprocess.Popen(
    "docker-compose up -d --build ", shell=True).wait()
subprocess.Popen(
    "./cm selenoid start --vnc", shell=True).wait()
subprocess.Popen(
    "./cm selenoid-ui start -p 8090", shell=True).wait()    
subprocess.Popen(
    "docker pull selenoid/vnc:chrome_92.0", shell=True).wait()
subprocess.Popen(
    "docker pull selenoid/vnc:firefox_92.0", shell=True).wait()    


