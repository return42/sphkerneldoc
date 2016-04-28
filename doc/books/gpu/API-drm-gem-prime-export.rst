.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-prime-export:

====================
drm_gem_prime_export
====================

*man drm_gem_prime_export(9)*

*4.6.0-rc5*

helper library implementation of the export callback


Synopsis
========

.. c:function:: struct dma_buf * drm_gem_prime_export( struct drm_device * dev, struct drm_gem_object * obj, int flags )

Arguments
=========

``dev``
    drm_device to export from

``obj``
    GEM object to export

``flags``
    flags like DRM_CLOEXEC and DRM_RDWR


Description
===========

This is the implementation of the gem_prime_export functions for GEM
drivers using the PRIME helpers.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
