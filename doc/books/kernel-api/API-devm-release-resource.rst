
.. _API-devm-release-resource:

=====================
devm_release_resource
=====================

*man devm_release_resource(9)*

*4.6.0-rc1*

release a previously requested resource


Synopsis
========

.. c:function:: void devm_release_resource( struct device * dev, struct resource * new )

Arguments
=========

``dev``
    device for which to release the resource

``new``
    descriptor of the resource to release


Description
===========

Releases a resource previously requested using ``devm_request_resource``.
