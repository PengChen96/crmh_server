
__author__ = "pc"

import os
from config import PROJECTNAME

# 获取工程路径
def getProjectPath(projectName=PROJECTNAME):
    path = os.getcwd()
    # print(path)
    p_list = path.split(projectName,1)
    # print(p_list)
    projectPath = os.path.join(p_list[0],projectName)
    return projectPath
