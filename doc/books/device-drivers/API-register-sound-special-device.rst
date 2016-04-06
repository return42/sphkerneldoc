
.. _API-register-sound-special-device:

=============================
register_sound_special_device
=============================

*man register_sound_special_device(9)*

*4.6.0-rc1*

register a special sound node


Synopsis
========

.. c:function:: int register_sound_special_device( const struct file_operations * fops, int unit, struct device * dev )

Arguments
=========

``fops``
    File operations for the driver

``unit``
    Unit number to allocate

``dev``
    device pointer


Description
===========

Allocate a special sound device by minor number from the sound subsystem.


Return
======

The allocated number is returned on success. On failure, a negative error code is returned.
