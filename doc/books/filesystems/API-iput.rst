.. -*- coding: utf-8; mode: rst -*-

.. _API-iput:

====
iput
====

*man iput(9)*

*4.6.0-rc5*

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

Puts an inode, dropping its usage count. If the inode use count hits
zero, the inode is then freed and may also be destroyed.

Consequently, ``iput`` can sleep.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
