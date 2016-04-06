
.. _API-hsi-async-write:

===============
hsi_async_write
===============

*man hsi_async_write(9)*

*4.6.0-rc1*

Submit a write transfer


Synopsis
========

.. c:function:: int hsi_async_write( struct hsi_client * cl, struct hsi_msg * msg )

Arguments
=========

``cl``
    Pointer to the HSI client

``msg``
    HSI message descriptor of the transfer


Description
===========

Return -errno on failure, 0 on success
