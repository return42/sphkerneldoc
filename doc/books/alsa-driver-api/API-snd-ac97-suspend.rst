
.. _API-snd-ac97-suspend:

================
snd_ac97_suspend
================

*man snd_ac97_suspend(9)*

*4.6.0-rc1*

General suspend function for AC97 codec


Synopsis
========

.. c:function:: void snd_ac97_suspend( struct snd_ac97 * ac97 )

Arguments
=========

``ac97``
    the ac97 instance


Description
===========

Suspends the codec, power down the chip.
