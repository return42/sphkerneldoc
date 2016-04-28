.. -*- coding: utf-8; mode: rst -*-

.. _API-seq-write:

=========
seq_write
=========

*man seq_write(9)*

*4.6.0-rc5*

write arbitrary data to buffer


Synopsis
========

.. c:function:: int seq_write( struct seq_file * seq, const void * data, size_t len )

Arguments
=========

``seq``
    seq_file identifying the buffer to which data should be written

``data``
    data address

``len``
    number of bytes


Description
===========

Return 0 on success, non-zero otherwise.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
