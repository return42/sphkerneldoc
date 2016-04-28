.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-match-bus:

=============
rio_match_bus
=============

*man rio_match_bus(9)*

*4.6.0-rc5*

Tell if a RIO device structure has a matching RIO driver device id
structure


Synopsis
========

.. c:function:: int rio_match_bus( struct device * dev, struct device_driver * drv )

Arguments
=========

``dev``
    the standard device structure to match against

``drv``
    the standard driver structure containing the ids to match against


Description
===========

Used by a driver to check whether a RIO device present in the system is
in its list of supported devices. Returns 1 if there is a matching
``struct rio_device_id`` or 0 if there is no match.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
