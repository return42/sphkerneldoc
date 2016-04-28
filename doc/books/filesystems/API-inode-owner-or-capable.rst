.. -*- coding: utf-8; mode: rst -*-

.. _API-inode-owner-or-capable:

======================
inode_owner_or_capable
======================

*man inode_owner_or_capable(9)*

*4.6.0-rc5*

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

Return true if current either has CAP_FOWNER in a namespace with the
inode owner uid mapped, or owns the file.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
