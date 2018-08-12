.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/async_tx/async_pq.c

.. _`do_async_gen_syndrome`:

do_async_gen_syndrome
=====================

.. c:function:: __async_inline struct dma_async_tx_descriptor *do_async_gen_syndrome(struct dma_chan *chan, const unsigned char *scfs, int disks, struct dmaengine_unmap_data *unmap, enum dma_ctrl_flags dma_flags, struct async_submit_ctl *submit)

    asynchronously calculate P and/or Q

    :param struct dma_chan \*chan:
        *undescribed*

    :param const unsigned char \*scfs:
        *undescribed*

    :param int disks:
        *undescribed*

    :param struct dmaengine_unmap_data \*unmap:
        *undescribed*

    :param enum dma_ctrl_flags dma_flags:
        *undescribed*

    :param struct async_submit_ctl \*submit:
        *undescribed*

.. _`do_sync_gen_syndrome`:

do_sync_gen_syndrome
====================

.. c:function:: void do_sync_gen_syndrome(struct page **blocks, unsigned int offset, int disks, size_t len, struct async_submit_ctl *submit)

    synchronously calculate a raid6 syndrome

    :param struct page \*\*blocks:
        *undescribed*

    :param unsigned int offset:
        *undescribed*

    :param int disks:
        *undescribed*

    :param size_t len:
        *undescribed*

    :param struct async_submit_ctl \*submit:
        *undescribed*

.. _`async_gen_syndrome`:

async_gen_syndrome
==================

.. c:function:: struct dma_async_tx_descriptor *async_gen_syndrome(struct page **blocks, unsigned int offset, int disks, size_t len, struct async_submit_ctl *submit)

    asynchronously calculate a raid6 syndrome

    :param struct page \*\*blocks:
        source blocks from idx 0..disks-3, P \ ````\  disks-2 and Q \ ````\  disks-1

    :param unsigned int offset:
        common offset into each block (src and dest) to start transaction

    :param int disks:
        number of blocks (including missing P or Q, see below)

    :param size_t len:
        length of operation in bytes

    :param struct async_submit_ctl \*submit:
        submission/completion modifiers

.. _`async_gen_syndrome.general-note`:

General note
------------

This routine assumes a field of GF(2^8) with a
primitive polynomial of 0x11d and a generator of {02}.

'disks' note: callers can optionally omit either P or Q (but not
both) from the calculation by setting blocks[disks-2] or
blocks[disks-1] to NULL.  When P or Q is omitted 'len' must be <=
PAGE_SIZE as a temporary buffer of this size is used in the
synchronous path.  'disks' always accounts for both destination
buffers.  If any source buffers (blocks[i] where i < disks - 2) are
set to NULL those buffers will be replaced with the raid6_zero_page
in the synchronous path and omitted in the hardware-asynchronous
path.

.. _`async_syndrome_val`:

async_syndrome_val
==================

.. c:function:: struct dma_async_tx_descriptor *async_syndrome_val(struct page **blocks, unsigned int offset, int disks, size_t len, enum sum_check_flags *pqres, struct page *spare, struct async_submit_ctl *submit)

    asynchronously validate a raid6 syndrome

    :param struct page \*\*blocks:
        source blocks from idx 0..disks-3, P \ ````\  disks-2 and Q \ ````\  disks-1

    :param unsigned int offset:
        common offset into each block (src and dest) to start transaction

    :param int disks:
        number of blocks (including missing P or Q, see below)

    :param size_t len:
        length of operation in bytes

    :param enum sum_check_flags \*pqres:
        on val failure SUM_CHECK_P_RESULT and/or SUM_CHECK_Q_RESULT are set

    :param struct page \*spare:
        temporary result buffer for the synchronous case

    :param struct async_submit_ctl \*submit:
        submission / completion modifiers

.. _`async_syndrome_val.description`:

Description
-----------

The same notes from async_gen_syndrome apply to the 'blocks',
and 'disks' parameters of this routine.  The synchronous path
requires a temporary result buffer and submit->scribble to be
specified.

.. This file was automatic generated / don't edit.

