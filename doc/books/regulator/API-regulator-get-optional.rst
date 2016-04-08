
.. _API-regulator-get-optional:

======================
regulator_get_optional
======================

*man regulator_get_optional(9)*

*4.6.0-rc1*

obtain optional access to a regulator.


Synopsis
========

.. c:function:: struct regulator ⋆ regulator_get_optional( struct device * dev, const char * id )

Arguments
=========

``dev``
    device for regulator “consumer”

``id``
    Supply name or regulator ID.


Description
===========

Returns a struct regulator corresponding to the regulator producer, or ``IS_ERR`` condition containing errno.

This is intended for use by consumers for devices which can have some supplies unconnected in normal use, such as some MMC devices. It can allow the regulator core to provide stub
supplies for other supplies requested using normal ``regulator_get`` calls without disrupting the operation of drivers that can handle absent supplies.

Use of supply names configured via ``regulator_set_device_supply`` is strongly encouraged. It is recommended that the supply name used should match the name used for the supply
and/or the relevant device pins in the datasheet.
