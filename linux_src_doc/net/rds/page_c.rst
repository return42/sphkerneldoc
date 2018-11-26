.. -*- coding: utf-8; mode: rst -*-
.. src-file: net/rds/page.c

.. _`rds_page_remainder_alloc`:

rds_page_remainder_alloc
========================

.. c:function:: int rds_page_remainder_alloc(struct scatterlist *scat, unsigned long bytes, gfp_t gfp)

    build up regions of a message.

    :param scat:
        Scatter list for message
    :type scat: struct scatterlist \*

    :param bytes:
        the number of bytes needed.
    :type bytes: unsigned long

    :param gfp:
        the waiting behaviour of the allocation
    :type gfp: gfp_t

.. _`rds_page_remainder_alloc.description`:

Description
-----------

\ ``gfp``\  is always ored with \__GFP_HIGHMEM.  Callers must be prepared to
kmap the pages, etc.

If \ ``bytes``\  is at least a full page then this just returns a page from
\ :c:func:`alloc_page`\ .

If \ ``bytes``\  is a partial page then this stores the unused region of the
page in a per-cpu structure.  Future partial-page allocations may be
satisfied from that cached region.  This lets us waste less memory on
small allocations with minimal complexity.  It works because the transmit
path passes read-only page regions down to devices.  They hold a page
reference until they are done with the region.

.. This file was automatic generated / don't edit.

