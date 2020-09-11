from django.test import TestCase


class TestTestCase(TestCase):

    def test_animals_can_speak(self):
        self.assertEqual('ok', 'ok')
