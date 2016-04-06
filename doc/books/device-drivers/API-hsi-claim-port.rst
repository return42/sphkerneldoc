
.. _API-hsi-claim-port:

==============
hsi_claim_port
==============

*man hsi_claim_port(9)*

*4.6.0-rc1*

Claim the HSI client's port


Synopsis
========

.. c:function:: int hsi_claim_port( struct hsi_client * cl, unsigned int share )

Arguments
=========

``cl``
    HSI client that wants to claim its port

``share``
    Flag to indicate if the client wants to share the port or not.


Description
===========

Returns -errno on failure, 0 on success.
