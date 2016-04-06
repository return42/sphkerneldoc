
.. _API-media-entity-enum-init:

======================
media_entity_enum_init
======================

*man media_entity_enum_init(9)*

*4.6.0-rc1*

Initialise an entity enumeration


Synopsis
========

.. c:function:: int media_entity_enum_init( struct media_entity_enum * ent_enum, struct media_device * mdev )

Arguments
=========

``ent_enum``
    Entity enumeration to be initialised

``mdev``
    The related media device


Description
===========

Returns zero on success or a negative error code.
