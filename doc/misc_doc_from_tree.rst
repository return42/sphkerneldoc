.. -*- coding: utf-8; mode: rst -*-

.. _xref_misc_doc_from_tree:

.. _`reST`: http://docutils.sourceforge.net/rst.html
.. _`Markdown`: http://daringfireball.net/projects/markdown/

================================================================================
                       Misc doc from *Documentation* tree
================================================================================

:STATE: in progress ...

Sync kernels' documentation would be done by:

.. code-block:: bash

   ./scripts/syncdoc.sh

Methods to sync and migrate documents from the origin:

* If doc-files are using any proprietary / individual markup,

  import / sync these files as *literalinclude*.

* If doc-files are allready using the `reST`_ markup.

  import / sync these files *as is*.

* If doc-files use `Markdown`_ or any other known markup

  convert with known tools and import / sync these files.

* suggestions?

migrated documents
==================

.. toctree::
   :maxdepth: 2

   linux_misc_doc/index

