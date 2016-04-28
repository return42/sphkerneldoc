.. -*- coding: utf-8; mode: rst -*-

.. _API-genphy-config-advert:

====================
genphy_config_advert
====================

*man genphy_config_advert(9)*

*4.6.0-rc5*

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

Writes MII_ADVERTISE with the appropriate values, after sanitizing the
values to make sure we only advertise what is supported. Returns < 0 on
error, 0 if the PHY's advertisement hasn't changed, and > 0 if it has
changed.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
