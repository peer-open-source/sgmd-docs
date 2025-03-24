#!/usr/bin/env python3
import os
import sys
from pathlib import Path
# import sphinx_rtd_theme
#sys.path.append(os.path.abspath('./sphinx_ext/'))

#
# -- Project information -----------------------------------------------------
#
project = "SGMD"
copyright = 'Berkeley, CA'
description = "Simulated Ground Motion Database"
author = "PEER"
#html_logo = "_static/images/xara.png"
html_title = "SGMD"
html_short_title = "SGMD"

root_doc = "launch" #"user/index"
html_additional_pages = {'index': 'home.html'}
html_extra_path = ["robots.txt"]

rst_prolog = """
.. |BRACE2| replace:: `BRACE2`_
.. _BRACE2: https://structures.live
.. |cmp| replace:: `Claudio M. Perez`_
.. _Claudio M. Perez: https://stairlab.berkeley.edu/people/claudioperez

"""

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
#   'toctree_filter',
    'myst_parser',
    'sphinx.ext.mathjax',
    'sphinx_copybutton',
    'sphinx_tabs.tabs',
    "sphinxcontrib.bibtex",
    "sphinx.ext.autosummary",
    'sphinxcontrib.bibtex',
    'sphinx_sitemap'
]
myst_enable_extensions = [
    "amsmath",
    "attrs_inline",
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
]
bibtex_bibfiles = ["references.bib"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
html_static_path = ['_static']

exclude_patterns = [
    "_build", "Thumbs.db", ".DS_Store", "**/hidden",
]

# -- Options for HTML output -------------------------------------------------

html_baseurl       = "https://sgmd.peer.berkeley.edu"
sitemap_url_scheme = "{link}"

html_theme = "sphinx_book_theme" #"pydata_sphinx_theme" #"sphinx_rtd_theme"
html_show_sphinx = False
html_show_sourcelink = False

if True:
    html_theme_options = {
    #   'analytics_id': 'UA-2431545-1',
    #   "body_max_width": None,
        "show_prev_next": False,
        "logo": {
#         "image_light": html_logo,
#         "image_dark": "_static/logo-dark.png",
          "link": html_baseurl, # "index.html",
          "text": f'<span class="lead display-3">{project}</span>',
#         "alt_text": "xara docs - Home",
        }
    }

if "book" in html_theme:
    html_theme_options.update({
        "use_download_button":  False,
        "use_edit_page_button": False,
        "article_header_start": ["toggle-primary-sidebar.html", "breadcrumbs"]
    })

html_context = {
    "html_baseurl": html_baseurl,
    "root_doc": root_doc,
    "description": description,
    "github_user": "peer-open-source",
#   "github_repo": "OpenSeesRT",
#   "doc_path": "<path-from-root-to-your-docs>",

    # HOME
    "examples": [],
    "features": [
        {"title": "Fast", "body": "Core components have been refactored to leverage modern C++ features, which has furnished substantial performance improvements over the alternative serial OpenSees interpreters."},
        {"title": "Free", "body": "All source code contributed to xara is licensed under a <em>pure</em> BSD."},
        {"title": "Robust", "body": '<em>xara</em> is designed from the ground up for use in production environments like <a href="https://structures.live">structures.live</a>'},
    ],
    "home_image": "_static/images/CableStayed02.png"
}

#  'style_nav_header_background': '#F2F2F2' #64B5F6 #607D8B,

html_css_files = [
    'css/custom.css'
] + [
    'css/home-css/'+str(file.name) for file in (Path(__file__).parents[0]/"_static/css/home-css/").glob("vars*.css")
] + [
     'css/css/'+str(file.name) for file in (Path(__file__).parents[0]/"_static/css/css/").glob("*.css")
] + [
    "css/veux.css",
]

html_secnum_suffix = " "

