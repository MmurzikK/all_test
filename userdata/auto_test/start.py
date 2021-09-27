import os
import shutil
import pathlib
import subprocess

os.chdir(pathlib.Path().parent)
shutil.rmtree("/result/UImanual", True)
subprocess.Popen(
    "python3 -m pytest -s /auto_test/test.py --alluredir /result/UImanual/regress", shell=True).wait()
subprocess.Popen("allure serve /result/UImanual/regress",
                 shell=True)
#subprocess.Popen(
#    "python -m pytest -s /api_test/tests/regress/test.py --alluredir /result/manual/regress", shell=True).wait()
#subprocess.Popen("allure serve /result/manual/regress",
#                 shell=True)

