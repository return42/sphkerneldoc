.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/media-device.c

.. _`media_device_register_entity`:

media_device_register_entity
============================

.. c:function:: int media_device_register_entity(struct media_device *mdev, struct media_entity *entity)

    Register an entity with a media device

    :param mdev:
        The media device
    :type mdev: struct media_device \*

    :param entity:
        The entity
    :type entity: struct media_entity \*

.. _`media_device_init`:

media_device_init
=================

.. c:function:: void media_device_init(struct media_device *mdev)

    initialize a media device

    :param mdev:
        The media device
    :type mdev: struct media_device \*

.. _`media_device_init.description`:

Description
-----------

The caller is responsible for initializing the media device before
registration. The following fields must be set:

- dev must point to the parent device
- model must be filled with the device model name

.. This file was automatic generated / don't edit.

