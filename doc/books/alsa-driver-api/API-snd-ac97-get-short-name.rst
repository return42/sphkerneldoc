
.. _API-snd-ac97-get-short-name:

=======================
snd_ac97_get_short_name
=======================

*man snd_ac97_get_short_name(9)*

*4.6.0-rc1*

retrieve codec name


Synopsis
========

.. c:function:: const char ⋆ snd_ac97_get_short_name( struct snd_ac97 * ac97 )

Arguments
=========

``ac97``
    the codec instance


Return
======

The short identifying name of the codec.
