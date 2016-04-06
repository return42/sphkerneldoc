
.. _API-platform-get-resource-byname:

============================
platform_get_resource_byname
============================

*man platform_get_resource_byname(9)*

*4.6.0-rc1*

get a resource for a device by name


Synopsis
========

.. c:function:: struct resource ⋆ platform_get_resource_byname( struct platform_device * dev, unsigned int type, const char * name )

Arguments
=========

``dev``
    platform device

``type``
    resource type

``name``
    resource name
