.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _kernel-doc-howto:

================
kernel-doc HOWTO
================

:author: Tim
:address: twaugh@redhat.com
:author: Markus Heiser
:address: markus.heiser@darmarIT.de


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
    dbxml2rst_migration
    kernel-doc-examples

Get Started
===========

If you like to write documentation with reST markup, a good starting
point might be:

* Write a *loose reST article*, which is just a ordinary text file with reST
  markup in, see ``Documentation/reST-nano-HOWTO.rst``
  (:ref:`kernel-articles:reST-nano-HOWTO`)

* Create a *book* (aka sphinx-project) by copying the template book from
  ``Documentation/template-book`` (:ref:`template-book:get-started`).


About
=====

In order to provide embedded, 'C' friendly, easy to maintain, but consistent and
extractable documentation of the functions and data structures in the Linux
kernel, the Linux kernel has adopted a consistent style for documenting
functions and their parameters, and structures and their members.  The format
for this documentation is called the **kernel-doc** format. This document
describes the kernel-doc format and gives hints on how to refer and extract
kernel-doc comments from source code.

  With kernel version 4.8 the reStructuredText (reST_) markup replaced the
  DocBook-XML format.

With reST as new base format the documentation building process changed
also. The building process is now based on sphinx-doc_ and the DocBook documents
will be migrated to reST gradually.  A new/modified kernel-doc parser extracts
the kernel-doc comments from the source files and produced reST markup which
could be embedded in your documentation.

  The reference implementation of this kernel-doc-HOWTO is available from the
  :ref:`LinuxDoc project <linuxdoc:linuxdoc>`. The kernel-doc parser supports
  two parsing modes, one for downward compatibility
  (:ref:`vintage-kernel-doc-mode`) and one for the upcoming reST markup
  (:ref:`reST-kernel-doc-mode`).

.. hint::

   This kernel-doc-HOWTO is my concept paper and not (yet) a full part of the
   Linux Kernel source tree.


The examples in this kernel-doc-HOWTO using the kernel-doc comments from the
example file :ref:`all-in-a-tumble-src`. This file is rendered in the chapter
:ref:`all-in-a-tumble`.


.. only:: html

   Index
   =====

   * :ref:`genindex`
