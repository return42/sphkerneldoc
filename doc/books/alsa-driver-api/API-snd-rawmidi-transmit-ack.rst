
.. _API-snd-rawmidi-transmit-ack:

========================
snd_rawmidi_transmit_ack
========================

*man snd_rawmidi_transmit_ack(9)*

*4.6.0-rc1*

acknowledge the transmission


Synopsis
========

.. c:function:: int snd_rawmidi_transmit_ack( struct snd_rawmidi_substream * substream, int count )

Arguments
=========

``substream``
    the rawmidi substream

``count``
    the transferred count


Description
===========

Advances the hardware pointer for the internal output buffer with the given size and updates the condition. Call after the transmission is finished.


Return
======

The advanced size if successful, or a negative error code on failure.
