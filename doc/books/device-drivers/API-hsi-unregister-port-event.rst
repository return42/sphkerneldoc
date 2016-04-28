.. -*- coding: utf-8; mode: rst -*-

.. _API-hsi-unregister-port-event:

=========================
hsi_unregister_port_event
=========================

*man hsi_unregister_port_event(9)*

*4.6.0-rc5*

Stop receiving port events for a client


Synopsis
========

.. c:function:: int hsi_unregister_port_event( struct hsi_client * cl )

Arguments
=========

``cl``
    HSI client that wants to stop receiving port events


Description
===========

Clients should call this function before releasing their associated
port.

Returns -errno on error, or 0 on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
