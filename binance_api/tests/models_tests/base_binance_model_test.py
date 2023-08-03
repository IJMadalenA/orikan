from unittest import TestCase
from django.core.exceptions import ObjectDoesNotExist


class BaseModelTestCase(TestCase):
    factory = None
    model = None

    def test_model_creation(self):
        model = self.factory.create()

        self.assertTrue(isinstance(model, self.model))
        self.assertTrue(model.pk)

    def test_model_equality(self):
        model1 = self.factory.create()
        model2 = self.factory.create()

        self.assertNotEqual(model1, model2)
        self.assertEqual(model1, model1)

    def test_model_delete_operation(self):
        model = self.factory.create()

        # Delete
        model.delete()

        # Verify that the model is deleted
        with self.assertRaises(ObjectDoesNotExist):
            self.model.objects.get(pk=model.pk)

    def test_model_hash(self):
        model = self.factory.create()

        self.assertEqual(hash(model), hash(model.pk))

    def test_model_relationships(self):
        if hasattr(self.model, "related_models"):
            related_models = self.model.related_models

            for related_model_name, related_factory in related_models.items():
                related_model = related_factory._meta.model
                related_instance = related_factory.create()

                model = self.factory.create(**{related_model_name: related_instance})
                self.assertEqual(getattr(model, related_model_name), related_instance)

                related_instance.delete()

    def _create_model_instance(self):
        """Crea y guarda una instancia del modelo."""
        model = self.model()
        model.save()
        return model

    def test_model_constraints(self):
        if hasattr(self.model, "constraint_fields"):
            constraint_fields = self.model.constraint_fields

            for field_name, constraint_values in constraint_fields.items():
                for constraint_value in constraint_values:
                    with self.assertRaises(Exception):
                        self.factory.create(**{field_name: constraint_value})
