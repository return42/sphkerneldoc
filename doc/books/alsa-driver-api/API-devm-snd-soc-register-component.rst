
.. _API-devm-snd-soc-register-component:

===============================
devm_snd_soc_register_component
===============================

*man devm_snd_soc_register_component(9)*

*4.6.0-rc1*

resource managed component registration


Synopsis
========

.. c:function:: int devm_snd_soc_register_component( struct device * dev, const struct snd_soc_component_driver * cmpnt_drv, struct snd_soc_dai_driver * dai_drv, int num_dai )

Arguments
=========

``dev``
    Device used to manage component

``cmpnt_drv``
    Component driver

``dai_drv``
    DAI driver

``num_dai``
    Number of DAIs to register


Description
===========

Register a component with automatic unregistration when the device is unregistered.
