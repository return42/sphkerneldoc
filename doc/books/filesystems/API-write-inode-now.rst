.. -*- coding: utf-8; mode: rst -*-

.. _API-write-inode-now:

===============
write_inode_now
===============

*man write_inode_now(9)*

*4.6.0-rc5*

write an inode to disk


Synopsis
========

.. c:function:: int write_inode_now( struct inode * inode, int sync )

Arguments
=========

``inode``
    inode to write to disk

``sync``
    whether the write should be synchronous or not


Description
===========

This function commits an inode to disk immediately if it is dirty. This
is primarily needed by knfsd.

The caller must either have a ref on the inode or must have set
I_WILL_FREE.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
