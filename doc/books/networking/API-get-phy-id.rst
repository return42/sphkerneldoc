
.. _API-get-phy-id:

==========
get_phy_id
==========

*man get_phy_id(9)*

*4.6.0-rc1*

reads the specified addr for its ID.


Synopsis
========

.. c:function:: int get_phy_id( struct mii_bus * bus, int addr, u32 * phy_id, bool is_c45, struct phy_c45_device_ids * c45_ids )

Arguments
=========

``bus``
    the target MII bus

``addr``
    PHY address on the MII bus

``phy_id``
    where to store the ID retrieved.

``is_c45``
    If true the PHY uses the 802.3 clause 45 protocol

``c45_ids``
    where to store the c45 ID information.


Description
===========

In the case of a 802.3-c22 PHY, reads the ID registers of the PHY at ``addr`` on the ``bus``, stores it in ``phy_id`` and returns zero on success.

In the case of a 802.3-c45 PHY, ``get_phy_c45_ids`` is invoked, and its return value is in turn returned.
