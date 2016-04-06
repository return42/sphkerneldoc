
.. _API-iput:

====
iput
====

*man iput(9)*

*4.6.0-rc1*

put an inode


Synopsis
========

.. c:function:: void iput( struct inode * inode )

Arguments
=========

``inode``
    inode to put


Description
===========

Puts an inode, dropping its usage count. If the inode use count hits zero, the inode is then freed and may also be destroyed.

Consequently, ``iput`` can sleep.
