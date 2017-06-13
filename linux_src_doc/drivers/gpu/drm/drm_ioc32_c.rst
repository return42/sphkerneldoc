.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_ioc32.c

.. _`drm_compat_ioctl`:

drm_compat_ioctl
================

.. c:function:: long drm_compat_ioctl(struct file *filp, unsigned int cmd, unsigned long arg)

    32bit IOCTL compatibility handler for DRM drivers

    :param struct file \*filp:
        file this ioctl is called on

    :param unsigned int cmd:
        ioctl cmd number

    :param unsigned long arg:
        user argument

.. _`drm_compat_ioctl.description`:

Description
-----------

Compatibility handler for 32 bit userspace running on 64 kernels. All actual
IOCTL handling is forwarded to \ :c:func:`drm_ioctl`\ , while marshalling structures as
appropriate. Note that this only handles DRM core IOCTLs, if the driver has
botched IOCTL itself, it must handle those by wrapping this function.

.. _`drm_compat_ioctl.return`:

Return
------

Zero on success, negative error code on failure.

.. This file was automatic generated / don't edit.

