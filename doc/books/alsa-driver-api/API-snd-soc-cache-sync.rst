
.. _API-snd-soc-cache-sync:

==================
snd_soc_cache_sync
==================

*man snd_soc_cache_sync(9)*

*4.6.0-rc1*

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
