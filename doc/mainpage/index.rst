.. -*- coding: utf-8; mode: rst -*-
.. include:: articles/refs.txt

.. _xref_linux_kernel_doc:

================================================================================
                          Linux Kernel's documentation
================================================================================

Welcome to the Linux Kernel's documentation. This POC adds reST_ to the
kernel-doc markup and replaces the DocBook toolchain with the sphinx-doc_
generator.

.. toctree::
   :maxdepth: 1

   articles/books
   articles/linux_misc_doc
   articles/linux_src_doc

The formated Linux source code documentation is based on the kernel-doc markup,
read :ref:`kernel-doc:kernel-doc-howto`. The reST_ markup comes not as a
replacement, it is an addition to the kernel-doc markup, so if you are familiar
with the *vintage* kernel-doc markup, you may switch directly to the
:ref:`kernel-doc:reST-kernel-doc-mode`.

Beside the kernel-doc source code documentation there is (has been) a
DocBook-XML toolchain to write books and convert them into various formats
(e.g. HTML).  Since reST_ is the new base format for generating output formats,
the DocBook-XML books has to migrate to reST. Within this POC, the migration is
allready done automaticly by a collection of tools and scripts (see
:ref:`xref_dbtools`). The migration is based on the linux kernel mainline and
will be updated frequently.

This site is a POC and my sandbox. All tested stuff from here is merged into
the **linux-doc-reST** branch of the linux kernel. Pull it from::

   git://github.com/return42/linux.git linux-doc-reST

The :ref:`kernel-doc:kernel-doc-howto`, :ref:`template-book:template-book` and
``make books-help`` are your friends.


Further Remarks
===============

.. toctree::
   :maxdepth: 1

   articles/why_rest
   articles/dbtools
   articles/faq
   LICENSE

