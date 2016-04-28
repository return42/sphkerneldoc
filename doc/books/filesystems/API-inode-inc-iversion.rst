.. -*- coding: utf-8; mode: rst -*-

.. _API-inode-inc-iversion:

==================
inode_inc_iversion
==================

*man inode_inc_iversion(9)*

*4.6.0-rc5*

increments i_version


Synopsis
========

.. c:function:: void inode_inc_iversion( struct inode * inode )

Arguments
=========

``inode``
    inode that need to be updated


Description
===========

Every time the inode is modified, the i_version field will be
incremented. The filesystem has to be mounted with i_version flag


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
