.. -*- coding: utf-8; mode: rst -*-

=======
mpage.c
=======

.. _`mpage_readpages`:

mpage_readpages
===============

.. c:function:: int mpage_readpages (struct address_space *mapping, struct list_head *pages, unsigned nr_pages, get_block_t get_block)

    populate an address space with some pages & start reads against them

    :param struct address_space \*mapping:
        the address_space

    :param struct list_head \*pages:
        The address of a list_head which contains the target pages.  These
        pages have their ->index populated and are otherwise uninitialised.
        The page at ``pages``\ ->prev has the lowest file offset, and reads should be
        issued in ``pages``\ ->prev to ``pages``\ ->next order.

    :param unsigned nr_pages:
        The number of pages at \*\ ``pages``

    :param get_block_t get_block:
        The filesystem's block mapper function.


.. _`mpage_readpages.description`:

Description
-----------

This function walks the pages and the blocks within each page, building and
emitting large BIOs.

If anything unusual happens, such as:

- encountering a page which has buffers
- encountering a page which has a non-hole after a hole
- encountering a page with non-contiguous blocks

then this code just gives up and calls the buffer_head-based read function.
It does handle a page which has holes at the end - that is a common case:
the end-of-file on blocksize < PAGE_SIZE setups.

BH_Boundary explanation:

There is a problem.  The mpage read code assembles several pages, gets all
their disk mappings, and then submits them all.  That's fine, but obtaining
the disk mappings may require I/O.  Reads of indirect blocks, for example.

So an mpage read of the first 16 blocks of an ext2 file will cause I/O to be
submitted in the following order::

        12 0 1 2 3 4 5 6 7 8 9 10 11 13 14 15 16

because the indirect block has to be read to get the mappings of blocks
13,14,15,16.  Obviously, this impacts performance.

So what we do it to allow the filesystem's :c:func:`get_block` function to set
BH_Boundary when it maps block 11.  BH_Boundary says: mapping of the block
after this one will require I/O against a block which is probably close to
this one.  So you should push what I/O you have currently accumulated.

This all causes the disk requests to be issued in the correct order.


.. _`mpage_writepages`:

mpage_writepages
================

.. c:function:: int mpage_writepages (struct address_space *mapping, struct writeback_control *wbc, get_block_t get_block)

    walk the list of dirty pages of the given address space & writepage() all of them

    :param struct address_space \*mapping:
        address space structure to write

    :param struct writeback_control \*wbc:
        subtract the number of written pages from \*\ ``wbc``\ ->nr_to_write

    :param get_block_t get_block:
        the filesystem's block mapper function.::

                    If this is NULL then use a_ops->writepage.  Otherwise, go
                    direct-to-BIO.


.. _`mpage_writepages.description`:

Description
-----------

This is a library function, which implements the :c:func:`writepages`
address_space_operation.

If a page is already under I/O, :c:func:`generic_writepages` skips it, even
if it's dirty.  This is desirable behaviour for memory-cleaning writeback,
but it is INCORRECT for data-integrity system calls such as :c:func:`fsync`.  :c:func:`fsync`
and :c:func:`msync` need to guarantee that all the data which was dirty at the time
the call was made get new I/O started against them.  If wbc->sync_mode is
WB_SYNC_ALL then we were called for data integrity and we must wait for
existing IO to complete.

