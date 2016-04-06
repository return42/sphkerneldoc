
.. _API-inode-permission:

================
inode_permission
================

*man inode_permission(9)*

*4.6.0-rc1*

Check for access rights to a given inode


Synopsis
========

.. c:function:: int inode_permission( struct inode * inode, int mask )

Arguments
=========

``inode``
    Inode to check permission on

``mask``
    Right to check for (``MAY_READ``, ``MAY_WRITE``, ``MAY_EXEC``)


Description
===========

Check for read/write/execute permissions on an inode. We use fs[ug]id for this, letting us set arbitrary permissions for filesystem access without changing the “normal” UIDs which
are used for other things.

When checking for MAY_APPEND, MAY_WRITE must also be set in ``mask``.
