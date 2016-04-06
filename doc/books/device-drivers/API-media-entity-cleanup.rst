
.. _API-media-entity-cleanup:

====================
media_entity_cleanup
====================

*man media_entity_cleanup(9)*

*4.6.0-rc1*

free resources associated with an entity


Synopsis
========

.. c:function:: void media_entity_cleanup( struct media_entity * entity )

Arguments
=========

``entity``
    entity where the pads belong


Description
===========

This function must be called during the cleanup phase after unregistering the entity (currently, it does nothing).
