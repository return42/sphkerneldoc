.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-pcm-assign:

===================
snd_ac97_pcm_assign
===================

*man snd_ac97_pcm_assign(9)*

*4.6.0-rc5*

assign AC97 slots to given PCM streams


Synopsis
========

.. c:function:: int snd_ac97_pcm_assign( struct snd_ac97_bus * bus, unsigned short pcms_count, const struct ac97_pcm * pcms )

Arguments
=========

``bus``
    the ac97 bus instance

``pcms_count``
    count of PCMs to be assigned

``pcms``
    PCMs to be assigned


Description
===========

It assigns available AC97 slots for given PCMs. If none or only some
slots are available, pcm->xxx.slots and pcm->xxx.rslots[] members are
reduced and might be zero.


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
