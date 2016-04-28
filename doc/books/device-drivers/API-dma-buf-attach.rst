.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-buf-attach:

==============
dma_buf_attach
==============

*man dma_buf_attach(9)*

*4.6.0-rc5*

Add the device to dma_buf's attachments list; optionally, calls
``attach`` of dma_buf_ops to allow device-specific attach
functionality


Synopsis
========

.. c:function:: struct dma_buf_attachment * dma_buf_attach( struct dma_buf * dmabuf, struct device * dev )

Arguments
=========

``dmabuf``
    [in] buffer to attach device to.

``dev``
    [in] device to be attached.


Description
===========

Returns struct dma_buf_attachment * for this attachment; returns
ERR_PTR on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
