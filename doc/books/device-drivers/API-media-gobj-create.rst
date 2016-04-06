
.. _API-media-gobj-create:

=================
media_gobj_create
=================

*man media_gobj_create(9)*

*4.6.0-rc1*

Initialize a graph object


Synopsis
========

.. c:function:: void media_gobj_create( struct media_device * mdev, enum media_gobj_type type, struct media_gobj * gobj )

Arguments
=========

``mdev``
    Pointer to the media_device that contains the object

``type``
    Type of the object

``gobj``
    Pointer to the graph object


Description
===========

This routine initializes the embedded struct media_gobj inside a media graph object. It is called automatically if media_⋆ ``_create`` calls are used. However, if the object
(entity, link, pad, interface) is embedded on some other object, this function should be called before registering the object at the media controller.
