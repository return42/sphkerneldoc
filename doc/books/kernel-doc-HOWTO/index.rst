.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _kernel-doc-howto:

================
kernel-doc HOWTO
================

In order to provide embedded, 'C' friendly, easy to maintain, but consistent and
extractable documentation of the functions and data structures in the Linux
kernel, the Linux kernel has adopted a consistent style for documenting
functions and their parameters, and structures and their members.

The format for this documentation is called the *kernel-doc* format. With kernel
version 4.x the restructuredText (reST_) markup was added to the *kernel-doc*
format. The kernel-doc parser supports the markup modes:
:ref:`vintage-kernel-doc-mode` / :ref:`reST-kernel-doc-mode`.  This document
gives hints on how to use these markups and how to refer and extract
documentation from source files.

The kernel-doc parser extracts the kernel-doc descriptions from the source files
and produced reST markup as base format. With reST as base format the
documentation building process changed also. The building process is now based
on sphinx-doc_ and the DocBook documents will be migrated to reST gradually.

.. toctree::
    :maxdepth: 1

    kernel-doc-intro
    kernel-doc-syntax
    vintage-kernel-doc-mode
    reST-kernel-doc-mode
    kernel-doc-directive
    table-markup
    kernel-doc-components
    kernel-doc-examples

The examples in this HOWTO using the kernel-doc comments from the example file
:ref:`all-in-a-tumble-src`. They are rendered in the
chapter :ref:`all-in-a-tumble`.

.. only:: html

  * :ref:`genindex`

