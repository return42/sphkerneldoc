.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-update-power:

=====================
snd_ac97_update_power
=====================

*man snd_ac97_update_power(9)*

*4.6.0-rc5*

update the powerdown register


Synopsis
========

.. c:function:: int snd_ac97_update_power( struct snd_ac97 * ac97, int reg, int powerup )

Arguments
=========

``ac97``
    the codec instance

``reg``
    the rate register, e.g. AC97_PCM_FRONT_DAC_RATE

``powerup``
    non-zero when power up the part


Description
===========

Update the AC97 powerdown register bits of the given part.


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
