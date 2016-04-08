
.. _API-snd-device-free:

===============
snd_device_free
===============

*man snd_device_free(9)*

*4.6.0-rc1*

release the device from the card


Synopsis
========

.. c:function:: void snd_device_free( struct snd_card * card, void * device_data )

Arguments
=========

``card``
    the card instance

``device_data``
    the data pointer to release


Description
===========

Removes the device from the list on the card and invokes the callbacks, dev_disconnect and dev_free, corresponding to the state. Then release the device.
