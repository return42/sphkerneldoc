.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-stop-tx:

===========
hsi_stop_tx
===========

*man hsi_stop_tx(9)*

*4.6.0-rc5*

Signal the port that the client no longer wants to transmit


Synopsis
========

.. c:function:: int hsi_stop_tx( struct hsi_client * cl )

Arguments
=========

``cl``
    Pointer to the HSI client


Description
===========

Return -errno on failure, 0 on success


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
