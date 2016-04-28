.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-tune-hardware:

======================
snd_ac97_tune_hardware
======================

*man snd_ac97_tune_hardware(9)*

*4.6.0-rc5*

tune up the hardware


Synopsis
========

.. c:function:: int snd_ac97_tune_hardware( struct snd_ac97 * ac97, const struct ac97_quirk * quirk, const char * override )

Arguments
=========

``ac97``
    the ac97 instance

``quirk``
    quirk list

``override``
    explicit quirk value (overrides the list if non-NULL)


Description
===========

Do some workaround for each pci device, such as renaming of the
headphone (true line-out) control as “Master”. The quirk-list must be
terminated with a zero-filled entry.


Return
======

Zero if successful, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
