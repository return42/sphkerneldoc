
.. _API-media-device-register-entity:

============================
media_device_register_entity
============================

*man media_device_register_entity(9)*

*4.6.0-rc1*

registers a media entity inside a previously registered media device.


Synopsis
========

.. c:function:: int media_device_register_entity( struct media_device * mdev, struct media_entity * entity )

Arguments
=========

``mdev``
    pointer to struct ``media_device``

``entity``
    pointer to struct ``media_entity`` to be registered


Description
===========

Entities are identified by a unique positive integer ID. The media controller framework will such ID automatically. IDs are not guaranteed to be contiguous, and the ID number can
change on newer Kernel versions. So, neither the driver nor userspace should hardcode ID numbers to refer to the entities, but, instead, use the framework to find the ID, when
needed.

The media_entity name, type and flags fields should be initialized before calling ``media_device_register_entity``. Entities embedded in higher-level standard structures can have
some of those fields set by the higher-level framework.

If the device has pads, ``media_entity_pads_init`` should be called before this function. Otherwise, the ``media_entity``.\ ``pad`` and ``media_entity``.\ ``num_pads`` should be
zeroed before calling this function.


Entities have flags that describe the entity capabilities and state
===================================================================

``MEDIA_ENT_FL_DEFAULT`` indicates the default entity for a given type. This can be used to report the default audio and video devices or the default camera sensor.


NOTE
====

Drivers should set the entity function before calling this function. Please notice that the values ``MEDIA_ENT_F_V4L2_SUBDEV_UNKNOWN`` and ``MEDIA_ENT_F_UNKNOWN`` should not be
used by the drivers.
