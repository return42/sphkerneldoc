.. -*- coding: utf-8; mode: rst -*-

.. _API-unlock-new-inode:

================
unlock_new_inode
================

*man unlock_new_inode(9)*

*4.6.0-rc5*

clear the I_NEW state and wake up any waiters


Synopsis
========

.. c:function:: void unlock_new_inode( struct inode * inode )

Arguments
=========

``inode``
    new inode to unlock


Description
===========

Called when the inode is fully initialised to clear the new state of the
inode and wake up anyone waiting for the inode to finish initialisation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
