
.. _API-snd-pcm-hw-constraint-ranges:

============================
snd_pcm_hw_constraint_ranges
============================

*man snd_pcm_hw_constraint_ranges(9)*

*4.6.0-rc1*

apply list of range constraints to a parameter


Synopsis
========

.. c:function:: int snd_pcm_hw_constraint_ranges( struct snd_pcm_runtime * runtime, unsigned int cond, snd_pcm_hw_param_t var, const struct snd_pcm_hw_constraint_ranges * r )

Arguments
=========

``runtime``
    PCM runtime instance

``cond``
    condition bits

``var``
    hw_params variable to apply the list of range constraints

``r``
    ranges


Description
===========

Apply the list of range constraints to an interval parameter.


Return
======

Zero if successful, or a negative error code on failure.
