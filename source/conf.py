# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'shpinx-test-version-ctrl'
copyright = '2024, kong'
author = 'kong'
release = 'v0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['chinese_search','sphinx.ext.mathjax','sphinx_sitemap', 'sphinx_multiversion']

templates_path = ['_templates']
exclude_patterns = []

language = 'zh-CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']


# version
templates_path = ['_templates']
html_sidebars = {
    '**': [
        'versioning.html',
    ],
}

# 指定哪个分支为 lastest 版本
smv_latest_version = 'master'
