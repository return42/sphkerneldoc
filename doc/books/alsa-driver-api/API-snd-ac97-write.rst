
.. _API-snd-ac97-write:

==============
snd_ac97_write
==============

*man snd_ac97_write(9)*

*4.6.0-rc1*

write a value on the given register


Synopsis
========

.. c:function:: void snd_ac97_write( struct snd_ac97 * ac97, unsigned short reg, unsigned short value )

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

Writes a value on the given register. This will invoke the write callback directly after the register check. This function doesn't change the register cache unlike
#\ ``snd_ca97_write_cache``, so use this only when you don't want to reflect the change to the suspend/resume state.
