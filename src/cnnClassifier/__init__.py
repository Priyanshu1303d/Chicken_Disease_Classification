

# we are making logging here because we want the importing
# to be shorthand i.e we will go directly by ---> from src.logging import logging  <----
# or instead we can make a folder inside folder CnnClassifier named logging and initialise it so that
# it enables us to import it in diff files and it will be -----> from src.CnnClassifier.logging import logging <------


import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s : %(message)s]"

log_dir = "logs"    #name of the folder where we wil store the logs
log_filepath = os.path.join(log_dir, "running_logs.log") #will join these path log_dir/running_logs.log
os.makedirs(log_dir , exist_ok=True)
# checks if the dir is present or not.. if not then make a new dir

logging.basicConfig(  #Do basic configuration for the logging system.
    level=logging.INFO,
    format = logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #Open the specified file and use it as the stream for logging.
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("cnnClassifierLogger")
# we will use this logger whenever we want to import it across files
#Return a logger with the specified name, creating it if necessary.
#If no name is specified, return the root logger.
