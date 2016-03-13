.. -*- coding: utf-8; mode: rst -*-

==============
media-device.c
==============



.. _xref_media_device_register_entity:

media_device_register_entity
============================

.. c:function:: int media_device_register_entity (struct media_device * mdev, struct media_entity * entity)

    Register an entity with a media device

    :param struct media_device * mdev:
        The media device

    :param struct media_entity * entity:
        The entity




.. _xref_media_device_init:

media_device_init
=================

.. c:function:: void media_device_init (struct media_device * mdev)

    initialize a media device

    :param struct media_device * mdev:
        The media device



Description
-----------

The caller is responsible for initializing the media device before
registration. The following fields must be set:


- dev must point to the parent device
- model must be filled with the device model name


