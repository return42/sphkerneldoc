.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-group-for-each-entry:

============================
snd_pcm_group_for_each_entry
============================

*man snd_pcm_group_for_each_entry(9)*

*4.6.0-rc5*

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

Iterate over the all linked substreams to the given ``substream``. When
``substream`` isn't linked with any others, this gives returns
``substream`` itself once.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
