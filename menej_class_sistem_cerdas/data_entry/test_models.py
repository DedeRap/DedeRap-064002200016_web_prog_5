from django.test import TestCase
from data_entry.models import Pengguna
"""
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to set up clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)
"""
class PenggunaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('SetupTestData dijalankan')
    Pengguna.objects.create(email='aku@gmail.com', password='pwdkurumit', \
                             address_1='kampus A Usakti, Grogol')
    
    def test_email_label(self):
        print('test email label dijalankan')
        pengguna = Pengguna.objects.get(id=1)
        field_label = pengguna._meta.get_field('email').verbose_name
        self.assertEqual(field_label, 'email')

    def test_password_max_length(self):
        print('test_password_max_length dijalankan')
        pengguna = Pengguna.objects.get(id=1)
        max_length = pengguna._meta.get_field('password').max_length
        self.assertEqual(max_length, 100)

    def test_object_name_is_email(self):
        print('test_object_name_is_email dijalankan')
        pengguna = Pengguna.objects.get(id=1)
        expected_object_name = f'{pengguna.email}'
        self.assertEqual(str(pengguna), expected_object_name)