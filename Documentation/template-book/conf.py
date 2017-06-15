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

# Set parser's default kernel-doc mode ``reST|kernel-doc``.
kernel_doc_mode = "reST"

# ------------------------------------------------------------------------------
# General configuration
# ------------------------------------------------------------------------------

project   = u'Template Book'
copyright = u'2016, The kernel development community'
author    = u'The kernel development community'

# Intersphinx
# -----------
#
# usage:  lorem :ref:`dtv_get_frontend <linux:dtv_get_frontend>` ipsum

# since https://h2626237.stratoserver.net/ is self-signed, disable tls verify
tls_verify = False

intersphinx_mapping['kernel-doc'] = ('https://h2626237.stratoserver.net/kernel/books/kernel-doc-HOWTO', None)
intersphinx_mapping['sphkerneldoc'] = ('https://h2626237.stratoserver.net/kernel/', None)

# ------------------------------------------------------------------------------
# Options for HTML output
# ------------------------------------------------------------------------------

# The name for this set of Sphinx documents.  If None, it defaults to
# Output file base name for HTML help builder.
htmlhelp_basename = main_name

