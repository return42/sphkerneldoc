.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/ioat/init.c

.. _`ioat_dma_self_test`:

ioat_dma_self_test
==================

.. c:function:: int ioat_dma_self_test(struct ioatdma_device *ioat_dma)

    Perform a IOAT transaction to verify the HW works.

    :param ioat_dma:
        dma device to be tested
    :type ioat_dma: struct ioatdma_device \*

.. _`ioat_dma_setup_interrupts`:

ioat_dma_setup_interrupts
=========================

.. c:function:: int ioat_dma_setup_interrupts(struct ioatdma_device *ioat_dma)

    setup interrupt handler

    :param ioat_dma:
        ioat dma device
    :type ioat_dma: struct ioatdma_device \*

.. _`ioat_enumerate_channels`:

ioat_enumerate_channels
=======================

.. c:function:: void ioat_enumerate_channels(struct ioatdma_device *ioat_dma)

    find and initialize the device's channels

    :param ioat_dma:
        the ioat dma device to be enumerated
    :type ioat_dma: struct ioatdma_device \*

.. _`ioat_free_chan_resources`:

ioat_free_chan_resources
========================

.. c:function:: void ioat_free_chan_resources(struct dma_chan *c)

    release all the descriptors

    :param c:
        *undescribed*
    :type c: struct dma_chan \*

.. This file was automatic generated / don't edit.

