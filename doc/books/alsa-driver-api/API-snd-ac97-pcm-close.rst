
.. _API-snd-ac97-pcm-close:

==================
snd_ac97_pcm_close
==================

*man snd_ac97_pcm_close(9)*

*4.6.0-rc1*

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
