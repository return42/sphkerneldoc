
.. _API-proc-dointvec-ms-jiffies:

========================
proc_dointvec_ms_jiffies
========================

*man proc_dointvec_ms_jiffies(9)*

*4.6.0-rc1*

read a vector of integers as 1 milliseconds


Synopsis
========

.. c:function:: int proc_dointvec_ms_jiffies( struct ctl_table * table, int write, void __user * buffer, size_t * lenp, loff_t * ppos )

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
    the current position in the file


Description
===========

Reads/writes up to table->maxlen/sizeof(unsigned int) integer values from/to the user buffer, treated as an ASCII string. The values read are assumed to be in 1/1000 seconds, and
are converted into jiffies.

Returns 0 on success.
