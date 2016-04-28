.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-bulk-unregister-supply-alias:

======================================
regulator_bulk_unregister_supply_alias
======================================

*man regulator_bulk_unregister_supply_alias(9)*

*4.6.0-rc5*

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

This helper function allows drivers to unregister several supply aliases
in one operation.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
