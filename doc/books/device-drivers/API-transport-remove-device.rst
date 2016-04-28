.. -*- coding: utf-8; mode: rst -*-

.. _API-transport-remove-device:

=======================
transport_remove_device
=======================

*man transport_remove_device(9)*

*4.6.0-rc5*

remove the visibility of a device


Synopsis
========

.. c:function:: void transport_remove_device( struct device * dev )

Arguments
=========

``dev``
    generic device to remove


Description
===========

This call removes the visibility of the device (to the user from sysfs),
but does not destroy it. To eliminate a device entirely you must also
call transport_destroy_device. If you don't need to do remove and
destroy as separate operations, use ``transport_unregister_device`` (see
transport_class.h) which will perform both calls for you.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
