.. -*- coding: utf-8; mode: rst -*-

.. _API-gem-allocate-guc-obj:

====================
gem_allocate_guc_obj
====================

*man gem_allocate_guc_obj(9)*

*4.6.0-rc5*

Allocate gem object for GuC usage


Synopsis
========

.. c:function:: struct drm_i915_gem_object * gem_allocate_guc_obj( struct drm_device * dev, u32 size )

Arguments
=========

``dev``
    drm device

``size``
    size of object


Description
===========

This is a wrapper to create a gem obj. In order to use it inside GuC,
the object needs to be pinned lifetime. Also we must pin it to gtt space
other than [0, GUC_WOPCM_TOP) because this range is reserved inside
GuC.


Return
======

A drm_i915_gem_object if successful, otherwise NULL.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
