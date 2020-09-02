# aiohttpdemo_polls/settings.py
import pathlib
import yaml

config_path = "../config/polls.yaml"

def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    return config

config = get_config(config_path)