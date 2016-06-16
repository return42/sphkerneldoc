.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _kernel-doc-directive:

================================
Use kernel-doc in reST documents
================================

There exists a `reST-directive
<http://www.sphinx-doc.org/en/stable/rest.html#directives>`_ named
``kernel-doc`` to integrate kernel-doc comments into a reST document (e.g. in a
*book*). The directive comes with options to fine grain control which parts
should be placed into the reST document. With no options given, the complete
kernel-doc comments from a source file will be inserted. So, the first and very
simple example is:

.. code-block:: rst

   My Media Book
   =============

   .. kernel-doc:: include/media/media-device.h

With this small example the kernel-doc comments from the media-device.h will be
inserted direct under the chapter "My Media Book". The "DOC:" sections, the function
and the type descriptions will be inserted in the order they appear in the source file.
Mostly you want to select more fine grained, read on to see how.

kernel-doc options
==================

Here is a short overview of the options:

.. code-block:: rst

    .. kernel-doc:: <src-filename>
        :doc: <section title>
        :no_header:
        :export:
        :internal:
        :functions: <function [, functions [, ...]]>
        :module: <prefix-id>
        :snippets:  <snippet [, snippets [, ...]]>
        :language:  <snippet-lang>
        :linenos:
        :debug:

The argument ``<src-filename>`` is required, it points to a source file in the
kernel source tree. The pathname is relativ to kernel's root folder.  The
options have the following meaning, but be aware that not all combinations of
these options make sense:

``doc <section title>``
    Include content of the ``DOC:`` section titled ``<section title>``.  Spaces
    are allowed in ``<section title>``; do not quote the ``<section title>``.

    The next option make only sense in conjunction with option ``doc``:

    ``no_header``
        Do not output DOC: section's title. Usefull, if the surrounding context
        already has a heading, and the DOC: section title is only used as an
        identifier. Take in mind, that this option will not supress any native
        reST heading markup in the comment (:ref:`reST-section-structure`).

``export [<src-fname-pattern> [, ...]]``
    Include documentation for all function, struct or whatever definition in
    ``<src-filename>``, exported using EXPORT_SYMBOL macro (``EXPORT_SYMBOL``,
    ``EXPORT_SYMBOL_GPL`` & ``EXPORT_SYMBOL_GPL_FUTURE``) either in
    ``<src-filename>`` or in any of the files specified by
    ``<src-fname-pattern>``.

    The ``<src-fname-pattern>`` (glob) is useful when the kernel-doc comments
    have been placed in header files, while EXPORT_SYMBOL are next to the
    function definitions.

``internal [<src-fname-pattern> [, ...]]``
    Include documentation for all documented definitions, **not** exported using
    EXPORT_SYMBOL macro either in ``<src-filename>`` or in any of the files
    specified by ``<src-fname-pattern>``.


``functions <name [, names [, ...]]>``
    Include documentation for each named definition.

``module <prefix-id>``
    The option ``:module: <id-prefix>`` sets a module-name. The module-name is
    used as a prefix for automatic generated IDs (reference anchors).

``snippets <name [, names [, ...]]>``
    Inserts the source-code passage(s) marked with the snippet ``name``. The
    snippet is inserted with a `code-block:: <http://www.sphinx-doc.org/en/stable/markup/code.html>`_
    directive.

    The next options make only sense in conjunction with option ``snippets``:

    ``language <highlighter>``
        Set highlighting language of the snippet code-block.

    ``linenos``
        Set line numbers in the snippet code-block.

``debug``
    Inserts a code-block with the generated reST source. This might somtimes
    helpful to see how the kernel-doc parser transforms the kernel-doc markup to
    reST markup.

ducumentation blocks
====================

The following example inserts the documentation block with the title "Theory of
Operation".

.. code-block:: rst

     .. kernel-doc::  ./all-in-a-tumble.h
        :doc:  Theory of Operation
        :module: example

With the module name "example" the title refers by:

.. code-block:: rst

    Rendered example: :ref:`example.theory-of-operation`

Rendered example: :ref:`example.theory-of-operation`

functions
=========

The following example inserts the documentation of struct 'user_function'.

.. code-block:: rst

     .. kernel-doc:: ./all-in-a-tumble.h
        :functions:  user_function
        :module:     example

.. code-block:: rst

    * Rendered example by ID with module prefix: :ref:`example.user_function`
    * Function reference: :c:func:`user_function`

* Rendered example by ID with module prefix: :ref:`example.user_function`
* Function reference: :c:func:`user_function`


structs, unions, enums and typedefs
===================================

The following example inserts the documentation of struct 'my_long_struct'.

.. code-block:: rst

     .. kernel-doc:: ./all-in-a-tumble.h
        :functions:  my_long_struct
        :module:     example

.. code-block:: rst

    * Rendered example by ID with module prefix: :ref:`example.my_long_struct`
    * Type reference: :c:type:`my_long_struct` or the alternativ notation
      with title :c:type:`struct my_long_struct <my_long_struct>`

* Rendered example by ID with module prefix: :ref:`example.my_long_struct`
* Type reference: :c:type:`my_long_struct` or the alternativ notation
  with title :c:type:`struct my_long_struct <my_long_struct>`

exported
========

.. code-block:: rst

  .. kernel-doc:: include/uapi/linux/dvb/frontend.h
     :export: net/mac80211/*.c
     :module: mac80211


Snippets
========

The kernel-doc Parser supports a comment-markup for
:ref:`kernel-doc-syntax-snippets`. By example; The directive of the shown
code-snippet below is:

.. code-block:: rst

     .. kernel-doc::  ./all-in-a-tumble.c
        :snippets:  hello-world
        :language:  c
        :linenos:

.. kernel-doc::  ./all-in-a-tumble.c
    :snippets:  hello-world
    :language:  c
    :linenos:

kernel-doc config
=================

Within the sphinx-doc config file (``conf.py`` or ``my_project.conf``) you can
set the following option.

kernel_doc_raise_error: ``True``
  If true, fatal errors (like missing function descriptions) raise an error. The
  default is ``True``. Because this might break your build process, you can
  change the value to ``False``.

  In this example, the documentation of definition ``no_longer_exists`` is
  required.

  .. code-block:: rst

      .. kernel-doc::  ./all-in-a-tumble.h
          :functions:  no_longer_exist

  Since this definition not exists (anymore), the following TODO entry is
  inserted, when ``kernel_doc_raise_error`` is ``False``.

  .. admonition:: an error gives a ".. todo::" directive with *Oops* in
      :class: rst-example

       .. kernel-doc::  ./all-in-a-tumble.h
           :functions:  no_longer_exist


kernel_doc_verbose_warn: ``True``
  If true, more warnings will be logged. E.g. a missing description of a
  function's return value will be logged.

kernel_doc_mode: ``reST``
  Set parser's default kernel-doc mode ``reST|kernel-doc``. See
  :ref:`reST-kernel-doc-mode` and :ref:`vintage-kernel-doc-mode`.
