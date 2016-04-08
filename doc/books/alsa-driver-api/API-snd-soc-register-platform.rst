
.. _API-snd-soc-register-platform:

=========================
snd_soc_register_platform
=========================

*man snd_soc_register_platform(9)*

*4.6.0-rc1*

Register a platform with the ASoC core


Synopsis
========

.. c:function:: int snd_soc_register_platform( struct device * dev, const struct snd_soc_platform_driver * platform_drv )

Arguments
=========

``dev``
    The device for the platform

``platform_drv``
    The driver for the platform
