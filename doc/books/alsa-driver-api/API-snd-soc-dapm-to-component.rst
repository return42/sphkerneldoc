
.. _API-snd-soc-dapm-to-component:

=========================
snd_soc_dapm_to_component
=========================

*man snd_soc_dapm_to_component(9)*

*4.6.0-rc1*

Casts a DAPM context to the component it is embedded in


Synopsis
========

.. c:function:: struct snd_soc_component ⋆ snd_soc_dapm_to_component( struct snd_soc_dapm_context * dapm )

Arguments
=========

``dapm``
    The DAPM context to cast to the component


Description
===========

This function must only be used on DAPM contexts that are known to be part of a component (e.g. in a component driver). Otherwise the behavior is undefined.
