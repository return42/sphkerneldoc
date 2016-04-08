
.. _API-snd-pcm-hw-param-first:

======================
snd_pcm_hw_param_first
======================

*man snd_pcm_hw_param_first(9)*

*4.6.0-rc1*

refine config space and return minimum value


Synopsis
========

.. c:function:: int snd_pcm_hw_param_first( struct snd_pcm_substream * pcm, struct snd_pcm_hw_params * params, snd_pcm_hw_param_t var, int * dir )

Arguments
=========

``pcm``
    PCM instance

``params``
    the hw_params instance

``var``
    parameter to retrieve

``dir``
    pointer to the direction (-1,0,1) or ``NULL``


Description
===========

Inside configuration space defined by ``params`` remove from ``var`` all values > minimum. Reduce configuration space accordingly.


Return
======

The minimum, or a negative error code on failure.
