
.. _API-media-entity-put:

================
media_entity_put
================

*man media_entity_put(9)*

*4.6.0-rc1*

Release the reference to the parent module


Synopsis
========

.. c:function:: void media_entity_put( struct media_entity * entity )

Arguments
=========

``entity``
    The entity


Description
===========

Release the reference count acquired by ``media_entity_get``.

The function will return immediately if ``entity`` is NULL.
