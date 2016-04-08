
.. _API-regulator-unregister-supply-alias:

=================================
regulator_unregister_supply_alias
=================================

*man regulator_unregister_supply_alias(9)*

*4.6.0-rc1*

Remove device alias


Synopsis
========

.. c:function:: void regulator_unregister_supply_alias( struct device * dev, const char * id )

Arguments
=========

``dev``
    device that will be given as the regulator “consumer”

``id``
    Supply name or regulator ID


Description
===========

Remove a lookup alias if one exists for id on dev.
