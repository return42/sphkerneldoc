.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-rawmidi-transmit-empty:

==========================
snd_rawmidi_transmit_empty
==========================

*man snd_rawmidi_transmit_empty(9)*

*4.6.0-rc5*

check whether the output buffer is empty


Synopsis
========

.. c:function:: int snd_rawmidi_transmit_empty( struct snd_rawmidi_substream * substream )

Arguments
=========

``substream``
    the rawmidi substream


Return
======

1 if the internal output buffer is empty, 0 if not.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
