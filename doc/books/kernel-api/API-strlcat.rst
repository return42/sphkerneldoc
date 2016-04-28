.. -*- coding: utf-8; mode: rst -*-

.. _API-strlcat:

=======
strlcat
=======

*man strlcat(9)*

*4.6.0-rc5*

Append a length-limited, C-string to another


Synopsis
========

.. c:function:: size_t strlcat( char * dest, const char * src, size_t count )

Arguments
=========

``dest``
    The string to be appended to

``src``
    The string to append to it

``count``
    The size of the destination buffer.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
