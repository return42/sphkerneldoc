.. -*- coding: utf-8; mode: rst -*-

.. _API-mpage-writepages:

================
mpage_writepages
================

*man mpage_writepages(9)*

*4.6.0-rc5*

walk the list of dirty pages of the given address space & ``writepage``
all of them


Synopsis
========

.. c:function:: int mpage_writepages( struct address_space * mapping, struct writeback_control * wbc, get_block_t get_block )

Arguments
=========

``mapping``
    address space structure to write

``wbc``
    subtract the number of written pages from * ``wbc``->nr_to_write

``get_block``
    the filesystem's block mapper function. If this is NULL then use
    a_ops->writepage. Otherwise, go direct-to-BIO.


Description
===========

This is a library function, which implements the ``writepages``
address_space_operation.

If a page is already under I/O, ``generic_writepages`` skips it, even if
it's dirty. This is desirable behaviour for memory-cleaning writeback,
but it is INCORRECT for data-integrity system calls such as ``fsync``.
``fsync`` and ``msync`` need to guarantee that all the data which was
dirty at the time the call was made get new I/O started against them. If
wbc->sync_mode is WB_SYNC_ALL then we were called for data integrity
and we must wait for existing IO to complete.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
