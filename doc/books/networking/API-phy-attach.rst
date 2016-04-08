
.. _API-phy-attach:

==========
phy_attach
==========

*man phy_attach(9)*

*4.6.0-rc1*

attach a network device to a particular PHY device


Synopsis
========

.. c:function:: struct phy_device ⋆ phy_attach( struct net_device * dev, const char * bus_id, phy_interface_t interface )

Arguments
=========

``dev``
    network device to attach

``bus_id``
    Bus ID of PHY device to attach

``interface``
    PHY device's interface


Description
===========

Same as ``phy_attach_direct`` except that a PHY bus_id string is passed instead of a pointer to a struct phy_device.
