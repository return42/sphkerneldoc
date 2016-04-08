
.. _API-phy-attach-direct:

=================
phy_attach_direct
=================

*man phy_attach_direct(9)*

*4.6.0-rc1*

attach a network device to a given PHY device pointer


Synopsis
========

.. c:function:: int phy_attach_direct( struct net_device * dev, struct phy_device * phydev, u32 flags, phy_interface_t interface )

Arguments
=========

``dev``
    network device to attach

``phydev``
    Pointer to phy_device to attach

``flags``
    PHY device's dev_flags

``interface``
    PHY device's interface


Description
===========

Called by drivers to attach to a particular PHY device. The phy_device is found, and properly hooked up to the phy_driver. If no driver is attached, then a generic driver is
used. The phy_device is given a ptr to the attaching device, and given a callback for link status change. The phy_device is returned to the attaching driver. This function takes
a reference on the phy device.
