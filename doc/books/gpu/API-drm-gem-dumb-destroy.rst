.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-dumb-destroy:

====================
drm_gem_dumb_destroy
====================

*man drm_gem_dumb_destroy(9)*

*4.6.0-rc5*

dumb fb callback helper for gem based drivers


Synopsis
========

.. c:function:: int drm_gem_dumb_destroy( struct drm_file * file, struct drm_device * dev, uint32_t handle )

Arguments
=========

``file``
    drm file-private structure to remove the dumb handle from

``dev``
    corresponding drm_device

``handle``
    the dumb handle to remove


Description
===========

This implements the ->dumb_destroy kms driver callback for drivers
which use gem to manage their backing storage.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
