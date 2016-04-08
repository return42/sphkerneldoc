
.. _API-snd-soc-kcontrol-component:

==========================
snd_soc_kcontrol_component
==========================

*man snd_soc_kcontrol_component(9)*

*4.6.0-rc1*

Returns the component that registered the control


Synopsis
========

.. c:function:: struct snd_soc_component ⋆ snd_soc_kcontrol_component( struct snd_kcontrol * kcontrol )

Arguments
=========

``kcontrol``
    The control for which to get the component


Note
====

This function will work correctly if the control has been registered for a component. Either with ``snd_soc_add_codec_controls`` or ``snd_soc_add_platform_controls`` or via table
based setup for either a CODEC, a platform or component driver. Otherwise the behavior is undefined.
