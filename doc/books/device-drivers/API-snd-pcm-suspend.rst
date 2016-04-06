
.. _API-snd-pcm-suspend:

===============
snd_pcm_suspend
===============

*man snd_pcm_suspend(9)*

*4.6.0-rc1*

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

Zero if successful (or ``substream`` is ``NULL``), or a negative error code.
