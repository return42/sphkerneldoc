.. -*- coding: utf-8; mode: rst -*-

.. _API-d-path:

======
d_path
======

*man d_path(9)*

*4.6.0-rc5*

return the path of a dentry


Synopsis
========

.. c:function:: char * d_path( const struct path * path, char * buf, int buflen )

Arguments
=========

``path``
    path to report

``buf``
    buffer to return value in

``buflen``
    buffer length


Description
===========

Convert a dentry into an ASCII path name. If the entry has been deleted
the string “(deleted)” is appended. Note that this is ambiguous.

Returns a pointer into the buffer or an error code if the path was too
long. Note: Callers should use the returned pointer, not the passed in
buffer, to use the name! The implementation often starts at an offset
into the buffer, and may leave 0 bytes at the start.

“buflen” should be positive.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
