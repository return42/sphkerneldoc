.. -*- coding: utf-8; mode: rst -*-

.. _xref_doc_from_source:

================================================================================
                                Doc from sources
================================================================================

:STATE: POV: autodoc generation of rst-files is simple but works (improve- &
    expandable)

Building reStructuredText doc trees would be done by:

.. code-block:: bash

   ./scripts/autodoc.sh

The script ``autodoc.sh`` uses a modified version of ``kernel-doc`` to extract
the doc-comments. The kernel sourcecode trees are chunked in smaler
*projects*. Within this POV we will extract only a few *projects*, e.g. the
``drivers/media`` from the LinuxTV project.

generated documents
===================

.. toctree::
   :maxdepth: 2

   linux_src_doc/index

