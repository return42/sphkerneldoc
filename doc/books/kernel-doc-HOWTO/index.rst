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

The format for this documentation is called the *kernel-doc* format.

With kernel version 4.x the restructuredText (reST_) markup was added to the
*kernel-doc* forma. This document gives hints on how to use the reST markup
within the *kernel-doc* format and how to refer or extract documentation from
source files.

With the reST addition the, documentation building process changed also. The
building process is now based on sphinx-doc_ and the DocBook documents will be
migrated to reST gradually.

.. toctree::
   :maxdepth: 1

   kernel-doc-intro
   kernel-doc-syntax
   vintage-kernel-doc-mode
   reST-kernel-doc-mode
   kernel-doc-components
   extract-kernel-doc


Some examples and *tests* (tests here might be droped later).

.. toctree::
   :maxdepth: 1

   all-in-a-tumble
