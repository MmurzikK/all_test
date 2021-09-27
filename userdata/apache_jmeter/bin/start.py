import os
import shutil
import pathlib
import subprocess
import allure

@allure.title("Close choose sity")
@allure.description("WTF!&BRO!&")
class TestJenkins():
    def test_test(self):
        os.chdir("/apache_jmeter/bin/")
        os.chmod("jmeter.sh", 777)
        os.system("./jmeter.sh -n -t B.jmx")
        assert 1 == 1




