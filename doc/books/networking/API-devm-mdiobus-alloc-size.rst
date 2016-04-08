
.. _API-devm-mdiobus-alloc-size:

=======================
devm_mdiobus_alloc_size
=======================

*man devm_mdiobus_alloc_size(9)*

*4.6.0-rc1*

Resource-managed ``mdiobus_alloc_size``


Synopsis
========

.. c:function:: struct mii_bus ⋆ devm_mdiobus_alloc_size( struct device * dev, int sizeof_priv )

Arguments
=========

``dev``
    Device to allocate mii_bus for

``sizeof_priv``
    Space to allocate for private structure.


Description
===========

Managed mdiobus_alloc_size. mii_bus allocated with this function is automatically freed on driver detach.

If an mii_bus allocated with this function needs to be freed separately, ``devm_mdiobus_free`` must be used.


RETURNS
=======

Pointer to allocated mii_bus on success, NULL on failure.
