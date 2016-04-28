.. -*- coding: utf-8; mode: rst -*-

.. _API-vsnprintf:

=========
vsnprintf
=========

*man vsnprintf(9)*

*4.6.0-rc5*

Format a string and place it in a buffer


Synopsis
========

.. c:function:: int vsnprintf( char * buf, size_t size, const char * fmt, va_list args )

Arguments
=========

``buf``
    The buffer to place the result into

``size``
    The size of the buffer, including the trailing null space

``fmt``
    The format string to use

``args``
    Arguments for the format string


Description
===========

This function generally follows C99 vsnprintf, but has some


extensions and a few limitations
================================

``n`` is unsupported ``p``\ * is handled by ``pointer``

See ``pointer`` or Documentation/printk-formats.txt for more extensive
description.

** Please update the documentation in both places when making changes **

The return value is the number of characters which would be generated
for the given input, excluding the trailing '\\0', as per ISO C99. If
you want to have the exact number of characters written into ``buf`` as
return value (not including the trailing '\\0'), use ``vscnprintf``. If
the return is greater than or equal to ``size``, the resulting string is
truncated.

If you're not already dealing with a va_list consider using
``snprintf``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
