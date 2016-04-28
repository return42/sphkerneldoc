.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-dapm-sync-unlocked:

==========================
snd_soc_dapm_sync_unlocked
==========================

*man snd_soc_dapm_sync_unlocked(9)*

*4.6.0-rc5*

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

Walks all dapm audio paths and powers widgets according to their stream
or path usage.

Requires external locking.

Returns 0 for success.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
