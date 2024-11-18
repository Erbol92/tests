
from main import check_email, list_of_numbers, reverse
import unittest
from config import ya_token
import requests


class TestCheckEmail(unittest.TestCase):
    def test_1(self):
        self.assertEqual(check_email('mail@mail.ru'), True)

    def test_2(self):
        self.assertEqual(check_email('@'), False)

    def test_3(self):
        self.assertEqual(check_email('m@'), False)


class TestListNumbers(unittest.TestCase):
    def test_range_1(self):
        self.assertListEqual(list_of_numbers(1), [1])

    def test_range_5(self):
        self.assertListEqual(list_of_numbers(5), [1, 2, 3, 4, 5])

    def test_range_3(self):
        self.assertListEqual(list_of_numbers(3), [1, 2, 3])


class TestReverse(unittest.TestCase):
    def test_1(self):
        self.assertEqual(reverse('lool pop mmm'), 'mmm pop lool')

    def test_2(self):
        self.assertEqual(reverse('aBc'), 'cba')

    def test_3(self):
        self.assertEqual(reverse('asdasdasd'), 'dsadsadsa')


class TestYA(unittest.TestCase):

    BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
    TOKEN = ya_token

    def setUp(self):
        self.headers = {
            "Authorization": self.TOKEN
        }
        self.folder_name = "test_folder"

    def tearDown(self):
        # Удаляем папку после тестов, если она была создана
        url = f"{self.BASE_URL}?path={self.folder_name}"
        requests.delete(url, headers=self.headers)

    def test_create_folder_success(self):
        url = f"{self.BASE_URL}?path={self.folder_name}"
        response = requests.put(url, headers=self.headers)
        # Ожидаем код 201 для успешного создания
        self.assertEqual(response.status_code, 201)

    def test_create_folder_already_exists(self):
        url = f"{self.BASE_URL}?path={self.folder_name}"
        response = requests.put(url, headers=self.headers)
        # Пытаемся создать папку с тем же именем
        response = requests.put(url, headers=self.headers)
        # Ожидаем код 409, если папка уже существует
        self.assertEqual(response.status_code, 409)

    def test_create_folder_invalid_path(self):
        invalid_folder_name = "invalid/folder/name"
        url = f"{self.BASE_URL}?path={invalid_folder_name}"
        response = requests.put(url, headers=self.headers)
        # Ожидаем код 409 для неверного пути
        self.assertEqual(response.status_code, 409)


if __name__ == '__main__':
    unittest.main()
