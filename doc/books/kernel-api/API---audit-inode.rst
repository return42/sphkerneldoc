
.. _API---audit-inode:

=============
__audit_inode
=============

*man __audit_inode(9)*

*4.6.0-rc1*

store the inode and device from a lookup


Synopsis
========

.. c:function:: void __audit_inode( struct filename * name, const struct dentry * dentry, unsigned int flags )

Arguments
=========

``name``
    name being audited

``dentry``
    dentry being audited

``flags``
    attributes for this particular entry
