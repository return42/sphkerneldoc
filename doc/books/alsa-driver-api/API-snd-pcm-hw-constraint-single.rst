
.. _API-snd-pcm-hw-constraint-single:

============================
snd_pcm_hw_constraint_single
============================

*man snd_pcm_hw_constraint_single(9)*

*4.6.0-rc1*

Constrain parameter to a single value


Synopsis
========

.. c:function:: int snd_pcm_hw_constraint_single( struct snd_pcm_runtime * runtime, snd_pcm_hw_param_t var, unsigned int val )

Arguments
=========

``runtime``
    PCM runtime instance

``var``
    The hw_params variable to constrain

``val``
    The value to constrain to


Return
======

Positive if the value is changed, zero if it's not changed, or a negative error code.
