.. -*- coding: utf-8; mode: rst -*-

===========
async_xor.c
===========


.. _`async_xor`:

async_xor
=========

.. c:function:: struct dma_async_tx_descriptor *async_xor (struct page *dest, struct page **src_list, unsigned int offset, int src_cnt, size_t len, struct async_submit_ctl *submit)

    attempt to xor a set of blocks with a dma engine.

    :param struct page \*dest:
        destination page

    :param struct page \*\*src_list:
        array of source pages

    :param unsigned int offset:
        common src/dst offset to start transaction

    :param int src_cnt:
        number of source pages

    :param size_t len:
        length in bytes

    :param struct async_submit_ctl \*submit:
        submission / completion modifiers



.. _`async_xor.honored-flags`:

honored flags
-------------

ASYNC_TX_ACK, ASYNC_TX_XOR_ZERO_DST, ASYNC_TX_XOR_DROP_DST

xor_blocks always uses the dest as a source so the
ASYNC_TX_XOR_ZERO_DST flag must be set to not include dest data in
the calculation.  The assumption with dma eninges is that they only
use the destination buffer as a source when it is explicity specified
in the source list.



.. _`async_xor.src_list-note`:

src_list note
-------------

if the dest is also a source it must be at index zero.
The contents of this array will be overwritten if a scribble region
is not specified.



.. _`async_xor_val`:

async_xor_val
=============

.. c:function:: struct dma_async_tx_descriptor *async_xor_val (struct page *dest, struct page **src_list, unsigned int offset, int src_cnt, size_t len, enum sum_check_flags *result, struct async_submit_ctl *submit)

    attempt a xor parity check with a dma engine.

    :param struct page \*dest:
        destination page used if the xor is performed synchronously

    :param struct page \*\*src_list:
        array of source pages

    :param unsigned int offset:
        offset in pages to start transaction

    :param int src_cnt:
        number of source pages

    :param size_t len:
        length in bytes

    :param enum sum_check_flags \*result:
        0 if sum == 0 else non-zero

    :param struct async_submit_ctl \*submit:
        submission / completion modifiers



.. _`async_xor_val.honored-flags`:

honored flags
-------------

ASYNC_TX_ACK



.. _`async_xor_val.src_list-note`:

src_list note
-------------

if the dest is also a source it must be at index zero.
The contents of this array will be overwritten if a scribble region
is not specified.

