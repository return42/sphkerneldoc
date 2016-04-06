
.. _API-hsi-async-read:

==============
hsi_async_read
==============

*man hsi_async_read(9)*

*4.6.0-rc1*

Submit a read transfer


Synopsis
========

.. c:function:: int hsi_async_read( struct hsi_client * cl, struct hsi_msg * msg )

Arguments
=========

``cl``
    Pointer to the HSI client

``msg``
    HSI message descriptor of the transfer


Description
===========

Return -errno on failure, 0 on success
