
.. _API-phy-write-mmd-indirect:

======================
phy_write_mmd_indirect
======================

*man phy_write_mmd_indirect(9)*

*4.6.0-rc1*

writes data to the MMD registers


Synopsis
========

.. c:function:: void phy_write_mmd_indirect( struct phy_device * phydev, int prtad, int devad, u32 data )

Arguments
=========

``phydev``
    The PHY device

``prtad``
    MMD Address

``devad``
    MMD DEVAD

``data``
    data to write in the MMD register


Description
===========

Write data from the MMD registers of the specified phy address.


To write these register we have
===============================

1) Write reg 13 // DEVAD 2) Write reg 14 // MMD Address 3) Write reg 13 // MMD Data Command for MMD DEVAD 3) Write reg 14 // Write MMD data
