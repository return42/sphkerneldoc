
.. _API-mdio-bus-match:

==============
mdio_bus_match
==============

*man mdio_bus_match(9)*

*4.6.0-rc1*

determine if given MDIO driver supports the given MDIO device


Synopsis
========

.. c:function:: int mdio_bus_match( struct device * dev, struct device_driver * drv )

Arguments
=========

``dev``
    target MDIO device

``drv``
    given MDIO driver


Description
===========

Given a MDIO device, and a MDIO driver, return 1 if the driver supports the device. Otherwise, return 0. This may require calling the devices own match function, since different
classes of MDIO devices have different match criteria.
