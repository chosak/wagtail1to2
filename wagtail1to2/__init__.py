from pkgutil import extend_path

import wagtail

from ._internal import WAGTAIL2 as _WAGTAIL2


wagtail.__path__ = extend_path(wagtail.__path__, __name__)
del wagtail


if not _WAGTAIL2:
    from wagtail.wagtailcore.apps import WagtailCoreAppConfig
    WagtailCoreAppConfig.name = 'wagtail.core'
    del WagtailCoreAppConfig
