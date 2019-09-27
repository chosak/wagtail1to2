import importlib
import unittest


class TestWagtail1To2(unittest.TestCase):
    def test_import_wagtail_module_itself(self):
        import wagtail

    def test_import_module(self):
        import wagtail.core

    def test_import_module_using_importlib(self):
        importlib.import_module('wagtail.core')

    def test_import_submodule(self):
        import wagtail.contrib.frontend_cache

    def test_import_submodule_using_importlib(self):
        importlib.import_module('wagtail.contrib.frontend_cache')

    def test_import_from_module(self):
        from wagtail.core import default_app_config
        self.assertIn('WagtailCoreAppConfig', default_app_config)

    def test_import_from_submodule(self):
        from wagtail.embeds.exceptions import EmbedException

    def test_invalid_module_import_still_fails(self):
        with self.assertRaises(ImportError):
            from wagtail import not_in_wagtail

    def test_invalid_submodule_import_still_fails(self):
        with self.assertRaises(ImportError):
            from wagtail.core import not_in_wagtail

    def test_django_setup_and_model_import(self):
        import django
        from django.conf import settings

        import wagtail1to2

        settings.configure(
            INSTALLED_APPS=(
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'wagtail.core',
            )
        )
        django.setup()

        from wagtail.core.models import Page
        self.assertEqual(Page.__module__, 'wagtail.core.models')


if __name__ == '__main__':
    unittest.main()
