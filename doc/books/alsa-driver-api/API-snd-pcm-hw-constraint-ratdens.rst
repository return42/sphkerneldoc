
.. _API-snd-pcm-hw-constraint-ratdens:

=============================
snd_pcm_hw_constraint_ratdens
=============================

*man snd_pcm_hw_constraint_ratdens(9)*

*4.6.0-rc1*

apply ratdens constraint to a parameter


Synopsis
========

.. c:function:: int snd_pcm_hw_constraint_ratdens( struct snd_pcm_runtime * runtime, unsigned int cond, snd_pcm_hw_param_t var, const struct snd_pcm_hw_constraint_ratdens * r )

Arguments
=========

``runtime``
    PCM runtime instance

``cond``
    condition bits

``var``
    hw_params variable to apply the ratdens constraint

``r``
    struct snd_ratdens constriants


Return
======

Zero if successful, or a negative error code on failure.
