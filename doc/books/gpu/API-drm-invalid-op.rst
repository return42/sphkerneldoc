
.. _API-drm-invalid-op:

==============
drm_invalid_op
==============

*man drm_invalid_op(9)*

*4.6.0-rc1*

DRM invalid ioctl implemntation


Synopsis
========

.. c:function:: int drm_invalid_op( struct drm_device * dev, void * data, struct drm_file * file_priv )

Arguments
=========

``dev``
    DRM device for the ioctl

``data``
    data pointer for the ioctl

``file_priv``
    DRM file for the ioctl call


Description
===========

This no-op implementation for drm ioctls is useful for deprecated functionality where we really don't want to allow userspace to call the ioctl any more. This is the case for old
ums interfaces for drivers that transitioned to kms gradually and so kept the old legacy tables around. This only applies to radeon and i915 kms drivers, other drivers shouldn't
need to use this function.

Always fails with a return value of -EINVAL.
