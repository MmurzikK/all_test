import os
import shutil
import pathlib
import subprocess

os.chdir(pathlib.Path(__file__).parent)
shutil.rmtree("/result/manual", True)
subprocess.Popen(
    "python -m pytest -s /api_test/tests/negative/test.py --alluredir /result/manual/negative", shell=True).wait()
subprocess.Popen("allure serve /result/manual/negative",
                 shell=True)
subprocess.Popen(
    "python -m pytest -s /api_test/tests/regress/test.py --alluredir /result/manual/regress", shell=True).wait()
subprocess.Popen("allure serve /result/manual/regress",
                 shell=True)
