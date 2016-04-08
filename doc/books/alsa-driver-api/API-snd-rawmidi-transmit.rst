
.. _API-snd-rawmidi-transmit:

====================
snd_rawmidi_transmit
====================

*man snd_rawmidi_transmit(9)*

*4.6.0-rc1*

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
