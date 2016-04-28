.. -*- coding: utf-8; mode: rst -*-

.. _API-devm-release-resource:

=====================
devm_release_resource
=====================

*man devm_release_resource(9)*

*4.6.0-rc5*

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

Releases a resource previously requested using
``devm_request_resource``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
