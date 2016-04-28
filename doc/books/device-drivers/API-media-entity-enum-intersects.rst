.. -*- coding: utf-8; mode: rst -*-

.. _API-media-entity-enum-intersects:

============================
media_entity_enum_intersects
============================

*man media_entity_enum_intersects(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
