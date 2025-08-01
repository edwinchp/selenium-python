from selenium.common import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open(self, url: str):
        self._driver.get(url)

    def _find(self, locator: tuple[str, str]) -> WebElement:
        return self._driver.find_element(*locator)

    def _type(self, locator: tuple[str, str], text: str, time: int = 30):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _click(self, locator: tuple[str, str], time: int = 30):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _wait_until_element_is_visible(self, locator: tuple[str, str], time: int = 30):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _get_text(self, locator: tuple[str, str], time: int = 30) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).text

    def _is_displayed(self, locator: tuple[str, str]) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False

    @property
    def current_url(self) -> str:
        return self._driver.current_url

