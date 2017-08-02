
from tools.log.logger import Logger
# 日志  DEBUG < INFO < WARNING < ERROR < CRITICAL
logger = Logger(logname='info.log', pyName="ubitTest.py").getlog()

logger.debug("测试logTest")
logger.info("测试logTest")
logger.warning("测试logTest")
logger.error("测试logTest")
logger.critical("测试logTest")