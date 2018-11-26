.. -*- coding: utf-8; mode: rst -*-
.. src-file: crypto/async_tx/async_memcpy.c

.. _`async_memcpy`:

async_memcpy
============

.. c:function:: struct dma_async_tx_descriptor *async_memcpy(struct page *dest, struct page *src, unsigned int dest_offset, unsigned int src_offset, size_t len, struct async_submit_ctl *submit)

    attempt to copy memory with a dma engine.

    :param dest:
        destination page
    :type dest: struct page \*

    :param src:
        src page
    :type src: struct page \*

    :param dest_offset:
        offset into 'dest' to start transaction
    :type dest_offset: unsigned int

    :param src_offset:
        offset into 'src' to start transaction
    :type src_offset: unsigned int

    :param len:
        length in bytes
    :type len: size_t

    :param submit:
        submission / completion modifiers
    :type submit: struct async_submit_ctl \*

.. _`async_memcpy.honored-flags`:

honored flags
-------------

ASYNC_TX_ACK

.. This file was automatic generated / don't edit.

