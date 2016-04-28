.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-pcm-hw-rule-add:

===================
snd_pcm_hw_rule_add
===================

*man snd_pcm_hw_rule_add(9)*

*4.6.0-rc5*

add the hw-constraint rule


Synopsis
========

.. c:function:: int snd_pcm_hw_rule_add( struct snd_pcm_runtime * runtime, unsigned int cond, int var, snd_pcm_hw_rule_func_t func, void * private, int dep, ... )

Arguments
=========

``runtime``
    the pcm runtime instance

``cond``
    condition bits

``var``
    the variable to evaluate

``func``
    the evaluation function

``private``
    the private data pointer passed to function

``dep``
    the dependent variables

``...``
    variable arguments


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
