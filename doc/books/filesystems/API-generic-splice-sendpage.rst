.. -*- coding: utf-8; mode: rst -*-

.. _API-generic-splice-sendpage:

=======================
generic_splice_sendpage
=======================

*man generic_splice_sendpage(9)*

*4.6.0-rc5*

splice data from a pipe to a socket


Synopsis
========

.. c:function:: ssize_t generic_splice_sendpage( struct pipe_inode_info * pipe, struct file * out, loff_t * ppos, size_t len, unsigned int flags )

Arguments
=========

``pipe``
    pipe to splice from

``out``
    socket to write to

``ppos``
    position in ``out``

``len``
    number of bytes to splice

``flags``
    splice modifier flags


Description
===========

Will send ``len`` bytes from the pipe to a network socket. No data
copying is involved.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
