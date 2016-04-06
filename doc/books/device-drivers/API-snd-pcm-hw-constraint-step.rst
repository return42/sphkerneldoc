
.. _API-snd-pcm-hw-constraint-step:

==========================
snd_pcm_hw_constraint_step
==========================

*man snd_pcm_hw_constraint_step(9)*

*4.6.0-rc1*

add a hw constraint step rule


Synopsis
========

.. c:function:: int snd_pcm_hw_constraint_step( struct snd_pcm_runtime * runtime, unsigned int cond, snd_pcm_hw_param_t var, unsigned long step )

Arguments
=========

``runtime``
    PCM runtime instance

``cond``
    condition bits

``var``
    hw_params variable to apply the step constraint

``step``
    step size


Return
======

Zero if successful, or a negative error code on failure.
