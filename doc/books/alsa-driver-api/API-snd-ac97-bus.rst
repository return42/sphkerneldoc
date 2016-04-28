.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-bus:

============
snd_ac97_bus
============

*man snd_ac97_bus(9)*

*4.6.0-rc5*

create an AC97 bus component


Synopsis
========

.. c:function:: int snd_ac97_bus( struct snd_card * card, int num, struct snd_ac97_bus_ops * ops, void * private_data, struct snd_ac97_bus ** rbus )

Arguments
=========

``card``
    the card instance

``num``
    the bus number

``ops``
    the bus callbacks table

``private_data``
    private data pointer for the new instance

``rbus``
    the pointer to store the new AC97 bus instance.


Description
===========

Creates an AC97 bus component. An struct snd_ac97_bus instance is
newly allocated and initialized.

The ops table must include valid callbacks (at least read and write).
The other callbacks, wait and reset, are not mandatory.

The clock is set to 48000. If another clock is needed, set
(*rbus)->clock manually.

The AC97 bus instance is registered as a low-level device, so you don't
have to release it manually.


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
