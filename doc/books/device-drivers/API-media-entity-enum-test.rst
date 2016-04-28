.. -*- coding: utf-8; mode: rst -*-

.. _API-media-entity-enum-test:

======================
media_entity_enum_test
======================

*man media_entity_enum_test(9)*

*4.6.0-rc5*

Test whether the entity is marked


Synopsis
========

.. c:function:: bool media_entity_enum_test( struct media_entity_enum * ent_enum, struct media_entity * entity )

Arguments
=========

``ent_enum``
    Entity enumeration

``entity``
    Entity to be tested


Description
===========

Returns true if the entity was marked.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
