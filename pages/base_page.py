from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    def click(self, locator):
        try:
            # element = self.wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR if not locator.startswith("//") else By.XPATH, locator))
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(e)

    def enter_text(self, locator, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)
            
        except Exception as e:
            print(e)


