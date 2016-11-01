.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/crypto/caam/caampkc.c

.. _`caam_read_raw_data`:

caam_read_raw_data
==================

.. c:function:: u8 *caam_read_raw_data(const u8 *buf, size_t *nbytes)

    Read a raw byte stream as a positive integer. The function skips buffer's leading zeros, copies the remained data to a buffer allocated in the GFP_DMA \| GFP_KERNEL zone and returns the address of the new buffer.

    :param const u8 \*buf:
        The data to read

    :param size_t \*nbytes:
        The amount of data to read

.. This file was automatic generated / don't edit.

