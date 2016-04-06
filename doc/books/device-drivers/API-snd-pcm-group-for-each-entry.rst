
.. _API-snd-pcm-group-for-each-entry:

============================
snd_pcm_group_for_each_entry
============================

*man snd_pcm_group_for_each_entry(9)*

*4.6.0-rc1*

iterate over the linked substreams


Synopsis
========

.. c:function:: snd_pcm_group_for_each_entry( s, substream )

Arguments
=========

``s``
    the iterator

``substream``
    the substream


Description
===========

Iterate over the all linked substreams to the given ``substream``. When ``substream`` isn't linked with any others, this gives returns ``substream`` itself once.
