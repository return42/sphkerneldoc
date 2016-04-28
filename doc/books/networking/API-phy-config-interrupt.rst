.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-config-interrupt:

====================
phy_config_interrupt
====================

*man phy_config_interrupt(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
