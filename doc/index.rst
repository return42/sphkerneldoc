.. -*- coding: utf-8; mode: rst -*-

.. _`Sphinx-Doc`: http://www.sphinx-doc.org/
.. _`intersphinx`: http://www.sphinx-doc.org/en/stable/ext/intersphinx.html

.. _xref_linux_kernel_doc:

================================================================================
                       Linux Kernel's documentation (POC)
================================================================================

Welcome to the Linux Kernel's documentation. This is a proof of concept, a
toolchain to migrate the Kernel's documentation to the `Sphinx-Doc`_ generator.

* https://sphkerneldoc.readthedocs.org
* https://github.com/return42/sphkerneldoc.git

The Kerner's documentation (the scope of content to migrate) is made up from:

.. toctree::
   :maxdepth: 1

   doc_from_source
   misc_doc_from_tree
   migrated_docbock

... what more should we consider?

In this POC only one (huge) document is created. In the long run the
documentation has to be chunked into small *projects*, each with it's own
document, which can be generated and distributed stand-alone. Cross reference
between these *projects* will be ensured by `intersphinx`_. The term *project*
has to be defined.


Discussion & related efforts
============================

* http://marc.info/?t=145540043500001&r=1&w=2
* http://static.lwn.net/kerneldoc/index.html
* https://git.linuxtv.org/mchehab/v4l2-docs-poc.git/
* https://mchehab.fedorapeople.org/media-kabi-docs-test/asciidoc_tests/media_api.html



Indices and tables
==================

* :ref:`genindex`
* :ref:`search`

