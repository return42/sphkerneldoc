.. -*- coding: utf-8; mode: rst -*-

.. _API-genphy-setup-forced:

===================
genphy_setup_forced
===================

*man genphy_setup_forced(9)*

*4.6.0-rc5*

configures/forces speed/duplex from ``phydev``


Synopsis
========

.. c:function:: int genphy_setup_forced( struct phy_device * phydev )

Arguments
=========

``phydev``
    target phy_device struct


Description
===========

Configures MII_BMCR to force speed/duplex to the values in phydev.
Assumes that the values are valid. Please see ``phy_sanitize_settings``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
