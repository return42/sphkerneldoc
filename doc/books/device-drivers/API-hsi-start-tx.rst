
.. _API-hsi-start-tx:

============
hsi_start_tx
============

*man hsi_start_tx(9)*

*4.6.0-rc1*

Signal the port that the client wants to start a TX


Synopsis
========

.. c:function:: int hsi_start_tx( struct hsi_client * cl )

Arguments
=========

``cl``
    Pointer to the HSI client


Description
===========

Return -errno on failure, 0 on success
