
.. _API-seq-lseek:

=========
seq_lseek
=========

*man seq_lseek(9)*

*4.6.0-rc1*

->``llseek`` method for sequential files.


Synopsis
========

.. c:function:: loff_t seq_lseek( struct file * file, loff_t offset, int whence )

Arguments
=========

``file``
    the file in question

``offset``
    new position

``whence``
    0 for absolute, 1 for relative position


Description
===========

Ready-made ->f_op->``llseek``
