.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-write-cache:

====================
snd_ac97_write_cache
====================

*man snd_ac97_write_cache(9)*

*4.6.0-rc5*

write a value on the given register and update the cache


Synopsis
========

.. c:function:: void snd_ac97_write_cache( struct snd_ac97 * ac97, unsigned short reg, unsigned short value )

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

Writes a value on the given register and updates the register cache. The
cached values are used for the cached-read and the suspend/resume.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
