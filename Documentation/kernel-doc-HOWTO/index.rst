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

  The reference implementation of this kernel-doc-HOWTO is available from the
  :ref:`LinuxDoc project <linuxdoc:linuxdoc>`. The kernel-doc parser supports
  two parsing modes, one for downward compatibility
  (:ref:`vintage-kernel-doc-mode`) and one for the upcoming reST markup
  (:ref:`reST-kernel-doc-mode`).

The examples in this kernel-doc-HOWTO using the kernel-doc comments from the
example file :ref:`all-in-a-tumble-src`. This file is rendered in the chapter
:ref:`all-in-a-tumble`.

.. hint::

   This kernel-doc-HOWTO is my concept paper and not (yet) a full part of the
   Linux Kernel source tree.


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
