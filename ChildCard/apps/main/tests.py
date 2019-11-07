from django.test import TestCase


class Temp_Test(TestCase):
    def setUp(self):
        self.value = 6

    def test(self):
        self.assertEqual(self.value, 6)
