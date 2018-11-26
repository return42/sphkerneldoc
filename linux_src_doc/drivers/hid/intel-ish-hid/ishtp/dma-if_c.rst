.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/intel-ish-hid/ishtp/dma-if.c

.. _`ishtp_cl_alloc_dma_buf`:

ishtp_cl_alloc_dma_buf
======================

.. c:function:: void ishtp_cl_alloc_dma_buf(struct ishtp_device *dev)

    Allocate DMA RX and TX buffer

    :param dev:
        ishtp device
    :type dev: struct ishtp_device \*

.. _`ishtp_cl_alloc_dma_buf.description`:

Description
-----------

Allocate RX and TX DMA buffer once during bus setup.
It allocates 1MB, RX and TX DMA buffer, which are divided
into slots.

.. _`ishtp_cl_free_dma_buf`:

ishtp_cl_free_dma_buf
=====================

.. c:function:: void ishtp_cl_free_dma_buf(struct ishtp_device *dev)

    Free DMA RX and TX buffer

    :param dev:
        ishtp device
    :type dev: struct ishtp_device \*

.. _`ishtp_cl_free_dma_buf.description`:

Description
-----------

Free DMA buffer when all clients are released. This is
only happens during error path in ISH built in driver
model

.. This file was automatic generated / don't edit.

