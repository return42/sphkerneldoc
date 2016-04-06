
.. _API-usb-bus-start-enum:

==================
usb_bus_start_enum
==================

*man usb_bus_start_enum(9)*

*4.6.0-rc1*

start immediate enumeration (for OTG)


Synopsis
========

.. c:function:: int usb_bus_start_enum( struct usb_bus * bus, unsigned port_num )

Arguments
=========

``bus``
    the bus (must use hcd framework)

``port_num``
    1-based number of port; usually bus->otg_port


Context
=======

``in_interrupt``


Description
===========

Starts enumeration, with an immediate reset followed later by hub_wq identifying and possibly configuring the device. This is needed by OTG controller drivers, where it helps meet
HNP protocol timing requirements for starting a port reset.


Return
======

0 if successful.
