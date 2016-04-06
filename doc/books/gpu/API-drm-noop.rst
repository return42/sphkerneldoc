
.. _API-drm-noop:

========
drm_noop
========

*man drm_noop(9)*

*4.6.0-rc1*

DRM no-op ioctl implemntation


Synopsis
========

.. c:function:: int drm_noop( struct drm_device * dev, void * data, struct drm_file * file_priv )

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

This no-op implementation for drm ioctls is useful for deprecated functionality where we can't return a failure code because existing userspace checks the result of the ioctl, but
doesn't care about the action.

Always returns successfully with 0.
