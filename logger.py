import logging
 
# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
 
# Creating an object
log = logging.getLogger()
 
# Setting the threshold of logger to DEBUG
log.setLevel(logging.DEBUG)
 
