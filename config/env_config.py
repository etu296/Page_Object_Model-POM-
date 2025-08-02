from pathlib import Path
import yaml
from dotenv import load_dotenv
import os

def get_env_config():
    load_dotenv()
    env = os.getenv("ENV", ".env")
    config_path = Path(__file__).resolve().parent / "environments" / f"{env}.yaml"
    with open(config_path, "r") as file:
        return yaml.safe_load(file)