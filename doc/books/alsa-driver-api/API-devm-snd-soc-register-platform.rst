.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-snd-soc-register-platform:

==============================
devm_snd_soc_register_platform
==============================

*man devm_snd_soc_register_platform(9)*

*4.6.0-rc5*

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

Register a platform driver with automatic unregistration when the device
is unregistered.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
