
.. _API-dma-buf-fd:

==========
dma_buf_fd
==========

*man dma_buf_fd(9)*

*4.6.0-rc1*

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
