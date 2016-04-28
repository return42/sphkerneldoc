.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-cache-sync:

==================
snd_soc_cache_sync
==================

*man snd_soc_cache_sync(9)*

*4.6.0-rc5*

Sync the register cache with the hardware


Synopsis
========

.. c:function:: int snd_soc_cache_sync( struct snd_soc_codec * codec )

Arguments
=========

``codec``
    CODEC to sync


Note
====

This function will call ``regcache_sync``


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
