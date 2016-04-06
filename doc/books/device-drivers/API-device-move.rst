
.. _API-device-move:

===========
device_move
===========

*man device_move(9)*

*4.6.0-rc1*

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
