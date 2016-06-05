.. -*- coding: utf-8; mode: rst -*-

.. _xref_linux_src_doc:

================================================================================
                             source code (autodoc)
================================================================================

Source code documentation from *autodoc* (``make htmlsrc``).

* `Linux kernel source <../linux_src_doc/index.html>`_

To build the reST file from the linux kernel sources run:

.. code-block:: bash

   cd doc
   make src2rst

The makefile target ``src2rst`` uses the script ``./scripts/autodoc.sh`` to
build the `reST linux_src_doc`_ tree from the source-code comments
(:ref:`xref_kernel-doc`).

The documentation is taken from all source files listet in the
`src_filelist`_. The `reST linux_src_doc`_ files are versioned within this
reposetory, a rebuild is only required when the linux kernel sources are updated
to a new release or the `src_filelist`_ is changed. With ``make htmlsrc`` the
HTML page linked above is build.

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

.. _xref_kernel-doc:

