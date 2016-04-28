.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-soc-add-platform:

====================
snd_soc_add_platform
====================

*man snd_soc_add_platform(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
