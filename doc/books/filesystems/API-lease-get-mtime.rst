.. -*- coding: utf-8; mode: rst -*-

.. _API-lease-get-mtime:

===============
lease_get_mtime
===============

*man lease_get_mtime(9)*

*4.6.0-rc5*

get the last modified time of an inode


Synopsis
========

.. c:function:: void lease_get_mtime( struct inode * inode, struct timespec * time )

Arguments
=========

``inode``
    the inode

``time``
    pointer to a timespec which will contain the last modified time


Description
===========

This is to force NFS clients to flush their caches for files with
exclusive leases. The justification is that if someone has an exclusive
lease, then they could be modifying it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
