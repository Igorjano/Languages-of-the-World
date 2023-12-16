from django.test import TestCase
from el_mundo.models import Languages


class TestLanguages(TestCase):
    def setUp(self):
        self.language = Languages.objects.create(name='Dari',
                                                 sign='prs')

    def test_adding_language(self):
        self.assertTrue(isinstance(self.language, Languages))
        db_language = Languages.objects.get(name='Dari')
        self.assertEquals(self.language, db_language)
        db_language_is_exists = Languages.objects.filter(name='Dari').exists()
        self.assertTrue(db_language_is_exists)

    def test_str(self):
        self.assertEquals(TestLanguages.__str__(self), 'TestLanguages')
