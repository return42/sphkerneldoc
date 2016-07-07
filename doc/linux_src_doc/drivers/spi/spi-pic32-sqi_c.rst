.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/spi/spi-pic32-sqi.c

.. _`ring_desc`:

struct ring_desc
================

.. c:type:: struct ring_desc

    Representation of SQI ring descriptor

.. _`ring_desc.definition`:

Definition
----------

.. code-block:: c

    struct ring_desc {
        struct list_head list;
        struct buf_desc *bd;
        dma_addr_t bd_dma;
        u32 xfer_len;
    }

.. _`ring_desc.members`:

Members
-------

list
    list element to add to free or used list.

bd
    PESQI controller buffer descriptor

bd_dma
    DMA address of PESQI controller buffer descriptor

xfer_len
    transfer length

.. This file was automatic generated / don't edit.

