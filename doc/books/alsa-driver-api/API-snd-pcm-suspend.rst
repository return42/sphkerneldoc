.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-suspend:

===============
snd_pcm_suspend
===============

*man snd_pcm_suspend(9)*

*4.6.0-rc5*

trigger SUSPEND to all linked streams


Synopsis
========

.. c:function:: int snd_pcm_suspend( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the PCM substream


Description
===========

After this call, all streams are changed to SUSPENDED state.


Return
======

Zero if successful (or ``substream`` is ``NULL``), or a negative error
code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
