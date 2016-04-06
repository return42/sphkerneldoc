
.. _API-hsi-register-port-event:

=======================
hsi_register_port_event
=======================

*man hsi_register_port_event(9)*

*4.6.0-rc1*

Register a client to receive port events


Synopsis
========

.. c:function:: int hsi_register_port_event( struct hsi_client * cl, void (*handler) struct hsi_client *, unsigned long )

Arguments
=========

``cl``
    HSI client that wants to receive port events

``handler``
    Event handler callback


Description
===========

Clients should register a callback to be able to receive events from the ports. Registration should happen after claiming the port. The handler can be called in interrupt context.

Returns -errno on error, or 0 on success.
