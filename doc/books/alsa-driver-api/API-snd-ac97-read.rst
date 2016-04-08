
.. _API-snd-ac97-read:

=============
snd_ac97_read
=============

*man snd_ac97_read(9)*

*4.6.0-rc1*

read a value from the given register


Synopsis
========

.. c:function:: unsigned short snd_ac97_read( struct snd_ac97 * ac97, unsigned short reg )

Arguments
=========

``ac97``
    the ac97 instance

``reg``
    the register to read


Description
===========

Reads a value from the given register. This will invoke the read callback directly after the register check.


Return
======

The read value.
