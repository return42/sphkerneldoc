.. -*- coding: utf-8; mode: rst -*-

.. _API-bdev-write-page:

===============
bdev_write_page
===============

*man bdev_write_page(9)*

*4.6.0-rc5*

Start writing a page to a block device


Synopsis
========

.. c:function:: int bdev_write_page( struct block_device * bdev, sector_t sector, struct page * page, struct writeback_control * wbc )

Arguments
=========

``bdev``
    The device to write the page to

``sector``
    The offset on the device to write the page to (need not be aligned)

``page``
    The page to write

``wbc``
    The writeback_control for the write


Description
===========

On entry, the page should be locked and not currently under writeback.
On exit, if the write started successfully, the page will be unlocked
and under writeback. If the write failed already (eg the driver failed
to queue the page to the device), the page will still be locked. If the
caller is a ->writepage implementation, it will need to unlock the page.

Errors returned by this function are usually “soft”, eg out of memory,
or queue full; callers should try a different route to write this page
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
