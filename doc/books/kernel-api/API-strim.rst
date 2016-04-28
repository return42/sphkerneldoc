.. -*- coding: utf-8; mode: rst -*-

.. _API-strim:

=====
strim
=====

*man strim(9)*

*4.6.0-rc5*

Removes leading and trailing whitespace from ``s``.


Synopsis
========

.. c:function:: char * strim( char * s )

Arguments
=========

``s``
    The string to be stripped.


Description
===========

Note that the first trailing whitespace is replaced with a
``NUL-terminator`` in the given string ``s``. Returns a pointer to the
first non-whitespace character in ``s``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
