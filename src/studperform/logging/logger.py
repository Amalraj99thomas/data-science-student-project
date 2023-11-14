#To log errors and exceptions as .txt files.

import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

try:
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO,


    )
except Exception as e:
    print(f"Error occurred while initializing the logging module")

logger = logging.getLogger(__name__)
#Uncomment to check for errors if any:
 
# if __name__=="__main__":
#     logging.info("Logging has been initialized.")


##Furthur Improvement:

# #To address the errors immediately if any to improve performance.
# #Can also be used to work around a repitive error.
# logging.error()

# #To store less critical information
# logging.info()