.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-flush:

=========
hsi_flush
=========

*man hsi_flush(9)*

*4.6.0-rc5*

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

This function will destroy all pending hsi_msg in the port and reset
the HW port so it is ready to receive and transmit from a clean state.

Return -errno on failure, 0 on success


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
