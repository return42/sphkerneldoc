.. -*- coding: utf-8; mode: rst -*-

.. _API-dma-buf-fd:

==========
dma_buf_fd
==========

*man dma_buf_fd(9)*

*4.6.0-rc5*

returns a file descriptor for the given dma_buf


Synopsis
========

.. c:function:: int dma_buf_fd( struct dma_buf * dmabuf, int flags )

Arguments
=========

``dmabuf``
    [in] pointer to dma_buf for which fd is required.

``flags``
    [in] flags to give to fd


Description
===========

On success, returns an associated 'fd'. Else, returns error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
