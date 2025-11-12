import yaml
import logging
import logging.config
import os
import io


def load_yaml(path: str):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def setup_logger():
    with io.open('config/logging.conf', 'r', encoding='utf-8') as f:
        logging.config.fileConfig(f)
    return logging.getLogger('appLogger')

def load_configs():
    config = load_yaml('config/config.yaml')
    db_conf = load_yaml('config/db_config.yaml')
    logger = setup_logger()
    return config, db_conf, logger
