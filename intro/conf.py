# -*- coding: utf-8; mode: python -*-
#
# This is the project specific sphinx-build configuration, which is loaded from
# the base configuration file (``../conf.py``). About config values consult:
#
# * http://www.sphinx-doc.org/en/stable/config.html
#
# While setting values here, please take care to not overwrite common needed
# configurations. This means, do not *overwrite* composite values (e.g. the
# list- or dictionary-value of "latex_elements" resp. "extensions") by
# thoughtless assignments. Manipulate composite values always by *update*
# (dict-values) or extend (list-values). Nevertheless, if you know what you are
# doing, you are free to *overwrite* values to your needs.
#
# useful preset names:
#
# * BASE_FOLDER: the folder where the top conf.py is located
# * main_name:   the basename of this project-folder

# ------------------------------------------------------------------------------
# General configuration
# ------------------------------------------------------------------------------

project   = u'POC'
copyright = u'2016, Linux documentation authors'
author    = u'Linux contributors'

intersphinx_mapping['linuxdoc'] =  ('https://return42.github.io/linuxdoc', None)
intersphinx_mapping['dbxml2rst'] =  ('https://return42.github.io/dbxml2rst', None)

intersphinx_mapping['linux'] = ('https://h2626237.stratoserver.net/kernel/linux_src_doc/', None)
intersphinx_mapping['kernel-doc'] = ('https://h2626237.stratoserver.net/kernel/books/kernel-doc-HOWTO', None)
intersphinx_mapping['template-book'] = ('https://h2626237.stratoserver.net/kernel/books/template-book/', None)

# ------------------------------------------------------------------------------
# Options for HTML output
# ------------------------------------------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = main_name

