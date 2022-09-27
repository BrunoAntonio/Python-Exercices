import pandas as pd
from datetime import datetime
import os
import logging

def get_data(url, logger):
    now = datetime.now()
    current_time = now.strftime("%Y-%m-%d %H:%M:%S")

    df = pd.read_json(url)
    df.insert(0, "extraction_id", current_time)
    
    if not os.path.isfile('data/data.csv'):
        df.to_csv('data/data.csv', header=True)
    else:
        df.to_csv('data/data.csv', mode='a', header=False)
        
    logger.info('extraction_id: %s|nº_of_added_rows: %i' % (current_time, df.shape[0]))

def logger():
    logger = logging.getLogger("data_extraction")
    logger.setLevel(logging.INFO)
    log_filename=os.path.join('log/log.log')
    handler=logging.FileHandler(log_filename,mode='a')
    handler.setFormatter(logging.Formatter("%(asctime)s|%(levelname)s|%(name)s|%(message)s"))
    logger.addHandler(handler)
    
    return logger
    
if __name__ == "__main__":
    url = "https://www.publico.pt/api/list/ultimas"
    logger = logger()
    get_data(url, logger)