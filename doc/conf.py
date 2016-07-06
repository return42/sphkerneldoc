# -*- coding: utf-8 -*-
#
# This is the common sphinx-build configuration used by the kernel documentation
# book's build process. About config values consult:
#
# * http://www.sphinx-doc.org/en/stable/config.html
#
# Project (book) specific configuration is read from a file given by the
# SPHPROJ_CONF environment (see function loadPrjConfig).

import sys
import os
from os.path import join as pathjoin
from os.path import abspath, dirname, splitext, basename, exists

sys.setrecursionlimit(2000)

BASE_FOLDER = []
for folder in dirname(__file__).split(os.sep):
    if folder == "cache":
        BASE_FOLDER.append("doc")
        break
    BASE_FOLDER.append(folder)
BASE_FOLDER = os.sep.join(BASE_FOLDER)

# ------------------------------------------------------------------------------
# General information about the project.
# ------------------------------------------------------------------------------

project   = 'The Linux Kernel'
copyright = '2016, The kernel development community'
author    = 'The kernel development community'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# version   = 'v4.7'
# The full version, including alpha/beta/rc tags.
# release   = 'v4.7-rc2'

# ------------------------------------------------------------------------------
def loadPrjConfig():
# ------------------------------------------------------------------------------

    from sphinx.util.pycompat import execfile_
    from sphinx.util.osutil import cd

    config_file = os.environ.get("SPHPROJ_CONF", None)
    if config_file is not None and exists(config_file):
        config_file = abspath(config_file)
        main_name   = splitext(basename(config_file))[0]
        config = globals().copy()
        config.update({
            "main_name" : main_name
        })
        config['__file__'] = config_file
        execfile_(config_file, config)
        globals().update(config)

# ------------------------------------------------------------------------------
# extensions
# ------------------------------------------------------------------------------

# only for debugging:
sys.path.append(abspath(pathjoin(BASE_FOLDER, "..", 'scripts')))
import common  # to get the SDK debugger/console

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here.

#sys.path.insert(0, pathjoin(BASE_FOLDER, 'extensions'))

# ------------------------------------------------------------------------------
# General configuration
# ------------------------------------------------------------------------------

# The default language to highlight source code in.
highlight_language = "none"

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# external links
# --------------
#
# usage:  lorem :man:`dvbv5-scan` ipsum

extlinks = {
    'man'         : ('http://manpages.ubuntu.com/cgi-bin/search.py?q=%s', ' ')
    , 'deb'       : ('http://packages.ubuntu.com/xenial/%s', ' ')
    }

# Intersphinx
# -----------
#
# usage:  lorem :ref:`dtv_get_frontend <linux:dtv_get_frontend>` ipsum

intersphinx_mapping = {}
intersphinx_mapping['linux'] = ('https://return42.github.io/sphkerneldoc/linux_src_doc/', None)
intersphinx_mapping['kernel-doc'] = ('https://return42.github.io/sphkerneldoc/books/kernel-doc-HOWTO/', None)
intersphinx_mapping['template-book'] = ('http://return42.github.io/sphkerneldoc/books/template-book/', None)

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "linuxdoc.rstFlatTable"    # flat-table reST directive
    , "linuxdoc.rstKernelDoc"  # kernel-doc reST directive
    , "linuxdoc.manKernelDoc"  # kernel-doc-man sphinx builder
    # , "xelatex"
    , 'sphinx.ext.autodoc'
    , 'sphinx.ext.extlinks'
    #, 'sphinx.ext.autosummary'
    #, 'sphinx.ext.doctest'
    , 'sphinx.ext.todo'
    , 'sphinx.ext.coverage'
    #, 'sphinx.ext.pngmath'
    #, 'sphinx.ext.mathjax'
    , 'sphinx.ext.viewcode'
    , 'sphinx.ext.intersphinx'
    , 'sphinx.ext.ifconfig'
]

# Gracefully handle missing rst2pdf.
try:
    import rst2pdf
    extensions += ['rst2pdf.pdfbuilder']
except ImportError:
    pass

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '_tex', 'sphinx-static']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True

# ------------------------------------------------------------------------------
# Options of the kernel-doc parser
# ------------------------------------------------------------------------------

# If true, fatal errors (like missing function descripions) raise an
# error. Default: True
kernel_doc_raise_error = False

# If true, more warnings will be logged. E.g. a missing description of a
# function's return value will be logged.
# Default: True
kernel_doc_verbose_warn = False

# Set parser's default kernel-doc mode ``reST|kernel-doc``.
# Default: "reST"
kernel_doc_mode = "reST"

# ------------------------------------------------------------------------------
# Options for HTML output
# ------------------------------------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = pathjoin(BASE_FOLDER, "_tex", "logo.png")

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['sphinx-static']

html_context = {
    'css_files': [
        '_static/theme_overrides.css',
    ],
}

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'hu', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'ru', 'sv', 'tr'
html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# Now only 'ja' uses this config value
#html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Kernel-Doc'

# ------------------------------------------------------------------------------
# Options for LaTeX output
# ------------------------------------------------------------------------------

# Additional stuff for the LaTeX preamble.

latex_preamble = r"""

\usepackage{darmarITCI}

%%\setmainfont{DejaVu Serif}
%%\setsansfont{DejaVu Sans}
\setmonofont[Scale=0.7]{DejaVu Sans Mono}

"""

# see HEADER in https://github.com/sphinx-doc/sphinx/blob/master/sphinx/writers/latex.py#L34
latex_elements = dict()
latex_elements.update({

    'preamble' : latex_preamble

    , 'papersize'  : 'a4paper'  # The paper size ('letter' or 'a4').
    , 'pointsize'  : '12pt'     # The font size ('10pt', '11pt' or '12pt').

    , 'extraclassoptions'    : ''
    , 'passoptionstopackages': ''


    # some packages are obsolete other changed with xelatex
    , 'inputenc'   : r''
    , 'utf8extra'  : r''
    , 'cmappkg'    : r''
    , 'fontenc'    : r'\usepackage{fontspec}'     # http://ctan.org/pkg/fontspec
    , 'babel'      : r'\usepackage{polyglossia}'  # http://ctan.org/pkg/polyglossia

    , 'amsmath'        : r'\usepackage{amsmath,amssymb}'
    , 'fontpkg'        : r'\usepackage{times}'
    , 'fncychap'       : r'' # r'\usepackage[Sunny]{fncychap}'
    , 'longtable'      : r'\usepackage{longtable}'
    , 'usepackages'    : r''
    , 'numfig_format'  : r''
    , 'contentsname'   : r''
    , 'title'          : r''
    , 'date'           : r''
    , 'release'        : r''
    , 'author'         : r''
    , 'logo'           : r''
    , 'releasename'    : r'Release'
    , 'makeindex'      : r'\makeindex'
    , 'shorthandoff'   : r''
    , 'maketitle'      : r'\maketitle'
    , 'tableofcontents': r'\tableofcontents'
    , 'footer'         : r''
    , 'printindex'     : r'\printindex'
    , 'transition'     : '\n\n\\bigskip\\hrule{}\\bigskip\n\n'
    , 'figure_align'   : r'htbp'
    , 'tocdepth'       : r''
    , 'pageautorefname': r''

    })


# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = pathjoin(BASE_FOLDER, "_tex", "logo.png")

latex_additional_files = [
    pathjoin(BASE_FOLDER,   "_tex", "Makefile")
    , pathjoin(BASE_FOLDER, "_tex", "darmarITCI.sty")
    , pathjoin(BASE_FOLDER, "_tex", "darmarITArticle.cls")
    , pathjoin(BASE_FOLDER, "_tex", "icon_left.png")
    , pathjoin(BASE_FOLDER, "_tex", "icon_right.png")
]

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# ------------------------------------------------------------------------------
# Options for manual page output
# ------------------------------------------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [ ]

# If true, show URL addresses after external links.
#man_show_urls = False

# ------------------------------------------------------------------------------
# Options for Texinfo output
# ------------------------------------------------------------------------------

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False

# ------------------------------------------------------------------------------
# Options for Epub output
# ------------------------------------------------------------------------------

# Bibliographic Dublin Core info.
# epub_title = project
# epub_author = author
# epub_publisher = author
# epub_copyright = copyright

# The basename for the epub file. It defaults to the project name.
#epub_basename = project

# The HTML theme for the epub output. Since the default themes are not
# optimized for small screen space, using the same theme for HTML and epub
# output is usually not wise. This defaults to 'epub', a theme designed to save
# visual space.
#epub_theme = 'epub'

# The language of the text. It defaults to the language option
# or 'en' if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
#epub_scheme = ''

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
#epub_identifier = ''

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# A sequence of (type, uri, title) tuples for the guide element of content.opf.
#epub_guide = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = []

# HTML files that should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
epub_exclude_files = ['search.html']

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

# Choose between 'default' and 'includehidden'.
#epub_tocscope = 'default'

# Fix unsupported image types using the Pillow.
#epub_fix_images = False

# Scale large images.
#epub_max_image_width = 0

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#epub_show_urls = 'inline'

# If false, no index is generated.
#epub_use_index = True

# ------------------------------------------------------------------------------
loadPrjConfig()
# ------------------------------------------------------------------------------
