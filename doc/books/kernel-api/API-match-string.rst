.. -*- coding: utf-8; mode: rst -*-

.. _API-match-string:

============
match_string
============

*man match_string(9)*

*4.6.0-rc5*

matches given string in an array


Synopsis
========

.. c:function:: int match_string( const char *const * array, size_t n, const char * string )

Arguments
=========

``array``
    array of strings

``n``
    number of strings in the array or -1 for NULL terminated arrays

``string``
    string to match with


Return
======

index of a ``string`` in the ``array`` if matches, or ``-EINVAL``
otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
