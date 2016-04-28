.. -*- coding: utf-8; mode: rst -*-

.. _API-sysfs-streq:

===========
sysfs_streq
===========

*man sysfs_streq(9)*

*4.6.0-rc5*

return true if strings are equal, modulo trailing newline


Synopsis
========

.. c:function:: bool sysfs_streq( const char * s1, const char * s2 )

Arguments
=========

``s1``
    one string

``s2``
    another string


Description
===========

This routine returns true iff two strings are equal, treating both NUL
and newline-then-NUL as equivalent string terminations. It's geared for
use with sysfs input strings, which generally terminate with newlines
but are compared against values without newlines.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
