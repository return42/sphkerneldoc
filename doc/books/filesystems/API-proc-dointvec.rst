
.. _API-proc-dointvec:

=============
proc_dointvec
=============

*man proc_dointvec(9)*

*4.6.0-rc1*

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

Reads/writes up to table->maxlen/sizeof(unsigned int) integer values from/to the user buffer, treated as an ASCII string.

Returns 0 on success.
