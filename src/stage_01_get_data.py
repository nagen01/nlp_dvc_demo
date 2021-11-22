import logging
import os
from typing_extensions import Required
from src.utils.all_utils import read_yaml, create_directories
import argparse
import urllib.request as req

logs_dir = "logs"
os.makedirs(logs_dir, exist_ok=True)
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
logging.basicConfig(
    filename=os.path.join(logs_dir, "running_logs.log"), 
    level=logging.INFO, 
    format=logging_str,
    filemode="a")

stage = "stage_01_get_data"

def get_data(config_path):
    config = read_yaml(config_path)
    #print(config)
    source_data_url = config["source_data_url"]
    source_download = config["source_download"]
    source_download_dir = source_download["data_dir"]
    create_directories([source_download_dir])
    source_download_filepath = os.path.join(source_download_dir, source_download["data_xml"])

    logging.info(f"Download started")
    filename, headers = req.urlretrieve(source_data_url, source_download_filepath)
    logging.info("Download completed")
    logging.info(f"Download file is present at {filename}")
    logging.info(f"Download headers at \n{headers}")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="config/config.yaml")

    parsed_args = args.parse_args()

    try:
        logging.info(f">>>>>Stage {stage} started")
        get_data(config_path=parsed_args.config)
        logging.info(f"Stage {stage} completed, data is loaded and saved >>>>>")
    except Exception as e:
        logging.exception(e)
        raise e