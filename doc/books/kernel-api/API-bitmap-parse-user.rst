.. -*- coding: utf-8; mode: rst -*-

.. _API-bitmap-parse-user:

=================
bitmap_parse_user
=================

*man bitmap_parse_user(9)*

*4.6.0-rc5*

convert an ASCII hex string in a user buffer into a bitmap


Synopsis
========

.. c:function:: int bitmap_parse_user( const char __user * ubuf, unsigned int ulen, unsigned long * maskp, int nmaskbits )

Arguments
=========

``ubuf``
    pointer to user buffer containing string.

``ulen``
    buffer size in bytes. If string is smaller than this then it must be
    terminated with a \\0.

``maskp``
    pointer to bitmap array that will contain result.

``nmaskbits``
    size of bitmap, in bits.


Description
===========

Wrapper for ``__bitmap_parse``, providing it with user buffer.

We cannot have this as an inline function in bitmap.h because it needs
linux/uaccess.h to get the ``access_ok`` declaration and this causes
cyclic dependencies.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
