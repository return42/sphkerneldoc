.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _xref_linux_src_doc:

================================================================================
                             source code (autodoc)
================================================================================

Source code documentation from *autodoc*.

* `Linux kernel source <../linux_src_doc/index.html>`_

.. hint::

   All you find *there* is in a experimental state!!!

autodoc
=======

.. _`reST linux_src_doc`: https://github.com/return42/sphkerneldoc/tree/master/doc/linux_src_doc

The makefile target ``src2rst`` uses the script ``scripts/autodoc.py`` which
makes a full scan of the kernel source tree, gather all kernel-doc comments and
builds a analogous tree (`reST linux_src_doc`_) of reST files with the
documentation from the source-code comments.

.. code-block:: bash

   cd doc
   make src2rst

The `reST linux_src_doc`_ files are versioned within this reposetory. A rebuild
is only required when the linux kernel sources are updated to a new release.
With ``make src.html`` the HTML page linked above is build.

.. _`cross_references`:

cross references
================

The `Linux kernel source <../linux_src_doc/index.html>`_ page could also be used
for cross references, a feature wich is available form the extension
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
