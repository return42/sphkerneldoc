.. -*- coding: utf-8; mode: rst -*-

.. _API-kstrtoint:

=========
kstrtoint
=========

*man kstrtoint(9)*

*4.6.0-rc5*

convert a string to an int


Synopsis
========

.. c:function:: int kstrtoint( const char * s, unsigned int base, int * res )

Arguments
=========

``s``
    The start of the string. The string must be null-terminated, and may
    also include a single newline before its terminating null. The first
    character may also be a plus sign or a minus sign.

``base``
    The number base to use. The maximum supported base is 16. If base is
    given as 0, then the base of the string is automatically detected
    with the conventional semantics - If it begins with 0x the number
    will be parsed as a hexadecimal (case insensitive), if it otherwise
    begins with 0, it will be parsed as an octal number. Otherwise it
    will be parsed as a decimal.

``res``
    Where to write the result of the conversion on success.


Description
===========

Returns 0 on success, -ERANGE on overflow and -EINVAL on parsing error.
Used as a replacement for the obsolete simple_strtoull. Return code
must be checked.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
