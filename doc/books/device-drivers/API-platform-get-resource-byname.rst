.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-get-resource-byname:

============================
platform_get_resource_byname
============================

*man platform_get_resource_byname(9)*

*4.6.0-rc5*

get a resource for a device by name


Synopsis
========

.. c:function:: struct resource * platform_get_resource_byname( struct platform_device * dev, unsigned int type, const char * name )

Arguments
=========

``dev``
    platform device

``type``
    resource type

``name``
    resource name


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
