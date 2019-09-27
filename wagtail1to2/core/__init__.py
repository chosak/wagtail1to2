import sys

from wagtail1to2._internal import AliasedModule, WAGTAIL2


_REAL_NAME = 'wagtail.core' if WAGTAIL2 else 'wagtail.wagtailcore'


sys.modules[__name__] = AliasedModule(sys.modules[__name__], _REAL_NAME)
