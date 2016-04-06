
.. _API-snd-pcm-hw-param-value:

======================
snd_pcm_hw_param_value
======================

*man snd_pcm_hw_param_value(9)*

*4.6.0-rc1*

return ``params`` field ``var`` value


Synopsis
========

.. c:function:: int snd_pcm_hw_param_value( const struct snd_pcm_hw_params * params, snd_pcm_hw_param_t var, int * dir )

Arguments
=========

``params``
    the hw_params instance

``var``
    parameter to retrieve

``dir``
    pointer to the direction (-1,0,1) or ``NULL``


Return
======

The value for field ``var`` if it's fixed in configuration space defined by ``params``. -``EINVAL`` otherwise.
