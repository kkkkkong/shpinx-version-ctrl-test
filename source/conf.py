# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme

project = 'shpinx-test-version-ctrl'
copyright = '2024, kong'
author = 'kong'
release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# extensions = ['chinese_search','sphinx.ext.mathjax','sphinx_sitemap', 'sphinx_multiversion']
extensions = [ 'sphinx_multiversion']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'

# html_static_path = ['_static']
html_static_path = [sphinx_rtd_theme.get_html_theme_path()]


# version
templates_path = ['_templates']
html_sidebars = {
    '**': [
        'versions.html',
    ],
}

# 指定哪个分支为 lastest 版本
smv_latest_version = 'main'
