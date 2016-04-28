.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-rawmidi-transmit:

====================
snd_rawmidi_transmit
====================

*man snd_rawmidi_transmit(9)*

*4.6.0-rc5*

copy from the buffer to the device


Synopsis
========

.. c:function:: int snd_rawmidi_transmit( struct snd_rawmidi_substream * substream, unsigned char * buffer, int count )

Arguments
=========

``substream``
    the rawmidi substream

``buffer``
    the buffer pointer

``count``
    the data size to transfer


Description
===========

Copies data from the buffer to the device and advances the pointer.


Return
======

The copied size if successful, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
