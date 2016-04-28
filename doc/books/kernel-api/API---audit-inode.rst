.. -*- coding: utf-8; mode: rst -*-

.. _API---audit-inode:

=============
__audit_inode
=============

*man __audit_inode(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
