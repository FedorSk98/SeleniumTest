import os

from selenium import webdriver
from selenium.common.exceptions import WebDriverException


class BasePage:
    def __init__(self):
        self.__driver = webdriver.Chrome(
         executable_path=os.getcwd()+'\\resources\\chromedriver.exe'
        )

    @property
    def driver(self):
        return self.__driver

    def openStartPage(self) -> str:
        result: str
        try:
            self.__driver.get("https://yandex.ru/")
        except WebDriverException as e:
            result = e.msg
        else:
            result = self.__driver.current_url
        return result

    def closeBrowser(self):
        self.__driver.close()