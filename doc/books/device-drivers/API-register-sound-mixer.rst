
.. _API-register-sound-mixer:

====================
register_sound_mixer
====================

*man register_sound_mixer(9)*

*4.6.0-rc1*

register a mixer device


Synopsis
========

.. c:function:: int register_sound_mixer( const struct file_operations * fops, int dev )

Arguments
=========

``fops``
    File operations for the driver

``dev``
    Unit number to allocate


Description
===========

Allocate a mixer device. Unit is the number of the mixer requested. Pass -1 to request the next free mixer unit.


Return
======

On success, the allocated number is returned. On failure, a negative error code is returned.
