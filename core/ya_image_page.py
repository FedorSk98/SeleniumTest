from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from .base import BasePage

class ImageYandexPage(BasePage):
    def __init__(self):
        BasePage.__init__(self)
        self.__linkImage = list()

    def isLinkImage(self) -> bool:
        return "https://yandex.ru/images/?utm_source=main_stripe_big" in self.driver.page_source

    def clickImage(self) -> None:
        self.driver.find_element_by_link_text("Картинки").click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def atPage(self) -> bool:
        return "https://yandex.ru/images/?utm_source=main_stripe_big" == self.driver.current_url

    def openFirstCategory(self) -> bool:
        result = False
        link = self.driver.find_element_by_class_name("PopularRequestList-Item_pos_0").find_element_by_tag_name("a")
        url =  link.get_attribute("href")
        link.click()
        self.driver.implicitly_wait(2)
        search_text = self.driver.find_element_by_class_name("input__control").get_attribute("value")
        if url == self.driver.current_url and search_text == link.text:
            result = True
        return result

    def openFirstImageInCategory(self) -> bool:
        result: bool
        link = self.driver.find_element_by_class_name("serp-item_pos_0").find_element_by_tag_name("a")
        link.click()
        try:
            self.driver.find_element_by_class_name("Modal_visible")
        except:
            result = False
        else:
            result = True
        return result

    def transitionOfImageNext(self) -> bool:
        self.__linkImage.append(self.driver.find_element_by_class_name("MMImage-Origin").get_attribute("src"))
        self.driver.find_element_by_class_name("CircleButton_type_next").click()
        self.__linkImage.append(self.driver.find_element_by_class_name("MMImage-Origin").get_attribute("src"))
        return self.__linkImage[0] != self.__linkImage.pop()

    def transitionOfImageBack(self) -> bool:
        self.driver.find_element_by_class_name("CircleButton_type_prev").click()
        element = self.driver.find_element_by_class_name("MMImage-Origin").get_attribute("src")
        return self.__linkImage[0] == element