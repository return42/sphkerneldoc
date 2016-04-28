.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-free-mmap-offset:

========================
drm_gem_free_mmap_offset
========================

*man drm_gem_free_mmap_offset(9)*

*4.6.0-rc5*

release a fake mmap offset for an object


Synopsis
========

.. c:function:: void drm_gem_free_mmap_offset( struct drm_gem_object * obj )

Arguments
=========

``obj``
    obj in question


Description
===========

This routine frees fake offsets allocated by
``drm_gem_create_mmap_offset``.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
