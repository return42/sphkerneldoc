.. -*- coding: utf-8; mode: rst -*-

.. _API-regulator-get-exclusive:

=======================
regulator_get_exclusive
=======================

*man regulator_get_exclusive(9)*

*4.6.0-rc5*

obtain exclusive access to a regulator.


Synopsis
========

.. c:function:: struct regulator * regulator_get_exclusive( struct device * dev, const char * id )

Arguments
=========

``dev``
    device for regulator “consumer”

``id``
    Supply name or regulator ID.


Description
===========

Returns a struct regulator corresponding to the regulator producer, or
``IS_ERR`` condition containing errno. Other consumers will be unable to
obtain this regulator while this reference is held and the use count for
the regulator will be initialised to reflect the current state of the
regulator.

This is intended for use by consumers which cannot tolerate shared use
of the regulator such as those which need to force the regulator off for
correct operation of the hardware they are controlling.

Use of supply names configured via ``regulator_set_device_supply`` is
strongly encouraged. It is recommended that the supply name used should
match the name used for the supply and/or the relevant device pins in
the datasheet.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
