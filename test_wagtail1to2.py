import importlib
import unittest

import wagtail


class TestWagtail1To2(unittest.TestCase):
    def test_import_wagtail1to2_module_itself(self):
        import wagtail1to2

    def test_import_module(self):
        import wagtail1to2.core

    def test_import_submodule(self):
        import wagtail1to2.contrib.frontend_cache

    def test_import_using_importlib(self):
        importlib.import_module('wagtail1to2.core')

    def test_import_submodule_using_importlib(self):
        importlib.import_module('wagtail1to2.contrib.frontend_cache')

    def test_import_from_module(self):
        from wagtail1to2.core import default_app_config
        self.assertIn('WagtailCoreAppConfig', default_app_config)

    def test_import_submodule(self):
        from wagtail1to2.embeds import exceptions

    def test_import_from_submodule(self):
        from wagtail1to2.embeds.exceptions import EmbedException

    def test_invalid_module_import_still_fails(self):
        with self.assertRaises(ImportError):
            from wagtail1to2 import not_in_wagtail

    def test_invalid_submodule_import_still_fails(self):
        with self.assertRaises(ImportError):
            from wagtail1to2.core import not_in_wagtail

    @unittest.skipIf(wagtail.VERSION[0] == 2, 'only applies to wagtail 1')
    def test_core_module_imports_properly_wagtail1(self):
        from wagtail1to2 import core
        self.assertEqual(core.__name__, 'wagtail.wagtailcore')

    @unittest.skipIf(wagtail.VERSION[0] == 1, 'only applies to wagtail 2')
    def test_core_module_imports_properly_wagtail2(self):
        from wagtail1to2 import core
        self.assertEqual(core.__name__, 'wagtail.core')

    def check_django_setup_and_model_import(self, expected_model_module):
        import django
        from django.conf import settings

        settings.configure(
            INSTALLED_APPS=(
                'django.contrib.auth',
                'django.contrib.contenttypes',
                'wagtail1to2.core',
                'wagtail1to2.contrib.frontend_cache',
            )
        )
        django.setup()

        from wagtail1to2.core.models import Page
        self.assertEqual(Page.__module__, expected_model_module)

    @unittest.skipIf(wagtail.VERSION[0] == 2, 'only applies to wagtail 1')
    def test_django_setup_and_model_import_wagtail1(self):
        self.check_django_setup_and_model_import('wagtail.wagtailcore.models')

    @unittest.skipIf(wagtail.VERSION[0] == 1, 'only applies to wagtail 2')
    def test_django_setup_and_model_import_wagtail1(self):
        self.check_django_setup_and_model_import('wagtail.core.models')


if __name__ == '__main__':
    unittest.main()
