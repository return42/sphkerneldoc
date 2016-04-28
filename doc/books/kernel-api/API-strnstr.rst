.. -*- coding: utf-8; mode: rst -*-

.. _API-strnstr:

=======
strnstr
=======

*man strnstr(9)*

*4.6.0-rc5*

Find the first substring in a length-limited string


Synopsis
========

.. c:function:: char * strnstr( const char * s1, const char * s2, size_t len )

Arguments
=========

``s1``
    The string to be searched

``s2``
    The string to search for

``len``
    the maximum number of characters to search


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
