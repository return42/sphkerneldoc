
.. _API-transport-add-device:

====================
transport_add_device
====================

*man transport_add_device(9)*

*4.6.0-rc1*

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

Usually, dev represents some component in the HBA system (either the HBA itself or a device remote across the HBA bus). This routine is simply a trigger point used to add the
device to the system and register attributes for it.
