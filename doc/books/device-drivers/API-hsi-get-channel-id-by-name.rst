.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-get-channel-id-by-name:

==========================
hsi_get_channel_id_by_name
==========================

*man hsi_get_channel_id_by_name(9)*

*4.6.0-rc5*

acquire channel id by channel name


Synopsis
========

.. c:function:: int hsi_get_channel_id_by_name( struct hsi_client * cl, char * name )

Arguments
=========

``cl``
    HSI client, which uses the channel

``name``
    name the channel is known under


Description
===========

Clients can call this function to get the hsi channel ids similar to
requesting IRQs or GPIOs by name. This function assumes the same channel
configuration is used for RX and TX.

Returns -errno on error or channel id on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
