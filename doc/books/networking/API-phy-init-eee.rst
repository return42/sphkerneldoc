
.. _API-phy-init-eee:

============
phy_init_eee
============

*man phy_init_eee(9)*

*4.6.0-rc1*

init and check the EEE feature


Synopsis
========

.. c:function:: int phy_init_eee( struct phy_device * phydev, bool clk_stop_enable )

Arguments
=========

``phydev``
    target phy_device struct

``clk_stop_enable``
    PHY may stop the clock during LPI


Description
===========

it checks if the Energy-Efficient Ethernet (EEE) is supported by looking at the MMD registers 3.20 and 7.60/61 and it programs the MMD register 3.0 setting the “Clock stop enable”
bit if required.
