from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from .base import BasePage

class SearchYandexPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        self.__searchLocatorID = "text"
        self.__suggestClassName = "mini-suggest__popup_visible"
        self.__searchResultID = "search-result"

    def is_input_search(self) -> bool:
        result: bool
        try:
            self.driver.find_element_by_id(self.__searchLocatorID)
        except NoSuchElementException:
            result = False
        else:
            result = True
        return result

    def inputTextSearch(self, text: str):
        self.driver.find_element_by_id(self.__searchLocatorID).send_keys(text)

    def isSuggest(self) -> bool:
        result: bool
        try:
            self.driver.implicitly_wait(1)
            self.driver.find_element_by_class_name(self.__suggestClassName)
        except NoSuchElementException:
            result = False
        else:
            result = True
        return result

    def clickEnter(self) -> bool:
        result: bool
        try:
            self.driver.find_element_by_id(self.__searchLocatorID).send_keys(Keys.ENTER)
            self.driver.implicitly_wait(2)
            self.driver.find_element_by_id(self.__searchResultID)
        except NoSuchElementException:
            result = False
        else:
            result = True
        return result

    def isLinkSiteInSearch(self, url_site: str) -> bool:
        result = False
        elements = self.driver.find_elements_by_class_name("serp-item")
        for temp_element in elements[:5]:
           link_elements = temp_element.find_elements_by_tag_name("a")
           for link in link_elements:
               url = str(link.get_attribute("href"))
               if url.find(url_site) != -1:
                   result = True
        return result