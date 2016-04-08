
.. _API-of-mdio-find-bus:

================
of_mdio_find_bus
================

*man of_mdio_find_bus(9)*

*4.6.0-rc1*

Given an mii_bus node, find the mii_bus.


Synopsis
========

.. c:function:: struct mii_bus ⋆ of_mdio_find_bus( struct device_node * mdio_bus_np )

Arguments
=========

``mdio_bus_np``
    Pointer to the mii_bus.


Description
===========

Returns a reference to the mii_bus, or NULL if none found. The embedded struct device will have its reference count incremented, and this must be put once the bus is finished
with.

Because the association of a device_node and mii_bus is made via ``of_mdiobus_register``, the mii_bus cannot be found before it is registered with ``of_mdiobus_register``.
