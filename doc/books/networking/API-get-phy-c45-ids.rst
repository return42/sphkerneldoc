.. -*- coding: utf-8; mode: rst -*-

.. _API-get-phy-c45-ids:

===============
get_phy_c45_ids
===============

*man get_phy_c45_ids(9)*

*4.6.0-rc5*

reads the specified addr for its 802.3-c45 IDs.


Synopsis
========

.. c:function:: int get_phy_c45_ids( struct mii_bus * bus, int addr, u32 * phy_id, struct phy_c45_device_ids * c45_ids )

Arguments
=========

``bus``
    the target MII bus

``addr``
    PHY address on the MII bus

``phy_id``
    where to store the ID retrieved.

``c45_ids``
    where to store the c45 ID information.


Description
===========

If the PHY devices-in-package appears to be valid, it and the
corresponding identifiers are stored in ``c45_ids``, zero is stored in
``phy_id``. Otherwise 0xffffffff is stored in ``phy_id``. Returns zero
on success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
