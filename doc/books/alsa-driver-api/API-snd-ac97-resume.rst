
.. _API-snd-ac97-resume:

===============
snd_ac97_resume
===============

*man snd_ac97_resume(9)*

*4.6.0-rc1*

General resume function for AC97 codec


Synopsis
========

.. c:function:: void snd_ac97_resume( struct snd_ac97 * ac97 )

Arguments
=========

``ac97``
    the ac97 instance


Description
===========

Do the standard resume procedure, power up and restoring the old register values.
