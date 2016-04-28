.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-register-device:

===================
snd_register_device
===================

*man snd_register_device(9)*

*4.6.0-rc5*

Register the ALSA device file for the card


Synopsis
========

.. c:function:: int snd_register_device( int type, struct snd_card * card, int dev, const struct file_operations * f_ops, void * private_data, struct device * device )

Arguments
=========

``type``
    the device type, SNDRV_DEVICE_TYPE_XXX

``card``
    the card instance

``dev``
    the device index

``f_ops``
    the file operations

``private_data``
    user pointer for f_ops-> ``open``

``device``
    the device to register


Description
===========

Registers an ALSA device file for the given card. The operators have to
be set in reg parameter.


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
