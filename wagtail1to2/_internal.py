from importlib import import_module

import wagtail


WAGTAIL2 = wagtail.VERSION[0] == 2


class AliasedModule(object):
    def __init__(self, real_module, aliased_module_name):
        self.real_module = real_module
        self.aliased_module_name = aliased_module_name

    def __getattr__(self, name):
        aliased_module = import_module(self.aliased_module_name)
        definition = getattr(aliased_module, name)

        # stash that definition into the current module so that we don't have to
        # redo this import next time we access it
        setattr(self.real_module, name, definition)

        return definition
