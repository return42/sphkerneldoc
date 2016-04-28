.. -*- coding: utf-8; mode: rst -*-

.. _API-media-device-unregister:

=======================
media_device_unregister
=======================

*man media_device_unregister(9)*

*4.6.0-rc5*

Unegisters a media device element


Synopsis
========

.. c:function:: void media_device_unregister( struct media_device * mdev )

Arguments
=========

``mdev``
    pointer to struct ``media_device``


Description
===========

It is safe to call this function on an unregistered (but initialised)
media device.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
