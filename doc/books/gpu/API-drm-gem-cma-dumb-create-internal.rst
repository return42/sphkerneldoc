.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-cma-dumb-create-internal:

================================
drm_gem_cma_dumb_create_internal
================================

*man drm_gem_cma_dumb_create_internal(9)*

*4.6.0-rc5*

create a dumb buffer object


Synopsis
========

.. c:function:: int drm_gem_cma_dumb_create_internal( struct drm_file * file_priv, struct drm_device * drm, struct drm_mode_create_dumb * args )

Arguments
=========

``file_priv``
    DRM file-private structure to create the dumb buffer for

``drm``
    DRM device

``args``
    IOCTL data


Description
===========

This aligns the pitch and size arguments to the minimum required. This
is an internal helper that can be wrapped by a driver to account for
hardware with more specific alignment requirements. It should not be
used directly as the ->``dumb_create`` callback in a DRM driver.


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
