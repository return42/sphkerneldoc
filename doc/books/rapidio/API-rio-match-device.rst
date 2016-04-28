.. -*- coding: utf-8; mode: rst -*-

.. _API-rio-match-device:

================
rio_match_device
================

*man rio_match_device(9)*

*4.6.0-rc5*

Tell if a RIO device has a matching RIO device id structure


Synopsis
========

.. c:function:: const struct rio_device_id * rio_match_device( const struct rio_device_id * id, const struct rio_dev * rdev )

Arguments
=========

``id``
    the RIO device id structure to match against

``rdev``
    the RIO device structure to match against


Description
===========

Used from driver probe and bus matching to check whether a RIO device
matches a device id structure provided by a RIO driver. Returns the
matching ``struct rio_device_id`` or ``NULL`` if there is no match.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
