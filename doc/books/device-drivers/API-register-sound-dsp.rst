
.. _API-register-sound-dsp:

==================
register_sound_dsp
==================

*man register_sound_dsp(9)*

*4.6.0-rc1*

register a DSP device


Synopsis
========

.. c:function:: int register_sound_dsp( const struct file_operations * fops, int dev )

Arguments
=========

``fops``
    File operations for the driver

``dev``
    Unit number to allocate


Description
===========

Allocate a DSP device. Unit is the number of the DSP requested. Pass -1 to request the next free DSP unit.

This function allocates both the audio and dsp device entries together and will always allocate them as a matching pair - eg dsp3/audio3


Return
======

On success, the allocated number is returned. On failure, a negative error code is returned.
