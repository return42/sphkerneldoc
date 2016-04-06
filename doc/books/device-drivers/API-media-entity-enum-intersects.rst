
.. _API-media-entity-enum-intersects:

============================
media_entity_enum_intersects
============================

*man media_entity_enum_intersects(9)*

*4.6.0-rc1*

Test whether two enums intersect


Synopsis
========

.. c:function:: bool media_entity_enum_intersects( struct media_entity_enum * ent_enum1, struct media_entity_enum * ent_enum2 )

Arguments
=========

``ent_enum1``
    First entity enumeration

``ent_enum2``
    Second entity enumeration


Description
===========

Returns true if entity enumerations e and f intersect, otherwise false.
