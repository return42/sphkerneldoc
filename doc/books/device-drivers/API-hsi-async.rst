
.. _API-hsi-async:

=========
hsi_async
=========

*man hsi_async(9)*

*4.6.0-rc1*

Submit an HSI transfer to the controller


Synopsis
========

.. c:function:: int hsi_async( struct hsi_client * cl, struct hsi_msg * msg )

Arguments
=========

``cl``
    HSI client sending the transfer

``msg``
    The HSI transfer passed to controller


Description
===========

The HSI message must have the channel, ttype, complete and destructor fields set beforehand. If nents > 0 then the client has to initialize also the scatterlists to point to the
buffers to write to or read from.

HSI controllers relay on pre-allocated buffers from their clients and they do not allocate buffers on their own.

Once the HSI message transfer finishes, the HSI controller calls the complete callback with the status and actual_len fields of the HSI message updated. The complete callback can
be called before returning from hsi_async.

Returns -errno on failure or 0 on success
