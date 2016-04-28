.. -*- coding: utf-8; mode: rst -*-

.. _API-media-device-register-entity-notify:

===================================
media_device_register_entity_notify
===================================

*man media_device_register_entity_notify(9)*

*4.6.0-rc5*

Registers a media entity_notify callback


Synopsis
========

.. c:function:: int media_device_register_entity_notify( struct media_device * mdev, struct media_entity_notify * nptr )

Arguments
=========

``mdev``
    The media device

``nptr``
    The media_entity_notify


Note
====

When a new entity is registered, all the registered
media_entity_notify callbacks are invoked.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
