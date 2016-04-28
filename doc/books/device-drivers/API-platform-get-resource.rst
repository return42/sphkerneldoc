.. -*- coding: utf-8; mode: rst -*-

.. _API-platform-get-resource:

=====================
platform_get_resource
=====================

*man platform_get_resource(9)*

*4.6.0-rc5*

get a resource for a device


Synopsis
========

.. c:function:: struct resource * platform_get_resource( struct platform_device * dev, unsigned int type, unsigned int num )

Arguments
=========

``dev``
    platform device

``type``
    resource type

``num``
    resource index


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
