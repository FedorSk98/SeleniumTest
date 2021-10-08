import unittest

from core.ya_image_page import ImageYandexPage

class TestImageYandex(unittest.TestCase):
    def setUp(self) -> None:
        self.__driver = ImageYandexPage()


    def test_image_yandex(self):
        self.assertEqual(
            "https://yandex.ru/",
            self.__driver.openStartPage(),
            "Не удалось открыть сайт!"
        )

        self.assertTrue(
            self.__driver.isLinkImage(),
            "Не найдено ссылки на 'Картинки'"
        )

        self.__driver.clickImage()

        self.assertTrue(
            self.__driver.atPage(),
            "Адрес открытой страницы неверный!"
        )

        self.assertTrue(
            self.__driver.openFirstCategory(),
            "В поиске указан не верный текст!"
        )

        self.assertTrue(
            self.__driver.openFirstImageInCategory(),
            "Невозможно открыть картинку"
        )

        self.assertTrue(
            self.__driver.transitionOfImageNext(),
            "Ошибка! Изображение не изменилось"
        )
        self.assertTrue(
            self.__driver.transitionOfImageBack(),
            "Ошибка! Открыто не то изображение"
        )

    def tearDown(self) -> None:
        self.__driver.closeBrowser()

if __name__ =="__main__":
    unittest.main()