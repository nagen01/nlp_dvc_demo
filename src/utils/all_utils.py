import yaml
import logging
import os

def read_yaml(path_to_yaml:str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"Yaml file loaded successfully from {path_to_yaml}")
    return content

def create_directories(path_to_direcotries:list) -> None:
    for path in path_to_direcotries:
        os.makedirs(path, exist_ok=True)
        logging.info(f"Directory created at {path}")