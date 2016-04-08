
.. _API-snd-device-initialize:

=====================
snd_device_initialize
=====================

*man snd_device_initialize(9)*

*4.6.0-rc1*

Initialize struct device for sound devices


Synopsis
========

.. c:function:: void snd_device_initialize( struct device * dev, struct snd_card * card )

Arguments
=========

``dev``
    device to initialize

``card``
    card to assign, optional
