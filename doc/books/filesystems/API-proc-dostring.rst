.. -*- coding: utf-8; mode: rst -*-

.. _API-proc-dostring:

=============
proc_dostring
=============

*man proc_dostring(9)*

*4.6.0-rc5*

read a string sysctl


Synopsis
========

.. c:function:: int proc_dostring( struct ctl_table * table, int write, void __user * buffer, size_t * lenp, loff_t * ppos )

Arguments
=========

``table``
    the sysctl table

``write``
    ``TRUE`` if this is a write to the sysctl file

``buffer``
    the user buffer

``lenp``
    the size of the user buffer

``ppos``
    file position


Description
===========

Reads/writes a string from/to the user buffer. If the kernel buffer
provided is not large enough to hold the string, the string is
truncated. The copied string is ``NULL-terminated``. If the string is
being read by the user process, it is copied and a newline '\\n' is
added. It is truncated if the buffer is not large enough.

Returns 0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
