
.. _API-dma-buf-detach:

==============
dma_buf_detach
==============

*man dma_buf_detach(9)*

*4.6.0-rc1*

Remove the given attachment from dmabuf's attachments list; optionally calls ``detach`` of dma_buf_ops for device-specific detach


Synopsis
========

.. c:function:: void dma_buf_detach( struct dma_buf * dmabuf, struct dma_buf_attachment * attach )

Arguments
=========

``dmabuf``
    [in] buffer to detach from.

``attach``
    [in] attachment to be detached; is free'd after this call.
