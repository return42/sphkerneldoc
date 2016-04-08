
.. _API---snd-rawmidi-transmit-ack:

==========================
__snd_rawmidi_transmit_ack
==========================

*man __snd_rawmidi_transmit_ack(9)*

*4.6.0-rc1*

acknowledge the transmission


Synopsis
========

.. c:function:: int __snd_rawmidi_transmit_ack( struct snd_rawmidi_substream * substream, int count )

Arguments
=========

``substream``
    the rawmidi substream

``count``
    the transferred count


Description
===========

This is a variant of ``__snd_rawmidi_transmit_ack`` without spinlock.
