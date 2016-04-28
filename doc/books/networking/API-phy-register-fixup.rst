.. -*- coding: utf-8; mode: rst -*-

.. _API-phy-register-fixup:

==================
phy_register_fixup
==================

*man phy_register_fixup(9)*

*4.6.0-rc5*

creates a new phy_fixup and adds it to the list


Synopsis
========

.. c:function:: int phy_register_fixup( const char * bus_id, u32 phy_uid, u32 phy_uid_mask, int (*run) struct phy_device * )

Arguments
=========

``bus_id``
    A string which matches phydev->mdio.dev.bus_id (or PHY_ANY_ID)

``phy_uid``
    Used to match against phydev->phy_id (the UID of the PHY) It can
    also be PHY_ANY_UID

``phy_uid_mask``
    Applied to phydev->phy_id and fixup->phy_uid before comparison

``run``
    The actual code to be run when a matching PHY is found


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
