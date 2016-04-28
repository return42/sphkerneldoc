.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-hw-constraint-pow2:

==========================
snd_pcm_hw_constraint_pow2
==========================

*man snd_pcm_hw_constraint_pow2(9)*

*4.6.0-rc5*

add a hw constraint power-of-2 rule


Synopsis
========

.. c:function:: int snd_pcm_hw_constraint_pow2( struct snd_pcm_runtime * runtime, unsigned int cond, snd_pcm_hw_param_t var )

Arguments
=========

``runtime``
    PCM runtime instance

``cond``
    condition bits

``var``
    hw_params variable to apply the power-of-2 constraint


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
