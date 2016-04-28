.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-dev-unref:

=============
drm_dev_unref
=============

*man drm_dev_unref(9)*

*4.6.0-rc5*

Drop reference of a DRM device


Synopsis
========

.. c:function:: void drm_dev_unref( struct drm_device * dev )

Arguments
=========

``dev``
    device to drop reference of or NULL


Description
===========

This decreases the ref-count of ``dev`` by one. The device is destroyed
if the ref-count drops to zero.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
