.. -*- coding: utf-8; mode: rst -*-

.. _API-media-entity-put:

================
media_entity_put
================

*man media_entity_put(9)*

*4.6.0-rc5*

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


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
