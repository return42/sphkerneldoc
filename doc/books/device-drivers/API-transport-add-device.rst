.. -*- coding: utf-8; mode: rst -*-

.. _API-transport-add-device:

====================
transport_add_device
====================

*man transport_add_device(9)*

*4.6.0-rc5*

declare a new dev for transport class association


Synopsis
========

.. c:function:: void transport_add_device( struct device * dev )

Arguments
=========

``dev``
    the generic device representing the entity being added


Description
===========

Usually, dev represents some component in the HBA system (either the HBA
itself or a device remote across the HBA bus). This routine is simply a
trigger point used to add the device to the system and register
attributes for it.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
