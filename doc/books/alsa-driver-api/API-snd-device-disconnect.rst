
.. _API-snd-device-disconnect:

=====================
snd_device_disconnect
=====================

*man snd_device_disconnect(9)*

*4.6.0-rc1*

disconnect the device


Synopsis
========

.. c:function:: void snd_device_disconnect( struct snd_card * card, void * device_data )

Arguments
=========

``card``
    the card instance

``device_data``
    the data pointer to disconnect


Description
===========

Turns the device into the disconnection state, invoking dev_disconnect callback, if the device was already registered.

Usually called from ``snd_card_disconnect``.


Return
======

Zero if successful, or a negative error code on failure or if the device not found.
