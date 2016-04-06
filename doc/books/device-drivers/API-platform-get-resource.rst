
.. _API-platform-get-resource:

=====================
platform_get_resource
=====================

*man platform_get_resource(9)*

*4.6.0-rc1*

get a resource for a device


Synopsis
========

.. c:function:: struct resource ⋆ platform_get_resource( struct platform_device * dev, unsigned int type, unsigned int num )

Arguments
=========

``dev``
    platform device

``type``
    resource type

``num``
    resource index
