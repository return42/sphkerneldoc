.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-unregister-supply-alias:

=================================
regulator_unregister_supply_alias
=================================

*man regulator_unregister_supply_alias(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
