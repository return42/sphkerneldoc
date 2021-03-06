.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fwserial/dma_fifo.c

.. _`dma_fifo_init`:

dma_fifo_init
=============

.. c:function:: void dma_fifo_init(struct dma_fifo *fifo)

    initialize the fifo to a valid but inoperative state

    :param fifo:
        address of in-place "struct dma_fifo" object
    :type fifo: struct dma_fifo \*

.. _`dma_fifo_alloc`:

dma_fifo_alloc
==============

.. c:function:: int dma_fifo_alloc(struct dma_fifo *fifo, int size, unsigned int align, int tx_limit, int open_limit, gfp_t gfp_mask)

    initialize and allocate dma_fifo

    :param fifo:
        address of in-place "struct dma_fifo" object
    :type fifo: struct dma_fifo \*

    :param size:
        'apparent' size, in bytes, of fifo
    :type size: int

    :param align:
        dma alignment to maintain (should be at least cpu cache alignment),
        must be power of 2
    :type align: unsigned int

    :param tx_limit:
        maximum # of bytes transmissible per dma (rounded down to
        multiple of alignment, but at least align size)
    :type tx_limit: int

    :param open_limit:
        maximum # of outstanding dma transactions allowed
    :type open_limit: int

    :param gfp_mask:
        get_free_pages mask, passed to \ :c:func:`kmalloc`\ 
    :type gfp_mask: gfp_t

.. _`dma_fifo_alloc.description`:

Description
-----------

The 'apparent' size will be rounded up to next greater aligned size.
Returns 0 if no error, otherwise an error code

.. _`dma_fifo_free`:

dma_fifo_free
=============

.. c:function:: void dma_fifo_free(struct dma_fifo *fifo)

    frees the fifo

    :param fifo:
        address of in-place "struct dma_fifo" to free
    :type fifo: struct dma_fifo \*

.. _`dma_fifo_free.description`:

Description
-----------

Also reinits the fifo to a valid but inoperative state. This
allows the fifo to be reused with a different target requiring
different fifo parameters.

.. _`dma_fifo_reset`:

dma_fifo_reset
==============

.. c:function:: void dma_fifo_reset(struct dma_fifo *fifo)

    dumps the fifo contents and reinits for reuse

    :param fifo:
        address of in-place "struct dma_fifo" to reset
    :type fifo: struct dma_fifo \*

.. _`dma_fifo_in`:

dma_fifo_in
===========

.. c:function:: int dma_fifo_in(struct dma_fifo *fifo, const void *src, int n)

    copies data into the fifo

    :param fifo:
        address of in-place "struct dma_fifo" to write to
    :type fifo: struct dma_fifo \*

    :param src:
        buffer to copy from
    :type src: const void \*

    :param n:
        # of bytes to copy
    :type n: int

.. _`dma_fifo_in.description`:

Description
-----------

Returns the # of bytes actually copied, which can be less than requested if
the fifo becomes full. If < 0, return is error code.

.. _`dma_fifo_out_pend`:

dma_fifo_out_pend
=================

.. c:function:: int dma_fifo_out_pend(struct dma_fifo *fifo, struct dma_pending *pended)

    gets address/len of next avail read and marks as pended

    :param fifo:
        address of in-place "struct dma_fifo" to read from
    :type fifo: struct dma_fifo \*

    :param pended:
        address of structure to fill with read address/len
        The data/len fields will be NULL/0 if no dma is pended.
    :type pended: struct dma_pending \*

.. _`dma_fifo_out_pend.description`:

Description
-----------

Returns the # of used bytes remaining in fifo (ie, if > 0, more data
remains in the fifo that was not pended). If < 0, return is error code.

.. _`dma_fifo_out_complete`:

dma_fifo_out_complete
=====================

.. c:function:: int dma_fifo_out_complete(struct dma_fifo *fifo, struct dma_pending *complete)

    marks pended dma as completed

    :param fifo:
        address of in-place "struct dma_fifo" which was read from
    :type fifo: struct dma_fifo \*

    :param complete:
        address of structure for previously pended dma to mark completed
    :type complete: struct dma_pending \*

.. This file was automatic generated / don't edit.

