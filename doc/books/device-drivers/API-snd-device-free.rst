.. -*- coding: utf-8; mode: rst -*-

.. _API-snd-device-free:

===============
snd_device_free
===============

*man snd_device_free(9)*

*4.6.0-rc5*

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

Removes the device from the list on the card and invokes the callbacks,
dev_disconnect and dev_free, corresponding to the state. Then release
the device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
