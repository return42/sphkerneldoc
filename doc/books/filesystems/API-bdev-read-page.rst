.. -*- coding: utf-8; mode: rst -*-

.. _API-bdev-read-page:

==============
bdev_read_page
==============

*man bdev_read_page(9)*

*4.6.0-rc5*

Start reading a page from a block device


Synopsis
========

.. c:function:: int bdev_read_page( struct block_device * bdev, sector_t sector, struct page * page )

Arguments
=========

``bdev``
    The device to read the page from

``sector``
    The offset on the device to read the page to (need not be aligned)

``page``
    The page to read


Description
===========

On entry, the page should be locked. It will be unlocked when the page
has been read. If the block driver implements rw_page synchronously,
that will be true on exit from this function, but it need not be.

Errors returned by this function are usually “soft”, eg out of memory,
or queue full; callers should try a different route to read this page
rather than propagate an error back up the stack.


Return
======

negative errno if an error occurs, 0 if submission was successful.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
