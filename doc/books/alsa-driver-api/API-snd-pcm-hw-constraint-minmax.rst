
.. _API-snd-pcm-hw-constraint-minmax:

============================
snd_pcm_hw_constraint_minmax
============================

*man snd_pcm_hw_constraint_minmax(9)*

*4.6.0-rc1*

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

Positive if the value is changed, zero if it's not changed, or a negative error code.
