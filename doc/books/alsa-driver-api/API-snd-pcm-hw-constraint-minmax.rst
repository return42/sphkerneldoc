.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-hw-constraint-minmax:

============================
snd_pcm_hw_constraint_minmax
============================

*man snd_pcm_hw_constraint_minmax(9)*

*4.6.0-rc5*

apply a min/max range constraint to an interval


Synopsis
========

.. c:function:: int snd_pcm_hw_constraint_minmax( struct snd_pcm_runtime * runtime, snd_pcm_hw_param_t var, unsigned int min, unsigned int max )

Arguments
=========

``runtime``
    PCM runtime instance

``var``
    hw_params variable to apply the range

``min``
    the minimal value

``max``
    the maximal value


Description
===========

Apply the min/max range constraint to an interval parameter.


Return
======

Positive if the value is changed, zero if it's not changed, or a
negative error code.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
