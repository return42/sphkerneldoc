.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-claim-port:

==============
hsi_claim_port
==============

*man hsi_claim_port(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
