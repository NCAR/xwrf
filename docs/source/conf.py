import datetime
import xwrf
import sphinx_autosummary_accessors

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'myst_nb',
    'sphinxext.opengraph',
    'sphinx_copybutton',
    'sphinxcontrib.autodoc_pydantic',
    'sphinx_autosummary_accessors',
    'sphinx_design',
]

# Autosummary pages will be generated by sphinx-autogen instead of sphinx-build
autosummary_generate = True

autodoc_typehints = 'description'
autodoc_typehints_description_target = 'documented'
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'private-members': True,
}

autodoc_member_order = 'groupwise'
autodoc_pydantic_model_show_json = True
autodoc_pydantic_settings_show_json = False

# Napoleon configurations

napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False

numpydoc_show_class_members = False
numpydoc_validation_checks = {'all'}


# MyST config
myst_enable_extensions = ['amsmath', 'colon_fence', 'deflist', 'html_image']
myst_url_schemes = ['http', 'https', 'mailto']

# sphinx-copybutton configurations
copybutton_prompt_text = r'>>> |\.\.\. |\$ |In \[\d*\]: | {2,5}\.\.\.: | {5,8}: '
copybutton_prompt_is_regexp = True

extlinks = {
    'issue': ('https://github.com/ncar-xdev/xwrf/issues/%s', 'GH#'),
    'pr': ('https://github.com/ncar-xdev/xwrf/pull/%s', 'GH#'),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates', sphinx_autosummary_accessors.templates_path]

# The master toctree document.
master_doc = 'index'

# General information about the project.
current_year = datetime.datetime.now().year
project = 'xWRF'
author = 'xWRF Developers'
copyright = f'2021-{current_year}, {author}'

# The short X.Y version.
version = xwrf.__version__.split('+')[0]
# The full version, including alpha/beta/rc tags.
release = xwrf.__version__


# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '**.ipynb_checkpoints', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'furo'
html_title = ''

html_context = {
    'github_user': 'ncar-xdev',
    'github_repo': 'xwrf',
    'github_version': 'main',
    'doc_path': 'docs',
}
html_static_path = ['_static']
html_theme_options = dict(
    # analytics_id=''  this is configured in rtfd.io
    # canonical_url="",
    light_logo='xwrf_logo_bg_light.svg',
    dark_logo='xwrf_logo_bg_dark.svg',
    sidebar_hide_name=True,
)
html_favicon = '_static/xwrf_favicon.ico'


# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'


# Output file base name for HTML help builder.
htmlhelp_basename = 'xwrfdoc'

# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    # 'papersize': 'letterpaper',
    # The font size ('10pt', '11pt' or '12pt').
    # 'pointsize': '10pt',
    # Additional stuff for the LaTeX preamble.
    # 'preamble': '',
}

latex_documents = [('index', 'xwrf.tex', 'xwrf Documentation', author, 'manual')]
man_pages = [('index', 'xwrf', 'xwrf Documentation', [author], 1)]
texinfo_documents = [
    (
        'index',
        'xwrf',
        'xwrf Documentation',
        author,
        'xwrf',
        'One line description of project.',
        'Miscellaneous',
    )
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'xarray': ('https://xarray.pydata.org/en/stable/', None),
    'metpy': ('https://unidata.github.io/MetPy/latest/', None),
    'xgcm': ('https://xgcm.readthedocs.io/en/latest/', None),
}
