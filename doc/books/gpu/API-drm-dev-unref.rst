
.. _API-drm-dev-unref:

=============
drm_dev_unref
=============

*man drm_dev_unref(9)*

*4.6.0-rc1*

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

This decreases the ref-count of ``dev`` by one. The device is destroyed if the ref-count drops to zero.
