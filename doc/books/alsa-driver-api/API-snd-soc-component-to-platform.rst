
.. _API-snd-soc-component-to-platform:

=============================
snd_soc_component_to_platform
=============================

*man snd_soc_component_to_platform(9)*

*4.6.0-rc1*

Casts a component to the platform it is embedded in


Synopsis
========

.. c:function:: struct snd_soc_platform ⋆ snd_soc_component_to_platform( struct snd_soc_component * component )

Arguments
=========

``component``
    The component to cast to a platform


Description
===========

This function must only be used on components that are known to be platforms. Otherwise the behavior is undefined.
