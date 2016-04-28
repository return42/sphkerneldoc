.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-period-elapsed:

======================
snd_pcm_period_elapsed
======================

*man snd_pcm_period_elapsed(9)*

*4.6.0-rc5*

update the pcm status for the next period


Synopsis
========

.. c:function:: void snd_pcm_period_elapsed( struct snd_pcm_substream * substream )

Arguments
=========

``substream``
    the pcm substream instance


Description
===========

This function is called from the interrupt handler when the PCM has
processed the period size. It will update the current pointer, wake up
sleepers, etc.

Even if more than one periods have elapsed since the last call, you have
to call this only once.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
