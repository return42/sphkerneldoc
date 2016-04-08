
.. _API-genphy-update-link:

==================
genphy_update_link
==================

*man genphy_update_link(9)*

*4.6.0-rc1*

update link status in ``phydev``


Synopsis
========

.. c:function:: int genphy_update_link( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Update the value in phydev->link to reflect the current link value. In order to do this, we need to read the status register twice, keeping the second value.
