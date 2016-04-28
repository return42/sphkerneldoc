.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-update:

===============
snd_ac97_update
===============

*man snd_ac97_update(9)*

*4.6.0-rc5*

update the value on the given register


Synopsis
========

.. c:function:: int snd_ac97_update( struct snd_ac97 * ac97, unsigned short reg, unsigned short value )

Arguments
=========

``ac97``
    the ac97 instance

``reg``
    the register to change

``value``
    the value to set


Description
===========

Compares the value with the register cache and updates the value only
when the value is changed.


Return
======

1 if the value is changed, 0 if no change, or a negative code on
failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
