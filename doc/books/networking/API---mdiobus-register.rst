
.. _API---mdiobus-register:

==================
__mdiobus_register
==================

*man __mdiobus_register(9)*

*4.6.0-rc1*

bring up all the PHYs on a given bus and attach them to bus


Synopsis
========

.. c:function:: int __mdiobus_register( struct mii_bus * bus, struct module * owner )

Arguments
=========

``bus``
    target mii_bus

``owner``
    module containing bus accessor functions


Description
===========

Called by a bus driver to bring up all the PHYs on a given bus, and attach them to the bus. Drivers should use ``mdiobus_register`` rather than ``__mdiobus_register`` unless they
need to pass a specific owner module. MDIO devices which are not PHYs will not be brought up by this function. They are expected to to be explicitly listed in DT and instantiated
by ``of_mdiobus_register``.

Returns 0 on success or < 0 on error.
