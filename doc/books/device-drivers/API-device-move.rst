.. -*- coding: utf-8; mode: rst -*-

.. _API-device-move:

===========
device_move
===========

*man device_move(9)*

*4.6.0-rc5*

moves a device to a new parent


Synopsis
========

.. c:function:: int device_move( struct device * dev, struct device * new_parent, enum dpm_order dpm_order )

Arguments
=========

``dev``
    the pointer to the struct device to be moved

``new_parent``
    the new parent of the device (can by NULL)

``dpm_order``
    how to reorder the dpm_list


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
