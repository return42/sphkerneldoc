
.. _API-snd-pcm-notify:

==============
snd_pcm_notify
==============

*man snd_pcm_notify(9)*

*4.6.0-rc1*

Add/remove the notify list


Synopsis
========

.. c:function:: int snd_pcm_notify( struct snd_pcm_notify * notify, int nfree )

Arguments
=========

``notify``
    PCM notify list

``nfree``
    0 = register, 1 = unregister


Description
===========

This adds the given notifier to the global list so that the callback is called for each registered PCM devices. This exists only for PCM OSS emulation, so far.
