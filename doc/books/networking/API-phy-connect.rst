.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-connect:

===========
phy_connect
===========

*man phy_connect(9)*

*4.6.0-rc5*

connect an ethernet device to a PHY device


Synopsis
========

.. c:function:: struct phy_device * phy_connect( struct net_device * dev, const char * bus_id, void (*handler) struct net_device *, phy_interface_t interface )

Arguments
=========

``dev``
    the network device to connect

``bus_id``
    the id string of the PHY device to connect

``handler``
    callback function for state change notifications

``interface``
    PHY device's interface


Description
===========

Convenience function for connecting ethernet devices to PHY devices. The
default behavior is for the PHY infrastructure to handle everything, and
only notify the connected driver when the link status changes. If you
don't want, or can't use the provided functionality, you may choose to
call only the subset of functions which provide the desired
functionality.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
