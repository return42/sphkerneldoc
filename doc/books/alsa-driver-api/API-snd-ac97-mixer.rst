
.. _API-snd-ac97-mixer:

==============
snd_ac97_mixer
==============

*man snd_ac97_mixer(9)*

*4.6.0-rc1*

create an Codec97 component


Synopsis
========

.. c:function:: int snd_ac97_mixer( struct snd_ac97_bus * bus, struct snd_ac97_template * template, struct snd_ac97 ** rac97 )

Arguments
=========

``bus``
    the AC97 bus which codec is attached to

``template``
    the template of ac97, including index, callbacks and the private data.

``rac97``
    the pointer to store the new ac97 instance.


Description
===========

Creates an Codec97 component. An struct snd_ac97 instance is newly allocated and initialized from the template. The codec is then initialized by the standard procedure.

The template must include the codec number (num) and address (addr), and the private data (private_data).

The ac97 instance is registered as a low-level device, so you don't have to release it manually.


Return
======

Zero if successful, or a negative error code on failure.
