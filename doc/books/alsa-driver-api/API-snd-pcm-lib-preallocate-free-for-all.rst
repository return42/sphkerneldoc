
.. _API-snd-pcm-lib-preallocate-free-for-all:

====================================
snd_pcm_lib_preallocate_free_for_all
====================================

*man snd_pcm_lib_preallocate_free_for_all(9)*

*4.6.0-rc1*

release all pre-allocated buffers on the pcm


Synopsis
========

.. c:function:: int snd_pcm_lib_preallocate_free_for_all( struct snd_pcm * pcm )

Arguments
=========

``pcm``
    the pcm instance


Description
===========

Releases all the pre-allocated buffers on the given pcm.


Return
======

Zero if successful, or a negative error code on failure.
