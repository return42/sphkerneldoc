.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _kernel-doc-components:

===================================
Components of the kernel-doc system
===================================

.. todo::

   description of the components is needed

..
   Many places in the source tree have extractable documentation in the
   form of block comments above functions.  The components of this system
   are:

   - scripts/kernel-doc

     This is a perl script that hunts for the block comments and can mark
     them up directly into DocBook, man, text, and HTML. (No, not
     texinfo.)

   - Documentation/DocBook/*.tmpl

     These are SGML template files, which are normal SGML files with
     special place-holders for where the extracted documentation should
     go.

   - scripts/docproc.c

     This is a program for converting SGML template files into SGML
     files. When a file is referenced it is searched for symbols
     exported (EXPORT_SYMBOL), to be able to distinguish between internal
     and external functions.
     It invokes kernel-doc, giving it the list of functions that
     are to be documented.
     Additionally it is used to scan the SGML template files to locate
     all the files referenced herein. This is used to generate dependency
     information as used by make.

   - Makefile

     The targets 'xmldocs', 'psdocs', 'pdfdocs', and 'htmldocs' are used
     to build XML DocBook files, PostScript files, PDF files, and html files
     in Documentation/DocBook. The older target 'sgmldocs' is equivalent
     to 'xmldocs'.

   - Documentation/DocBook/Makefile

     This is where C files are associated with SGML templates.

