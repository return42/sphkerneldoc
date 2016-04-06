
.. _API---media-entity-enum-init:

========================
__media_entity_enum_init
========================

*man __media_entity_enum_init(9)*

*4.6.0-rc1*

Initialise an entity enumeration


Synopsis
========

.. c:function:: int __media_entity_enum_init( struct media_entity_enum * ent_enum, int idx_max )

Arguments
=========

``ent_enum``
    Entity enumeration to be initialised

``idx_max``
    Maximum number of entities in the enumeration


Return
======

Returns zero on success or a negative error code.
