.. -*- coding: utf-8; mode: rst -*-

.. _API-mark-buffer-dirty:

=================
mark_buffer_dirty
=================

*man mark_buffer_dirty(9)*

*4.6.0-rc5*

mark a buffer_head as needing writeout


Synopsis
========

.. c:function:: void mark_buffer_dirty( struct buffer_head * bh )

Arguments
=========

``bh``
    the buffer_head to mark dirty


Description
===========

``mark_buffer_dirty`` will set the dirty bit against the buffer, then
set its backing page dirty, then tag the page as dirty in its
address_space's radix tree and then attach the address_space's inode
to its superblock's dirty inode list.

``mark_buffer_dirty`` is atomic. It takes
bh->b_page->mapping->private_lock, mapping->tree_lock and
mapping->host->i_lock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
