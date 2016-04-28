.. -*- coding: utf-8; mode: rst -*-

.. _API-mpage-readpages:

===============
mpage_readpages
===============

*man mpage_readpages(9)*

*4.6.0-rc5*

populate an address space with some pages & start reads against them


Synopsis
========

.. c:function:: int mpage_readpages( struct address_space * mapping, struct list_head * pages, unsigned nr_pages, get_block_t get_block )

Arguments
=========

``mapping``
    the address_space

``pages``
    The address of a list_head which contains the target pages. These
    pages have their ->index populated and are otherwise uninitialised.
    The page at ``pages``->prev has the lowest file offset, and reads
    should be issued in ``pages``->prev to ``pages``->next order.

``nr_pages``
    The number of pages at *\ ``pages``

``get_block``
    The filesystem's block mapper function.


Description
===========

This function walks the pages and the blocks within each page, building
and emitting large BIOs.

If anything unusual happens, such as:

- encountering a page which has buffers - encountering a page which has
a non-hole after a hole - encountering a page with non-contiguous blocks

then this code just gives up and calls the buffer_head-based read
function. It does handle a page which has holes at the end - that is a
common case: the end-of-file on blocksize < PAGE_SIZE setups.


BH_Boundary explanation
=======================

There is a problem. The mpage read code assembles several pages, gets
all their disk mappings, and then submits them all. That's fine, but
obtaining the disk mappings may require I/O. Reads of indirect blocks,
for example.

So an mpage read of the first 16 blocks of an ext2 file will cause I/O
to be


submitted in the following order
================================

12 0 1 2 3 4 5 6 7 8 9 10 11 13 14 15 16

because the indirect block has to be read to get the mappings of blocks
13,14,15,16. Obviously, this impacts performance.

So what we do it to allow the filesystem's ``get_block`` function to set
BH_Boundary when it maps block 11. BH_Boundary says: mapping of the
block after this one will require I/O against a block which is probably
close to this one. So you should push what I/O you have currently
accumulated.

This all causes the disk requests to be issued in the correct order.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
