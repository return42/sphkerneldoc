.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-rawmidi-new:

===============
snd_rawmidi_new
===============

*man snd_rawmidi_new(9)*

*4.6.0-rc5*

create a rawmidi instance


Synopsis
========

.. c:function:: int snd_rawmidi_new( struct snd_card * card, char * id, int device, int output_count, int input_count, struct snd_rawmidi ** rrawmidi )

Arguments
=========

``card``
    the card instance

``id``
    the id string

``device``
    the device index

``output_count``
    the number of output streams

``input_count``
    the number of input streams

``rrawmidi``
    the pointer to store the new rawmidi instance


Description
===========

Creates a new rawmidi instance. Use ``snd_rawmidi_set_ops`` to set the
operators to the new instance.


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
