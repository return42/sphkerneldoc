
.. _API-devm-snd-soc-register-platform:

==============================
devm_snd_soc_register_platform
==============================

*man devm_snd_soc_register_platform(9)*

*4.6.0-rc1*

resource managed platform registration


Synopsis
========

.. c:function:: int devm_snd_soc_register_platform( struct device * dev, const struct snd_soc_platform_driver * platform_drv )

Arguments
=========

``dev``
    Device used to manage platform

``platform_drv``
    platform to register


Description
===========

Register a platform driver with automatic unregistration when the device is unregistered.
