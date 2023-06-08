# Imported from Django:
from django.test import TestCase


class BaseFactoryTestCase(TestCase):
    factory = None
    model = None

    def test_factory_creation(self):
        model = self.factory()

        self.assertTrue(model.pk)
        self.assertTrue(self.factory._meta.model.objects.get(pk=model.pk))

    def test_factory_count(self):
        model_count_before = self.factory._meta.model.objects.count()

        self.factory.create_batch(5)

        model_count_after = self.factory._meta.model.objects.count()
        self.assertEqual(model_count_after, model_count_before + 5)
