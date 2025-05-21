import os
import sys


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'F-Code AI Crew Training'
copyright = '2025, F-Code AI Crew'
author = 'F-Code AI Crew'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx_design',
    'sphinx_copybutton',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_logo = '_static/images/fcode.svg'
html_favicon = '_static/images/fcode.svg'
html_css_files = ["stylesheets/style.css"]
html_theme_options = {
    "logo": {
        "image_light": "_static/images/fcode.svg",
        "image_dark": "_static/images/fcode.svg",
        "text": "F-Code AI Crew",
        "alt_text": "F-Code Logo",
    },
    "navbar_start": ["navbar-logo"],
    "icon_links": [
        {
            "name": "F-Code AI GitHub",
            "url": "https://github.com/F-Code-AI-Crew",
            "icon": "fa-brands fa-github",
        },
        {
            "name": "F-Code Facebook",
            "url": "https://www.facebook.com/fcodeclub",
            "icon": "fa-brands fa-facebook",
        },
    ],
    "icon_links_label": "Quick Links",
    "use_edit_page_button": False,
}
html_show_sourcelink = False


pygments_style = "friendly"  # Try also "friendly", "monokai", etc.


# Add more path here to import scripts
sys.path.insert(0, os.path.abspath('./python_docs/day_01/scripts'))
# sys.path.insert(0, os.path.abspath('./python_docs/day_02/scripts'))
