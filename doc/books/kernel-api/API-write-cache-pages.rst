.. -*- coding: utf-8; mode: rst -*-

.. _API-write-cache-pages:

=================
write_cache_pages
=================

*man write_cache_pages(9)*

*4.6.0-rc5*

walk the list of dirty pages of the given address space and write all of
them.


Synopsis
========

.. c:function:: int write_cache_pages( struct address_space * mapping, struct writeback_control * wbc, writepage_t writepage, void * data )

Arguments
=========

``mapping``
    address space structure to write

``wbc``
    subtract the number of written pages from * ``wbc``->nr_to_write

``writepage``
    function called for each page

``data``
    data passed to writepage function


Description
===========

If a page is already under I/O, ``write_cache_pages`` skips it, even if
it's dirty. This is desirable behaviour for memory-cleaning writeback,
but it is INCORRECT for data-integrity system calls such as ``fsync``.
``fsync`` and ``msync`` need to guarantee that all the data which was
dirty at the time the call was made get new I/O started against them. If
wbc->sync_mode is WB_SYNC_ALL then we were called for data integrity
and we must wait for existing IO to complete.

To avoid livelocks (when other process dirties new pages), we first tag
pages which should be written back with TOWRITE tag and only then start
writing them. For data-integrity sync we have to be careful so that we
do not miss some pages (e.g., because some other process has cleared
TOWRITE tag we set). The rule we follow is that TOWRITE tag can be
cleared only by the process clearing the DIRTY tag (and submitting the
page for IO).


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
