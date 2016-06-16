.. -*- coding: utf-8; mode: rst -*-

.. _kernel-doc-tests:

================
Additional tests
================


DOC sections
============

The DOC section tests are based on this comment:

.. kernel-doc::  ./all-in-a-tumble.h
    :snippets:  theory-of-operation

multiple DOC sections
---------------------

.. code-block:: rst

   .. kernel-doc::  ./all-in-a-tumble.h
       :doc: multiple DOC sections
       :no_header:

.. admonition:: DOC section
    :class: rst-example

    .. kernel-doc::  ./all-in-a-tumble.h
        :doc: multiple DOC sections
        :no_header:


option no_header
----------------

.. code-block:: rst

    .. kernel-doc::  ./all-in-a-tumble.h
        :doc:  Theory of Operation
        :no_header:

.. admonition:: DOC section with "no_header"
    :class: rst-example

    .. kernel-doc::  ./all-in-a-tumble.h
        :doc:  Theory of Operation
        :no_header:


exported symbols
================

Get documentation of exported symbols
-------------------------------------

This test gathers exports from ``all-in-a-tumble.h`` and ``all-in-a-tumble.c``
and parses comments from ``all-in-a-tumble.c``.

.. code-block:: rst

    .. kernel-doc::  ./all-in-a-tumble.c
        :export:  ./all-in-a-tumble.h
        :module: example

.. admonition:: exported symbols
    :class: rst-example

    .. kernel-doc::  ./all-in-a-tumble.c
        :export:  ./all-in-a-tumble.h
        :module: example


Get documentation of internal symbols
-------------------------------------

This test gathers exports from ``all-in-a-tumble.h`` and ``all-in-a-tumble.c``
and parses comments from ``all-in-a-tumble.c``, from where only the *not
exported* definitions are used in the reST output:

.. code-block:: rst

    .. kernel-doc::  ./all-in-a-tumble.c
        :internal:  ./all-in-a-tumble.h
        :module: example

.. admonition:: internal symbols
    :class: rst-example

    .. kernel-doc::  ./all-in-a-tumble.c
        :internal:  ./all-in-a-tumble.h
        :module: example


Missing exports
---------------

In the next test, the ``:export: {file glob pattern}`` is used, but it does not
match any file, or there are no exports in the matching files. Whatever, An
empty list of exported symbols is treated as an error:

.. code-block:: rst

    .. kernel-doc::  ./all-in-a-tumble.c
        :export:  ./match_files_without_exports*

.. admonition:: missing exports
    :class: rst-example

    .. kernel-doc::  ./all-in-a-tumble.c
        :export:  ./match_files_without_exports*

