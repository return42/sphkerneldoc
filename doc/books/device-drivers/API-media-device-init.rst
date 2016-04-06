
.. _API-media-device-init:

=================
media_device_init
=================

*man media_device_init(9)*

*4.6.0-rc1*

Initializes a media device element


Synopsis
========

.. c:function:: void media_device_init( struct media_device * mdev )

Arguments
=========

``mdev``
    pointer to struct ``media_device``


Description
===========

This function initializes the media device prior to its registration. The media device initialization and registration is split in two functions to avoid race conditions and make
the media device available to user-space before the media graph has been completed.

So drivers need to first initialize the media device, register any entity within the media device, create pad to pad links and then finally register the media device by calling
``media_device_register`` as a final step.
