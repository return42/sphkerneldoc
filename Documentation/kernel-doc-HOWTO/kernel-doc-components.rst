.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _kernel-doc-components:

===================================
Components of the kernel-doc system
===================================

Many places in the source tree have extractable kernel-doc documentation.  The
components of this system are:

Documentation/template-book
  Template book and build configuration. It includes additional hints and
  practical recommendations: :ref:`template-book:get-started`.

Documentation/Makefile.reST and Documentation/conf.py
  Makefile and basic `sphinx config`_ file to build the various reST documents
  and output formats. Provides the basic sphinx-doc_ build infrastructure
  including the *sphinx-subprojects* feature. With this feature each book can be
  build and distributed stand-alone. Cross reference between *subprojects* will
  be ensured by `intersphinx`_.

Documentation/sphinx-static
  Paths that contain sphinx-doc_ custom static files (such as style sheets).

Documentation/index.rst and the other Documentation/\*.rst
  The ``*.rst`` files, are *loose reST articles*, formerly known as *text
  files*.  Theirs html is build by the ``books-index`` target, which is also a
  prerequisite of the main target ``htmldocs``.

Documentation/\*/conf.py
  In the folders with a ``*/conf.py``, the books with reST markup are
  placed. To provide *sphinx-subprojects*, each book has it's own folder and a
  ``Documentation/*/conf.py`` file which *overwrites* the basic configuration
  from ``Documentation/conf.py`` (settings see `sphinx config`_)

:ref:`LinuxDoc project <linuxdoc:linuxdoc>`
  This includes python extensions related to the Linux documentation processes,
  see installation instructions at :ref:`LinuxDoc project <linuxdoc:linuxdoc>`.

Documentation/books_migrated
  Content the of automatic migrated DocBook-XML to reST documents
  (:ref:`dbxml2rst_migration`).

