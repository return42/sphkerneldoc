
.. _API-snd-pcm-suspend-all:

===================
snd_pcm_suspend_all
===================

*man snd_pcm_suspend_all(9)*

*4.6.0-rc1*

trigger SUSPEND to all substreams in the given pcm


Synopsis
========

.. c:function:: int snd_pcm_suspend_all( struct snd_pcm * pcm )

Arguments
=========

``pcm``
    the PCM instance


Description
===========

After this call, all streams are changed to SUSPENDED state.


Return
======

Zero if successful (or ``pcm`` is ``NULL``), or a negative error code.
