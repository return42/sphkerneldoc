.. -*- coding: utf-8; mode: rst -*-

.. _API-strncpy:

=======
strncpy
=======

*man strncpy(9)*

*4.6.0-rc5*

Copy a length-limited, C-string


Synopsis
========

.. c:function:: char * strncpy( char * dest, const char * src, size_t count )

Arguments
=========

``dest``
    Where to copy the string to

``src``
    Where to copy the string from

``count``
    The maximum number of bytes to copy


Description
===========

The result is not ``NUL-terminated`` if the source exceeds ``count``
bytes.

In the case where the length of ``src`` is less than that of count, the
remainder of ``dest`` will be padded with ``NUL``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
