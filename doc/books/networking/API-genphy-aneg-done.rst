
.. _API-genphy-aneg-done:

================
genphy_aneg_done
================

*man genphy_aneg_done(9)*

*4.6.0-rc1*

return auto-negotiation status


Synopsis
========

.. c:function:: int genphy_aneg_done( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Reads the status register and returns 0 either if auto-negotiation is incomplete, or if there was an error. Returns BMSR_ANEGCOMPLETE if auto-negotiation is done.
