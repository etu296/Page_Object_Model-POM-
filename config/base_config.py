from pathlib import Path
from dotenv import load_dotenv
import os

class BaseConfig:
    BASE_DIR = Path(__file__).resolve().parent.parent
    SCREENSHOT_DIR = BASE_DIR / "reports" / "screenshots"
    LOGS_DIR = BASE_DIR / "logs"
    ENV_CONFIG_DIR = BASE_DIR / "config" / "environments"
    REPORT_DIR = BASE_DIR / "reports"
    ALLURE_RESULTS = BASE_DIR / "reports" / "allure_results"

    load_dotenv(dotenv_path=BASE_DIR / ".env")
    ENV = os.getenv("ENV")
    BROWSER = os.getenv("BROWSER", "chrome").lower()
    HEADLESS = os.getenv("HEADLESS", "True").lower() in ["true", "1", "yes"]


