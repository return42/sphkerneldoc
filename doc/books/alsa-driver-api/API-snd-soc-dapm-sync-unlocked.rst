
.. _API-snd-soc-dapm-sync-unlocked:

==========================
snd_soc_dapm_sync_unlocked
==========================

*man snd_soc_dapm_sync_unlocked(9)*

*4.6.0-rc1*

scan and power dapm paths


Synopsis
========

.. c:function:: int snd_soc_dapm_sync_unlocked( struct snd_soc_dapm_context * dapm )

Arguments
=========

``dapm``
    DAPM context


Description
===========

Walks all dapm audio paths and powers widgets according to their stream or path usage.

Requires external locking.

Returns 0 for success.
