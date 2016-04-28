.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-object-init:

===================
drm_gem_object_init
===================

*man drm_gem_object_init(9)*

*4.6.0-rc5*

initialize an allocated shmem-backed GEM object


Synopsis
========

.. c:function:: int drm_gem_object_init( struct drm_device * dev, struct drm_gem_object * obj, size_t size )

Arguments
=========

``dev``
    drm_device the object should be initialized for

``obj``
    drm_gem_object to initialize

``size``
    object size


Description
===========

Initialize an already allocated GEM object of the specified size with
shmfs backing store.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
