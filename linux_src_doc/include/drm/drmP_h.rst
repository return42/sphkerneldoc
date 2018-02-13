.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drmP.h

.. _`drm_drv_uses_atomic_modeset`:

drm_drv_uses_atomic_modeset
===========================

.. c:function:: bool drm_drv_uses_atomic_modeset(struct drm_device *dev)

    check if the driver implements \ :c:func:`atomic_commit`\ 

    :param struct drm_device \*dev:
        DRM device

.. _`drm_drv_uses_atomic_modeset.description`:

Description
-----------

This check is useful if drivers do not have DRIVER_ATOMIC set but
have atomic modesetting internally implemented.

.. This file was automatic generated / don't edit.

