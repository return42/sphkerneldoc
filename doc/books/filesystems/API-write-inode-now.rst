
.. _API-write-inode-now:

===============
write_inode_now
===============

*man write_inode_now(9)*

*4.6.0-rc1*

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

This function commits an inode to disk immediately if it is dirty. This is primarily needed by knfsd.

The caller must either have a ref on the inode or must have set I_WILL_FREE.
