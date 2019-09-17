#!/usr/bin/env python
import re
import sys

from wagtail.bin.wagtail import UpdateModulePaths


class UpdateModulePathsFromWagtail1ToWagtail1To2(UpdateModulePaths):
    REPLACEMENTS = [
        (re.compile(r'\bwagtail\.wagtailcore\b'), 'wagtail1to2.core'),
        (re.compile(r'\bwagtail\.wagtailadmin\b'), 'wagtail1to2.admin'),
        (re.compile(r'\bwagtail\.wagtaildocs\b'), 'wagtail1to2.documents'),
        (re.compile(r'\bwagtail\.wagtailembeds\b'), 'wagtail1to2.embeds'),
        (re.compile(r'\bwagtail\.wagtailimages\b'), 'wagtail1to2.images'),
        (re.compile(r'\bwagtail\.wagtailsearch\b'), 'wagtail1to2.search'),
        (re.compile(r'\bwagtail\.wagtailsites\b'), 'wagtail1to2.sites'),
        (re.compile(r'\bwagtail\.wagtailsnippets\b'), 'wagtail1to2.snippets'),
        (re.compile(r'\bwagtail\.wagtailusers\b'), 'wagtail1to2.users'),
        (re.compile(r'\bwagtail\.wagtailforms\b'), 'wagtail1to2.contrib.forms'),
        (re.compile(r'\bwagtail\.wagtailredirects\b'), 'wagtail1to2.contrib.redirects'),
        (re.compile(r'\bwagtail\.contrib\.wagtailfrontendcache\b'), 'wagtail1to2.contrib.frontend_cache'),
        (re.compile(r'\bwagtail\.contrib\.wagtailroutablepage\b'), 'wagtail1to2.contrib.routable_page'),
        (re.compile(r'\bwagtail\.contrib\.wagtailsearchpromotions\b'), 'wagtail1to2.contrib.search_promotions'),
        (re.compile(r'\bwagtail\.contrib\.wagtailsitemaps\b'), 'wagtail1to2.contrib.sitemaps'),
        (re.compile(r'\bwagtail\.contrib\.wagtailstyleguide\b'), 'wagtail1to2.contrib.styleguide'),
        #(re.compile(r'\bwagtail\.(?:\b)'), 'wagtail1to2.'),
    ]


def main():
    # This is needed because Wagtail's UpdateModulePaths is invoked as a
    # subcommand of the wagtail command-line utility.
    sys.argv.insert(1, 'updatemodulepaths')

    UpdateModulePathsFromWagtail1ToWagtail1To2().execute(sys.argv)


if __name__ == "__main__":
    main()
