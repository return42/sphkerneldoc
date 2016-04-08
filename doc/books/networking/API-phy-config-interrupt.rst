
.. _API-phy-config-interrupt:

====================
phy_config_interrupt
====================

*man phy_config_interrupt(9)*

*4.6.0-rc1*

configure the PHY device for the requested interrupts


Synopsis
========

.. c:function:: int phy_config_interrupt( struct phy_device * phydev, u32 interrupts )

Arguments
=========

``phydev``
    the phy_device struct

``interrupts``
    interrupt flags to configure for this ``phydev``


Description
===========

Returns 0 on success or < 0 on error.
