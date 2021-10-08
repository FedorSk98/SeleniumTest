import unittest


from core.ya_search_page import SearchYandexPage

class TestYandex(unittest.TestCase):
    def setUp(self) -> None:
        self.__driver = SearchYandexPage()

    def test_search_yandex(self):
        self.assertEqual(
            "https://yandex.ru/",
            self.__driver.openStartPage(),
            "Не удалось открыть сайт!"
        )

        self.assertTrue(
            self.__driver.is_input_search(),
            "Не найдена поисковая строка!"
        )

        self.__driver.inputTextSearch("Тензор")

        self.assertTrue(
            self.__driver.isSuggest(),
            "Не найдена таблица с подсказками!"
        )

        self.assertTrue(
            self.__driver.clickEnter(),
            "Не найдена таблица с резултатами поиска!"
        )

        self.assertTrue(
            self.__driver.isLinkSiteInSearch("tensor.ru"),
            "Не найдено ссылки на сайт в первых 5 результатах поиска!"
        )

    def tearDown(self) -> None:
        self.__driver.closeBrowser()

