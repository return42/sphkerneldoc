.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-pcm-open:

=================
snd_ac97_pcm_open
=================

*man snd_ac97_pcm_open(9)*

*4.6.0-rc5*

opens the given AC97 pcm


Synopsis
========

.. c:function:: int snd_ac97_pcm_open( struct ac97_pcm * pcm, unsigned int rate, enum ac97_pcm_cfg cfg, unsigned short slots )

Arguments
=========

``pcm``
    the ac97 pcm instance

``rate``
    rate in Hz, if codec does not support VRA, this value must be
    48000Hz

``cfg``
    output stream characteristics

``slots``
    a subset of allocated slots (snd_ac97_pcm_assign) for this pcm


Description
===========

It locks the specified slots and sets the given rate to AC97 registers.


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
