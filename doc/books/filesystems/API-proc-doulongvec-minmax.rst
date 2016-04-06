
.. _API-proc-doulongvec-minmax:

======================
proc_doulongvec_minmax
======================

*man proc_doulongvec_minmax(9)*

*4.6.0-rc1*

read a vector of long integers with min/max values


Synopsis
========

.. c:function:: int proc_doulongvec_minmax( struct ctl_table * table, int write, void __user * buffer, size_t * lenp, loff_t * ppos )

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

Reads/writes up to table->maxlen/sizeof(unsigned long) unsigned long values from/to the user buffer, treated as an ASCII string.

This routine will ensure the values are within the range specified by table->extra1 (min) and table->extra2 (max).

Returns 0 on success.
