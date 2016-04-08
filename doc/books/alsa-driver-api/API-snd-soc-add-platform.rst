
.. _API-snd-soc-add-platform:

====================
snd_soc_add_platform
====================

*man snd_soc_add_platform(9)*

*4.6.0-rc1*

Add a platform to the ASoC core


Synopsis
========

.. c:function:: int snd_soc_add_platform( struct device * dev, struct snd_soc_platform * platform, const struct snd_soc_platform_driver * platform_drv )

Arguments
=========

``dev``
    The parent device for the platform

``platform``
    The platform to add

``platform_drv``
    The driver for the platform
