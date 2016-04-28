.. -*- coding: utf-8; mode: rst -*-

.. _API-proc-dointvec:

=============
proc_dointvec
=============

*man proc_dointvec(9)*

*4.6.0-rc5*

read a vector of integers


Synopsis
========

.. c:function:: int proc_dointvec( struct ctl_table * table, int write, void __user * buffer, size_t * lenp, loff_t * ppos )

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

Reads/writes up to table->maxlen/sizeof(unsigned int) integer values
from/to the user buffer, treated as an ASCII string.

Returns 0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
