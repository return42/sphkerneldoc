.. -*- coding: utf-8; mode: rst -*-

.. _API-bprintf:

=======
bprintf
=======

*man bprintf(9)*

*4.6.0-rc5*

Parse a format string and place args' binary value in a buffer


Synopsis
========

.. c:function:: int bprintf( u32 * bin_buf, size_t size, const char * fmt, ... )

Arguments
=========

``bin_buf``
    The buffer to place args' binary value

``size``
    The size of the buffer(by words(32bits), not characters)

``fmt``
    The format string to use @...: Arguments for the format string

``...``
    variable arguments


Description
===========

The function returns the number of words(u32) written into ``bin_buf``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
