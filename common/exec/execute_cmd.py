import subprocess
import platform
class execute_cmd(object):
    def __init__(self):
        ostype = platform.system()
        if ostype == "Windows":
            self.shell = True
            self.encoding = "gbk"
        else:
            self.shell = False
            self.encoding = "utf8"

    def execute(self,cmd):
        pass



