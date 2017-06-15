.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _xref_about_this_poc:

================================================================================
                                 About this POC
================================================================================

This *POC* demonstrate some *alternative* Linux-Kernel documentation concepts.

.. toctree::
   :maxdepth: 1
   :glob:

   concepts
   about_sphinx
   why_rest
   LICENSE

-----

Most of the concepts tested here are implemented in Sphinx-doc extensions
available from the :ref:`LinuxDoc <linuxdoc:linuxdoc>` project.  If you try to
compile this POC by your own, you do not need to install LinuxDoc, but please
consider that you need a local copy of the Jon's docs-next branch::

    git://git.lwn.net/linux.git docs-next

To point to your local copy run Makefile targets with environment e.g.::

   make srctree=/to/your/linux help

Alternatively you can modify the Makefile and change the default
``srctree=/share/linux-docs-next`` to your needs:

.. code-block:: diff

   diff --git a/Makefile b/Makefile
   index 5c3036b..1b7deed 100644
   --- a/Makefile
   +++ b/Makefile
   @@ -16,5 +16,5 @@ FONTSIZE  := 11
   export DOCCLASS  := manual

   -srctree=/share/linux-docs-next
   +srctree ?= /to/your/linux
   export srctree



