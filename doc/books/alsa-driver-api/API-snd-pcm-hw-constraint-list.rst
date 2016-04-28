.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-hw-constraint-list:

==========================
snd_pcm_hw_constraint_list
==========================

*man snd_pcm_hw_constraint_list(9)*

*4.6.0-rc5*

apply a list of constraints to a parameter


Synopsis
========

.. c:function:: int snd_pcm_hw_constraint_list( struct snd_pcm_runtime * runtime, unsigned int cond, snd_pcm_hw_param_t var, const struct snd_pcm_hw_constraint_list * l )

Arguments
=========

``runtime``
    PCM runtime instance

``cond``
    condition bits

``var``
    hw_params variable to apply the list constraint

``l``
    list


Description
===========

Apply the list of constraints to an interval parameter.


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
