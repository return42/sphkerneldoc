.. -*- coding: utf-8; mode: rst -*-

.. _API---snd-rawmidi-transmit-peek:

===========================
__snd_rawmidi_transmit_peek
===========================

*man __snd_rawmidi_transmit_peek(9)*

*4.6.0-rc5*

copy data from the internal buffer


Synopsis
========

.. c:function:: int __snd_rawmidi_transmit_peek( struct snd_rawmidi_substream * substream, unsigned char * buffer, int count )

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

This is a variant of ``snd_rawmidi_transmit_peek`` without spinlock.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
