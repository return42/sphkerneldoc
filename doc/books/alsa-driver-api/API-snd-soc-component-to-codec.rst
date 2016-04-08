
.. _API-snd-soc-component-to-codec:

==========================
snd_soc_component_to_codec
==========================

*man snd_soc_component_to_codec(9)*

*4.6.0-rc1*

Casts a component to the CODEC it is embedded in


Synopsis
========

.. c:function:: struct snd_soc_codec ⋆ snd_soc_component_to_codec( struct snd_soc_component * component )

Arguments
=========

``component``
    The component to cast to a CODEC


Description
===========

This function must only be used on components that are known to be CODECs. Otherwise the behavior is undefined.
