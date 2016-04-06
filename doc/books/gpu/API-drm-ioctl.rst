
.. _API-drm-ioctl:

=========
drm_ioctl
=========

*man drm_ioctl(9)*

*4.6.0-rc1*

ioctl callback implementation for DRM drivers


Synopsis
========

.. c:function:: long drm_ioctl( struct file * filp, unsigned int cmd, unsigned long arg )

Arguments
=========

``filp``
    file this ioctl is called on

``cmd``
    ioctl cmd number

``arg``
    user argument


Looks up the ioctl function in the
==================================

:ioctls table, checking for root previleges if so required, and dispatches to the respective function.


Returns
=======

Zero on success, negative error code on failure.
