.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _xref_linux_src_doc:

================================================================================
                          source code (kernel-autodoc)
================================================================================


The makefile target ``src2rst`` of this POC uses the command-line
``kernel-autodoc`` from the :ref:`linuxdoc lib <linuxdoc:linuxdoc_cmdline>` and
makes a full scan of the kernel source tree. The scan gather all kernel-doc
comments and builds a analogous tree (`reST linux_src_doc`_) of reST files with
the documentation from the source-code comments. With ``make src.html`` the HTML
page linked below is build.

* HTML rendered `Linux kernel source <../linux_src_doc/index.html>`_

.. hint::

   All you find *there* is in a experimental state!!!

.. _`reST linux_src_doc`: https://github.com/return42/sphkerneldoc/tree/master/doc/linux_src_doc

.. _`cross_references`:

cross references
================

The `Linux kernel source <../linux_src_doc/index.html>`_ page could also be used
for cross references, a feature which is available form the extension
`sphinx.ext.intersphinx`_. Add just one line to your sphinx-project:

.. code-block:: python

    intersphinx_mapping = {}
    ...
    intersphinx_mapping['linux'] = (
        'https://return42.github.io/sphkerneldoc/linux_src_doc/', None)

E.g. to refer to a function in the DVB-Frontend, write:

.. code-block:: rst

    lorem :ref:`dtv_get_frontend <linux:dtv_get_frontend>` ipsum

which will be rendered like this:

    lorem :ref:`dtv_get_frontend <linux:dtv_get_frontend>` ipsum
