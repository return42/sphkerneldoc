
.. _API-snd-device-register:

===================
snd_device_register
===================

*man snd_device_register(9)*

*4.6.0-rc1*

register the device


Synopsis
========

.. c:function:: int snd_device_register( struct snd_card * card, void * device_data )

Arguments
=========

``card``
    the card instance

``device_data``
    the data pointer to register


Description
===========

Registers the device which was already created via ``snd_device_new``. Usually this is called from ``snd_card_register``, but it can be called later if any new devices are created
after invocation of ``snd_card_register``.


Return
======

Zero if successful, or a negative error code on failure or if the device not found.
