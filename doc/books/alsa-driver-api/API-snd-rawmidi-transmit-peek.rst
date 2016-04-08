
.. _API-snd-rawmidi-transmit-peek:

=========================
snd_rawmidi_transmit_peek
=========================

*man snd_rawmidi_transmit_peek(9)*

*4.6.0-rc1*

copy data from the internal buffer


Synopsis
========

.. c:function:: int snd_rawmidi_transmit_peek( struct snd_rawmidi_substream * substream, unsigned char * buffer, int count )

Arguments
=========

``substream``
    the rawmidi substream

``buffer``
    the buffer pointer

``count``
    data size to transfer


Description
===========

Copies data from the internal output buffer to the given buffer.

Call this in the interrupt handler when the midi output is ready, and call ``snd_rawmidi_transmit_ack`` after the transmission is finished.


Return
======

The size of copied data, or a negative error code on failure.
