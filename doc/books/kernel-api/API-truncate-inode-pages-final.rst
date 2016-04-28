.. -*- coding: utf-8; mode: rst -*-

.. _API-truncate-inode-pages-final:

==========================
truncate_inode_pages_final
==========================

*man truncate_inode_pages_final(9)*

*4.6.0-rc5*

truncate *all* pages before inode dies


Synopsis
========

.. c:function:: void truncate_inode_pages_final( struct address_space * mapping )

Arguments
=========

``mapping``
    mapping to truncate


Description
===========

Called under (and serialized by) inode->i_mutex.

Filesystems have to use this in the .evict_inode path to inform the VM
that this is the final truncate and the inode is going away.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
