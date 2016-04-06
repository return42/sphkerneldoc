
.. _API-media-entity-get:

================
media_entity_get
================

*man media_entity_get(9)*

*4.6.0-rc1*

Get a reference to the parent module


Synopsis
========

.. c:function:: struct media_entity ⋆ media_entity_get( struct media_entity * entity )

Arguments
=========

``entity``
    The entity


Description
===========

Get a reference to the parent media device module.

The function will return immediately if ``entity`` is NULL.

Return a pointer to the entity on success or NULL on failure.
