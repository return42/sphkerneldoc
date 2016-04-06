
.. _API-register-sound-midi:

===================
register_sound_midi
===================

*man register_sound_midi(9)*

*4.6.0-rc1*

register a midi device


Synopsis
========

.. c:function:: int register_sound_midi( const struct file_operations * fops, int dev )

Arguments
=========

``fops``
    File operations for the driver

``dev``
    Unit number to allocate


Description
===========

Allocate a midi device. Unit is the number of the midi device requested. Pass -1 to request the next free midi unit.


Return
======

On success, the allocated number is returned. On failure, a negative error code is returned.
