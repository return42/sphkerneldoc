.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-gem-cma-dumb-create:

=======================
drm_gem_cma_dumb_create
=======================

*man drm_gem_cma_dumb_create(9)*

*4.6.0-rc5*

create a dumb buffer object


Synopsis
========

.. c:function:: int drm_gem_cma_dumb_create( struct drm_file * file_priv, struct drm_device * drm, struct drm_mode_create_dumb * args )

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

This function computes the pitch of the dumb buffer and rounds it up to
an integer number of bytes per pixel. Drivers for hardware that doesn't
have any additional restrictions on the pitch can directly use this
function as their ->``dumb_create`` callback.

For hardware with additional restrictions, drivers can adjust the fields
set up by userspace and pass the IOCTL data along to the
``drm_gem_cma_dumb_create_internal`` function.


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
