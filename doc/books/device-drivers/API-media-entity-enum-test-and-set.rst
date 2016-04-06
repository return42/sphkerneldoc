
.. _API-media-entity-enum-test-and-set:

==============================
media_entity_enum_test_and_set
==============================

*man media_entity_enum_test_and_set(9)*

*4.6.0-rc1*

Test whether the entity is marked, and mark it


Synopsis
========

.. c:function:: bool media_entity_enum_test_and_set( struct media_entity_enum * ent_enum, struct media_entity * entity )

Arguments
=========

``ent_enum``
    Entity enumeration

``entity``
    Entity to be tested


Description
===========

Returns true if the entity was marked, and mark it before doing so.
