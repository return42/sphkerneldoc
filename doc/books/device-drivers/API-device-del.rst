.. -*- coding: utf-8; mode: rst -*-

.. _API-device-del:

==========
device_del
==========

*man device_del(9)*

*4.6.0-rc5*

delete device from system.


Synopsis
========

.. c:function:: void device_del( struct device * dev )

Arguments
=========

``dev``
    device.


Description
===========

This is the first part of the device unregistration sequence. This
removes the device from the lists we control from here, has it removed
from the other driver model subsystems it was added to in
``device_add``, and removes it from the kobject hierarchy.


NOTE
====

this should be called manually _iff_ ``device_add`` was also called
manually.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
