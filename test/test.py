from main import Bot

import unittest
import json


class Test_Bot(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        token = input('Ключ бота')
        login = input('Мобильный телефон с привязкой к логину')
        password = input('пароль к логину')
        cls.user_id = input('id vk')
        cls.VKinder = Bot(token, login, password)

    @classmethod
    def tearDownClass(cls):
        pass

    def test_info_check_function(self):
        self.assertIsInstance(self.VKinder.check_data(self.user_id), bool)

    def test_search_function(self):
        self.assertIsInstance(self.VKinder.search_people(self.user_id), list)

    def test_json_file(self):
        self.VKinder.search_people(self.user_id)
        self.VKinder.pick(self.user_id)
        with open("test/created files/pairs.json", "r", encoding='UTF-8') as f:
            results = json.load(f)
        self.assertLessEqual(len(results), 10)
        if len(results) > 0:
            for result in results:
                self.assertIsNotNone(result.get('url'))
                self.assertIsNotNone(result.get('top1_photo'))


if __name__ == '__main__':
    unittest.main()
