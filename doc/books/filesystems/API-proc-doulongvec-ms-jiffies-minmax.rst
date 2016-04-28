.. -*- coding: utf-8; mode: rst -*-

.. _API-proc-doulongvec-ms-jiffies-minmax:

=================================
proc_doulongvec_ms_jiffies_minmax
=================================

*man proc_doulongvec_ms_jiffies_minmax(9)*

*4.6.0-rc5*

read a vector of millisecond values with min/max values


Synopsis
========

.. c:function:: int proc_doulongvec_ms_jiffies_minmax( struct ctl_table * table, int write, void __user * buffer, size_t * lenp, loff_t * ppos )

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

Reads/writes up to table->maxlen/sizeof(unsigned long) unsigned long
values from/to the user buffer, treated as an ASCII string. The values
are treated as milliseconds, and converted to jiffies when they are
stored.

This routine will ensure the values are within the range specified by
table->extra1 (min) and table->extra2 (max).

Returns 0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
