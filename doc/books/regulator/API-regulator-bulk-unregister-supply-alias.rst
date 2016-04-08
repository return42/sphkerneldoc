
.. _API-regulator-bulk-unregister-supply-alias:

======================================
regulator_bulk_unregister_supply_alias
======================================

*man regulator_bulk_unregister_supply_alias(9)*

*4.6.0-rc1*

unregister multiple aliases


Synopsis
========

.. c:function:: void regulator_bulk_unregister_supply_alias( struct device * dev, const char *const * id, int num_id )

Arguments
=========

``dev``
    device that will be given as the regulator “consumer”

``id``
    List of supply names or regulator IDs

``num_id``
    Number of aliases to unregister


Description
===========

This helper function allows drivers to unregister several supply aliases in one operation.
