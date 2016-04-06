
.. _API-hsi-flush:

=========
hsi_flush
=========

*man hsi_flush(9)*

*4.6.0-rc1*

Flush all pending transactions on the client's port


Synopsis
========

.. c:function:: int hsi_flush( struct hsi_client * cl )

Arguments
=========

``cl``
    Pointer to the HSI client


Description
===========

This function will destroy all pending hsi_msg in the port and reset the HW port so it is ready to receive and transmit from a clean state.

Return -errno on failure, 0 on success
