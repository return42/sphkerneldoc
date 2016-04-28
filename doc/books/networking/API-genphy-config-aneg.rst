.. -*- coding: utf-8; mode: rst -*-

.. _API-genphy-config-aneg:

==================
genphy_config_aneg
==================

*man genphy_config_aneg(9)*

*4.6.0-rc5*

restart auto-negotiation or write BMCR


Synopsis
========

.. c:function:: int genphy_config_aneg( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

If auto-negotiation is enabled, we configure the advertising, and then
restart auto-negotiation. If it is not enabled, then we write the BMCR.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
