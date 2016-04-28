.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-hw-constraint-integer:

=============================
snd_pcm_hw_constraint_integer
=============================

*man snd_pcm_hw_constraint_integer(9)*

*4.6.0-rc5*

apply an integer constraint to an interval


Synopsis
========

.. c:function:: int snd_pcm_hw_constraint_integer( struct snd_pcm_runtime * runtime, snd_pcm_hw_param_t var )

Arguments
=========

``runtime``
    PCM runtime instance

``var``
    hw_params variable to apply the integer constraint


Description
===========

Apply the constraint of integer to an interval parameter.


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
