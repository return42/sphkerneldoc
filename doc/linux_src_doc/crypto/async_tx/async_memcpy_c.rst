.. -*- coding: utf-8; mode: rst -*-

==============
async_memcpy.c
==============


.. _`async_memcpy`:

async_memcpy
============

.. c:function:: struct dma_async_tx_descriptor *async_memcpy (struct page *dest, struct page *src, unsigned int dest_offset, unsigned int src_offset, size_t len, struct async_submit_ctl *submit)

    attempt to copy memory with a dma engine.

    :param struct page \*dest:
        destination page

    :param struct page \*src:
        src page

    :param unsigned int dest_offset:
        offset into 'dest' to start transaction

    :param unsigned int src_offset:
        offset into 'src' to start transaction

    :param size_t len:
        length in bytes

    :param struct async_submit_ctl \*submit:
        submission / completion modifiers



.. _`async_memcpy.honored-flags`:

honored flags
-------------

ASYNC_TX_ACK

