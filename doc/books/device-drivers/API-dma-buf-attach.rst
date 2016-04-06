
.. _API-dma-buf-attach:

==============
dma_buf_attach
==============

*man dma_buf_attach(9)*

*4.6.0-rc1*

Add the device to dma_buf's attachments list; optionally, calls ``attach`` of dma_buf_ops to allow device-specific attach functionality


Synopsis
========

.. c:function:: struct dma_buf_attachment ⋆ dma_buf_attach( struct dma_buf * dmabuf, struct device * dev )

Arguments
=========

``dmabuf``
    [in] buffer to attach device to.

``dev``
    [in] device to be attached.


Description
===========

Returns struct dma_buf_attachment ⋆ for this attachment; returns ERR_PTR on error.
