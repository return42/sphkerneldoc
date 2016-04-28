.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-buf-end-cpu-access:

======================
dma_buf_end_cpu_access
======================

*man dma_buf_end_cpu_access(9)*

*4.6.0-rc5*

Must be called after accessing a dma_buf from the cpu in the kernel
context. Calls end_cpu_access to allow exporter-specific actions.
Coherency is only guaranteed in the specified range for the specified
access direction.


Synopsis
========

.. c:function:: int dma_buf_end_cpu_access( struct dma_buf * dmabuf, enum dma_data_direction direction )

Arguments
=========

``dmabuf``
    [in] buffer to complete cpu access for.

``direction``
    [in] length of range for cpu access.


Description
===========

Can return negative error values, returns 0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
