
.. _API-dma-buf-get:

===========
dma_buf_get
===========

*man dma_buf_get(9)*

*4.6.0-rc1*

returns the dma_buf structure related to an fd


Synopsis
========

.. c:function:: struct dma_buf ⋆ dma_buf_get( int fd )

Arguments
=========

``fd``
    [in] fd associated with the dma_buf to be returned


Description
===========

On success, returns the dma_buf structure associated with an fd; uses file's refcounting done by fget to increase refcount. returns ERR_PTR otherwise.
