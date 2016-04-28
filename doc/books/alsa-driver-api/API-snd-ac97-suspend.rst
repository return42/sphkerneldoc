.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-suspend:

================
snd_ac97_suspend
================

*man snd_ac97_suspend(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
