import sys
import logging
import time
from threading import Thread
from pvconf import PvConf
from pvrelay import PvRelay

# Logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)
logger.info("PyFusionSolarDataRelay 1.0.4 started")

# Config
conf = PvConf(logger)
if conf.debug:
    logger.debug("Enabled verbose logging")
    logger.setLevel(logging.DEBUG)
    conf.print()
else:
    logger.setLevel(logging.INFO)

# Start PvRelay and KenterRelay
try:
    if __name__ == '__main__':
        fs_thread = Thread(target = PvRelay, args=[conf, logger])
        fs_thread.daemon = True
        fs_thread.start()
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    logger.info("Ctrl C - Stopping relay")
    sys.exit(0)

