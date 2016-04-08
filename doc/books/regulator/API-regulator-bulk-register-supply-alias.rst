
.. _API-regulator-bulk-register-supply-alias:

====================================
regulator_bulk_register_supply_alias
====================================

*man regulator_bulk_register_supply_alias(9)*

*4.6.0-rc1*

register multiple aliases


Synopsis
========

.. c:function:: int regulator_bulk_register_supply_alias( struct device * dev, const char *const * id, struct device * alias_dev, const char *const * alias_id, int num_id )

Arguments
=========

``dev``
    device that will be given as the regulator “consumer”

``id``
    List of supply names or regulator IDs

``alias_dev``
    device that should be used to lookup the supply

``alias_id``
    List of supply names or regulator IDs that should be used to lookup the supply

``num_id``
    Number of aliases to register


Description
===========

``return`` 0 on success, an errno on failure.

This helper function allows drivers to register several supply aliases in one operation. If any of the aliases cannot be registered any aliases that were registered will be removed
before returning to the caller.
