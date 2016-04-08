
.. _API-regulator-get:

=============
regulator_get
=============

*man regulator_get(9)*

*4.6.0-rc1*

lookup and obtain a reference to a regulator.


Synopsis
========

.. c:function:: struct regulator ⋆ regulator_get( struct device * dev, const char * id )

Arguments
=========

``dev``
    device for regulator “consumer”

``id``
    Supply name or regulator ID.


Description
===========

Returns a struct regulator corresponding to the regulator producer, or ``IS_ERR`` condition containing errno.

Use of supply names configured via ``regulator_set_device_supply`` is strongly encouraged. It is recommended that the supply name used should match the name used for the supply
and/or the relevant device pins in the datasheet.
