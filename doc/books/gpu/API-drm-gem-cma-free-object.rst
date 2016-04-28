.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-cma-free-object:

=======================
drm_gem_cma_free_object
=======================

*man drm_gem_cma_free_object(9)*

*4.6.0-rc5*

free resources associated with a CMA GEM object


Synopsis
========

.. c:function:: void drm_gem_cma_free_object( struct drm_gem_object * gem_obj )

Arguments
=========

``gem_obj``
    GEM object to free


Description
===========

This function frees the backing memory of the CMA GEM object, cleans up
the GEM object state and frees the memory used to store the object
itself. Drivers using the CMA helpers should set this as their DRM
driver's ->``gem_free_object`` callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
