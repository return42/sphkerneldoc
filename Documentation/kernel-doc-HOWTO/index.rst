.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _kernel-doc-howto:

================
kernel-doc HOWTO
================

With reST as new base format the documentation building process changed
also. The building process of the output formats is now based on sphinx-doc_.  A
new kernel-doc parser extracts the kernel-doc comments from the source files and
produced reST markup which could be embedded in your documentation.

.. hint::

   This kernel-doc-HOWTO is my concept paper and not (yet) a full part of the
   Linux Kernel source tree.  The reference implementation of this
   kernel-doc-HOWTO is available from the :ref:`LinuxDoc project
   <linuxdoc:linuxdoc>`.  The examples in this kernel-doc-HOWTO are using the
   kernel-doc comments from :ref:`kernel-doc-examples`.



Documentation
=============

.. toctree::
    :maxdepth: 1

    kernel-doc-intro
    kernel-doc-syntax
    reST-kernel-doc-mode
    kernel-doc-directive
    kernel-include-directive
    table-markup
    kernel-doc-components
    vintage-kernel-doc-mode
    kernel-doc-examples


.. only:: html

   Index
   =====

   * :ref:`genindex`
