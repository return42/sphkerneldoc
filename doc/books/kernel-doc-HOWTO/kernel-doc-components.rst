.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _kernel-doc-components:

===================================
Components of the kernel-doc system
===================================

Many places in the source tree have extractable kernel-doc documentation.  The
components of this system are:

Documentation/Makefile.reST and Documentation/conf.py
  Makefile and basic `sphinx config`_ file to build the various reST documents
  and output formats. Provides the basic sphinx-doc_ build infrastructure
  including the *sphinx-subprojects* feature. With this feature each book can be
  build and distributed stand-alone. Cross reference between *subprojects* will
  be ensured by `intersphinx`_.

Documentation/sphinx-static and Documentation/sphinx-tex
  Paths that contain sphinx-doc_ custom static files (such as style sheets).

Documentation/books
  In this folder, the books with reST markup are placed. To provide
  *sphinx-subprojects*, each book has its one folder and a (optional)
  ``Documentation/books/{book-name}.conf`` file which *overwrites* the basic
  configuration from ``Documentation/conf.py`` (settings see `sphinx config`_)

scripts/site-python/linuxdoc
  This folder includes python extensions related to the linux documentation
  processes.




