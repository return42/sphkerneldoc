
.. _API-inode-owner-or-capable:

======================
inode_owner_or_capable
======================

*man inode_owner_or_capable(9)*

*4.6.0-rc1*

check current task permissions to inode


Synopsis
========

.. c:function:: bool inode_owner_or_capable( const struct inode * inode )

Arguments
=========

``inode``
    inode being checked


Description
===========

Return true if current either has CAP_FOWNER in a namespace with the inode owner uid mapped, or owns the file.
