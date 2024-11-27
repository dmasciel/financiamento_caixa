from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Tempo padrão para espera

    def wait_for_element(self, by, locator):
        return self.wait.until(EC.presence_of_element_located((by, locator)))

    def wait_and_click(self, by, locator):
        element = self.wait_for_element(by, locator)
        self.wait.until(EC.element_to_be_clickable((by, locator)))
        element.click()
        return element

    def input_text(self, by, locator, text):
        element = self.wait_for_element(by, locator)
        element.clear()
        element.send_keys(text)
        return element
