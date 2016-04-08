
.. _API-genphy-config-advert:

====================
genphy_config_advert
====================

*man genphy_config_advert(9)*

*4.6.0-rc1*

sanitize and advertise auto-negotiation parameters


Synopsis
========

.. c:function:: int genphy_config_advert( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Writes MII_ADVERTISE with the appropriate values, after sanitizing the values to make sure we only advertise what is supported. Returns < 0 on error, 0 if the PHY's advertisement
hasn't changed, and > 0 if it has changed.
