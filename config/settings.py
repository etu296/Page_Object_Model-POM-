from config.env_config import get_env_config

env_config = get_env_config()
BASE_URL = env_config.get("base_url")