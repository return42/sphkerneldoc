.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-ac97-resume:

===============
snd_ac97_resume
===============

*man snd_ac97_resume(9)*

*4.6.0-rc5*

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

Do the standard resume procedure, power up and restoring the old
register values.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
