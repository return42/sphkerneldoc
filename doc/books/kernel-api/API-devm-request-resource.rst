.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-request-resource:

=====================
devm_request_resource
=====================

*man devm_request_resource(9)*

*4.6.0-rc5*

request and reserve an I/O or memory resource


Synopsis
========

.. c:function:: int devm_request_resource( struct device * dev, struct resource * root, struct resource * new )

Arguments
=========

``dev``
    device for which to request the resource

``root``
    root of the resource tree from which to request the resource

``new``
    descriptor of the resource to request


Description
===========

This is a device-managed version of ``request_resource``. There is
usually no need to release resources requested by this function
explicitly since that will be taken care of when the device is unbound
from its driver. If for some reason the resource needs to be released
explicitly, because of ordering issues for example, drivers must call
``devm_release_resource`` rather than the regular ``release_resource``.

When a conflict is detected between any existing resources and the newly
requested resource, an error message will be printed.

Returns 0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
