.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-pcm-close:

==================
snd_ac97_pcm_close
==================

*man snd_ac97_pcm_close(9)*

*4.6.0-rc5*

closes the given AC97 pcm


Synopsis
========

.. c:function:: int snd_ac97_pcm_close( struct ac97_pcm * pcm )

Arguments
=========

``pcm``
    the ac97 pcm instance


Description
===========

It frees the locked AC97 slots.


Return
======

Zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
