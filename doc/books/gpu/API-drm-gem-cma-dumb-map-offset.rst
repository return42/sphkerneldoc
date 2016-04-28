.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-cma-dumb-map-offset:

===========================
drm_gem_cma_dumb_map_offset
===========================

*man drm_gem_cma_dumb_map_offset(9)*

*4.6.0-rc5*

return the fake mmap offset for a CMA GEM object


Synopsis
========

.. c:function:: int drm_gem_cma_dumb_map_offset( struct drm_file * file_priv, struct drm_device * drm, u32 handle, u64 * offset )

Arguments
=========

``file_priv``
    DRM file-private structure containing the GEM object

``drm``
    DRM device

``handle``
    GEM object handle

``offset``
    return location for the fake mmap offset


Description
===========

This function look up an object by its handle and returns the fake mmap
offset associated with it. Drivers using the CMA helpers should set this
as their DRM driver's ->``dumb_map_offset`` callback.


Returns
=======

0 on success or a negative error code on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
