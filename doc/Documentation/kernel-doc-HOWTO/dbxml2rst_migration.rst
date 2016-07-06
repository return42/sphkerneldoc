.. -*- coding: utf-8; mode: rst -*-
.. include:: refs.txt

.. _dbxml2rst_migration:

=============================
DocBook-XML to reST migration
=============================

The folder ``Documentation/books_migrated`` is only for shipping the automatic
migrated DocBook-XML to reST documents.

* The automatic migration is described in `dbtools`_.

Take a look at the commit message log, to see on which commit each
migration was applied.

Review
======

It is recommended to review each automatic migrated document. The migration
itself is mostly perfect, but there are some other (historical) reasons
whichever could cause an improper document. Here are some:

* The new document build toolchain is more strict than the old one.

* The old kernel-doc/docproc was/is buggy, e.g. it includs all declarations when
  only exported (``!E<filename>``) should be included, but in the sorce file are no
  symbols exported. The ``!Elib/debugobjects.c`` of the ``debugobjects.tmpl`` is
  an example for this. In the past, this *misbehavior* of the docproc has been
  taken as a feature, by the authors :-o

* Error messages has been ignored.

* Implicit rules like ``!E<filename>`` or ``I<filename>`` are prone for silent
  mistakes. E.g. if a exported function or Macros has been moved to an other
  location, there is no error message at all and the document's content get lost
  silent :-o

.. caution::

   If you are willing to review a book, move the book from the
   ``Documentation/books_migrated/<name>`` folder down to the
   ``Documentation/<name>`` folder.



