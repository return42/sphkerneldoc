.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-register-supply-alias:

===============================
regulator_register_supply_alias
===============================

*man regulator_register_supply_alias(9)*

*4.6.0-rc5*

Provide device alias for supply lookup


Synopsis
========

.. c:function:: int regulator_register_supply_alias( struct device * dev, const char * id, struct device * alias_dev, const char * alias_id )

Arguments
=========

``dev``
    device that will be given as the regulator “consumer”

``id``
    Supply name or regulator ID

``alias_dev``
    device that should be used to lookup the supply

``alias_id``
    Supply name or regulator ID that should be used to lookup the supply


Description
===========

All lookups for id on dev will instead be conducted for alias_id on
alias_dev.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
