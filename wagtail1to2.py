import re
import sys

import wagtail


_WAGTAIL_PACKAGE = 'wagtail'


_WAGTAIL2 = wagtail.VERSION[0] == 2


_WAGTAIL_MOVES_1_TO_2 = [
    ('wagtail.contrib.wagtailfrontendcache', 'wagtail.contrib.frontend_cache'),
    ('wagtail.contrib.wagtailroutablepage', 'wagtail.contrib.routable_page'),
    ('wagtail.contrib.wagtailsearchpromotions', 'wagtail.contrib.search_promotions'),
    ('wagtail.contrib.wagtailsitemaps', 'wagtail.contrib.sitemaps'),
    ('wagtail.contrib.wagtailstyleguide', 'wagtail.contrib.styleguide'),
    ('wagtail.wagtailadmin', 'wagtail.admin'),
    ('wagtail.wagtailcore', 'wagtail.core'),
    ('wagtail.wagtaildocs', 'wagtail.documents'),
    ('wagtail.wagtailembeds', 'wagtail.embeds'),
    ('wagtail.wagtailforms', 'wagtail.contrib.forms'),
    ('wagtail.wagtailimages', 'wagtail.images'),
    ('wagtail.wagtailredirects', 'wagtail.contrib.redirects'),
    ('wagtail.wagtailsearch', 'wagtail.search'),
    ('wagtail.wagtailsites', 'wagtail.sites'),
    ('wagtail.wagtailsnippets', 'wagtail.snippets'),
    ('wagtail.wagtailusers', 'wagtail.users'),
]


class _WagtailImporter(object):
    """Combined Meta path finder and loader to handle Wagtail 1/2 imports.

    See https://docs.python.org/3/glossary.html#term-meta-path-finder and
    https://docs.python.org/3/glossary.html#term-loader.
    """
    def __init__(self, name, moves):
        self.name = name
        self.moves = dict(moves)

    def find_module(self, fullname, path):
        """Returns this object if a module is known, otherwise None."""
        if fullname.startswith(self.name + '.'):
            try:
                self._find_matching_move(fullname)
                return self
            except ImportError:
                pass

    def load_module(self, fullname):
        """Loads a module given its name."""
        try:
            return sys.modules[fullname]
        except KeyError:
            pass

        wagtail1_name, wagtail2_name = self._find_matching_move(fullname)
        wagtail_name = wagtail2_name if _WAGTAIL2 else wagtail1_name

        wagtail_module = self._import_module(wagtail_name)

        sys.modules[fullname] = wagtail_module

        return wagtail_module

    def _find_matching_move(self, fullname):
        wagtail_name = re.sub(
            r'^{}'.format(self.name),
            _WAGTAIL_PACKAGE,
            fullname
        )

        for wagtail1_name, wagtail2_name in self.moves.items():
            wagtail2_name_re = re.compile(r'^{}(\..*)?$'.format(wagtail2_name))
            match = wagtail2_name_re.search(wagtail_name)

            if match:
                remainder = match.group(1) or ''
                return wagtail1_name + remainder, wagtail2_name + remainder

        raise ImportError('unsupported module {}'.format(fullname))

    def _import_module(self, fullname):
        __import__(fullname)
        return sys.modules[fullname]


_importer = _WagtailImporter(__name__, _WAGTAIL_MOVES_1_TO_2)


__path__ = []
__package = __name__


if sys.meta_path:
    for i, importer in enumerate(sys.meta_path):
        if (
            type(importer).__name__ == '_WagtailImporter' and
            importer.__name__ == __name__
        ):
            del sys.meta_path[i]
            break

    del i, importer


sys.meta_path.append(_importer)
