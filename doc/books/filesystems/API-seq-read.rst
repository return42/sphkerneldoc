.. -*- coding: utf-8; mode: rst -*-

.. _API-seq-read:

========
seq_read
========

*man seq_read(9)*

*4.6.0-rc5*

->``read`` method for sequential files.


Synopsis
========

.. c:function:: ssize_t seq_read( struct file * file, char __user * buf, size_t size, loff_t * ppos )

Arguments
=========

``file``
    the file to read from

``buf``
    the buffer to read to

``size``
    the maximum number of bytes to read

``ppos``
    the current position in the file


Description
===========

Ready-made ->f_op->``read``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
