.. -*- coding: utf-8; mode: rst -*-

.. _API-seq-lseek:

=========
seq_lseek
=========

*man seq_lseek(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
