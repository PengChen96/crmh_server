
import os
import logging
from tools.utils.c_path import getProjectPath

class Logger():
    def __init__(self, logname, pyName):
        # 创建一个logger
        self.logger = logging.getLogger(pyName)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        savePath = os.path.join(getProjectPath(),"static","pDownload","log",logname)
        fh = logging.FileHandler(savePath,encoding='utf8')
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger
