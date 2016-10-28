.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/dma/virt-dma.c

.. _`vchan_tx_desc_free`:

vchan_tx_desc_free
==================

.. c:function:: int vchan_tx_desc_free(struct dma_async_tx_descriptor *tx)

    free a reusable descriptor

    :param struct dma_async_tx_descriptor \*tx:
        the transfer

.. _`vchan_tx_desc_free.description`:

Description
-----------

This function frees a previously allocated reusable descriptor. The only
other way is to clear the DMA_CTRL_REUSE flag and submit one last time the
transfer.

Returns 0 upon success

.. This file was automatic generated / don't edit.

