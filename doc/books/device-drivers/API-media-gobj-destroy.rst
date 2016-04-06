
.. _API-media-gobj-destroy:

==================
media_gobj_destroy
==================

*man media_gobj_destroy(9)*

*4.6.0-rc1*

Stop using a graph object on a media device


Synopsis
========

.. c:function:: void media_gobj_destroy( struct media_gobj * gobj )

Arguments
=========

``gobj``
    Pointer to the graph object


Description
===========

This should be called by all routines like ``media_device_unregister`` that remove/destroy media graph objects.
