.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-lib-preallocate-free-for-all:

====================================
snd_pcm_lib_preallocate_free_for_all
====================================

*man snd_pcm_lib_preallocate_free_for_all(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
