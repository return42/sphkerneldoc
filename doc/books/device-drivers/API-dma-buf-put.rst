.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-buf-put:

===========
dma_buf_put
===========

*man dma_buf_put(9)*

*4.6.0-rc5*

decreases refcount of the buffer


Synopsis
========

.. c:function:: void dma_buf_put( struct dma_buf * dmabuf )

Arguments
=========

``dmabuf``
    [in] buffer to reduce refcount of


Description
===========

Uses file's refcounting done implicitly by ``fput``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
