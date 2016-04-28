.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-rawmidi-receive:

===================
snd_rawmidi_receive
===================

*man snd_rawmidi_receive(9)*

*4.6.0-rc5*

receive the input data from the device


Synopsis
========

.. c:function:: int snd_rawmidi_receive( struct snd_rawmidi_substream * substream, const unsigned char * buffer, int count )

Arguments
=========

``substream``
    the rawmidi substream

``buffer``
    the buffer pointer

``count``
    the data size to read


Description
===========

Reads the data from the internal buffer.


Return
======

The size of read data, or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
