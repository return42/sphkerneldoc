.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-trigger-done:

====================
snd_pcm_trigger_done
====================

*man snd_pcm_trigger_done(9)*

*4.6.0-rc5*

Mark the master substream


Synopsis
========

.. c:function:: void snd_pcm_trigger_done( struct snd_pcm_substream * substream, struct snd_pcm_substream * master )

Arguments
=========

``substream``
    the pcm substream instance

``master``
    the linked master substream


Description
===========

When multiple substreams of the same card are linked and the hardware
supports the single-shot operation, the driver calls this in the loop in
``snd_pcm_group_for_each_entry`` for marking the substream as “done”.
Then most of trigger operations are performed only to the given master
substream.

The trigger_master mark is cleared at timestamp updates at the end of
trigger operations.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
