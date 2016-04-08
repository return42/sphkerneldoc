
.. _API-phy-aneg-done:

=============
phy_aneg_done
=============

*man phy_aneg_done(9)*

*4.6.0-rc1*

return auto-negotiation status


Synopsis
========

.. c:function:: int phy_aneg_done( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Return the auto-negotiation status from this ``phydev`` Returns > 0 on success or < 0 on error. 0 means that auto-negotiation is still pending.
