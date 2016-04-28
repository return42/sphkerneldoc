.. -*- coding: utf-8; mode: rst -*-

.. _API-block-invalidatepage:

====================
block_invalidatepage
====================

*man block_invalidatepage(9)*

*4.6.0-rc5*

invalidate part or all of a buffer-backed page


Synopsis
========

.. c:function:: void block_invalidatepage( struct page * page, unsigned int offset, unsigned int length )

Arguments
=========

``page``
    the page which is affected

``offset``
    start of the range to invalidate

``length``
    length of the range to invalidate


Description
===========

``block_invalidatepage`` is called when all or part of the page has
become invalidated by a truncate operation.

``block_invalidatepage`` does not have to release all buffers, but it
must ensure that no dirty buffer is left outside ``offset`` and that no
I/O is underway against any of the blocks which are outside the
truncation point. Because the caller is about to free (and possibly
reuse) those blocks on-disk.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
