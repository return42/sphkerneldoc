.. -*- coding: utf-8; mode: rst -*-

.. _API-media-entity-remove-links:

=========================
media_entity_remove_links
=========================

*man media_entity_remove_links(9)*

*4.6.0-rc5*

remove all links associated with an entity


Synopsis
========

.. c:function:: void media_entity_remove_links( struct media_entity * entity )

Arguments
=========

``entity``
    pointer to ``media_entity``


Note
====

this is called automatically when an entity is unregistered via
``media_device_register_entity``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
