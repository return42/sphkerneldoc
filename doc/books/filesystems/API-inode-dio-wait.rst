.. -*- coding: utf-8; mode: rst -*-

.. _API-inode-dio-wait:

==============
inode_dio_wait
==============

*man inode_dio_wait(9)*

*4.6.0-rc5*

wait for outstanding DIO requests to finish


Synopsis
========

.. c:function:: void inode_dio_wait( struct inode * inode )

Arguments
=========

``inode``
    inode to wait for


Description
===========

Waits for all pending direct I/O requests to finish so that we can
proceed with a truncate or equivalent operation.

Must be called under a lock that serializes taking new references to
i_dio_count, usually by inode->i_mutex.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
