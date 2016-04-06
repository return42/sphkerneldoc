
.. _API-snd-pcm-stop-xrun:

=================
snd_pcm_stop_xrun
=================

*man snd_pcm_stop_xrun(9)*

*4.6.0-rc1*

stop the running streams as XRUN


Synopsis
========

.. c:function:: int snd_pcm_stop_xrun( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the PCM substream instance


Description
===========

This stops the given running substream (and all linked substreams) as XRUN. Unlike ``snd_pcm_stop``, this function takes the substream lock by itself.


Return
======

Zero if successful, or a negative error code.
