.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-device-new:

==============
snd_device_new
==============

*man snd_device_new(9)*

*4.6.0-rc5*

create an ALSA device component


Synopsis
========

.. c:function:: int snd_device_new( struct snd_card * card, enum snd_device_type type, void * device_data, struct snd_device_ops * ops )

Arguments
=========

``card``
    the card instance

``type``
    the device type, SNDRV_DEV_XXX

``device_data``
    the data pointer of this device

``ops``
    the operator table


Description
===========

Creates a new device component for the given data pointer. The device
will be assigned to the card and managed together by the card.

The data pointer plays a role as the identifier, too, so the pointer
address must be unique and unchanged.


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
