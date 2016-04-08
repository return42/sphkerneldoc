
.. _API-snd-pcm-lib-ioctl:

=================
snd_pcm_lib_ioctl
=================

*man snd_pcm_lib_ioctl(9)*

*4.6.0-rc1*

a generic PCM ioctl callback


Synopsis
========

.. c:function:: int snd_pcm_lib_ioctl( struct snd_pcm_substream * substream, unsigned int cmd, void * arg )

Arguments
=========

``substream``
    the pcm substream instance

``cmd``
    ioctl command

``arg``
    ioctl argument


Description
===========

Processes the generic ioctl commands for PCM. Can be passed as the ioctl callback for PCM ops.


Return
======

Zero if successful, or a negative error code on failure.
