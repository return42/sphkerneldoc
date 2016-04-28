.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-hw-constraint-mask64:

============================
snd_pcm_hw_constraint_mask64
============================

*man snd_pcm_hw_constraint_mask64(9)*

*4.6.0-rc5*

apply the given bitmap mask constraint


Synopsis
========

.. c:function:: int snd_pcm_hw_constraint_mask64( struct snd_pcm_runtime * runtime, snd_pcm_hw_param_t var, u_int64_t mask )

Arguments
=========

``runtime``
    PCM runtime instance

``var``
    hw_params variable to apply the mask

``mask``
    the 64bit bitmap mask


Description
===========

Apply the constraint of the given bitmap mask to a 64-bit mask
parameter.


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
