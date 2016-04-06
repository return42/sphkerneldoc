
.. _API-seq-release:

===========
seq_release
===========

*man seq_release(9)*

*4.6.0-rc1*

free the structures associated with sequential file.


Synopsis
========

.. c:function:: int seq_release( struct inode * inode, struct file * file )

Arguments
=========

``inode``
    its inode

``file``
    file in question


Description
===========

Frees the structures associated with sequential file; can be used as ->f_op->``release`` if you don't have private data to destroy.
