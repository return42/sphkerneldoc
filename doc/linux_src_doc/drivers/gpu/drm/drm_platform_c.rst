.. -*- coding: utf-8; mode: rst -*-

==============
drm_platform.c
==============

.. _`drm_platform_init`:

drm_platform_init
=================

.. c:function:: int drm_platform_init (struct drm_driver *driver, struct platform_device *platform_device)

    Register a platform device with the DRM subsystem

    :param struct drm_driver \*driver:
        DRM device driver

    :param struct platform_device \*platform_device:
        platform device to register


.. _`drm_platform_init.description`:

Description
-----------

Registers the specified DRM device driver and platform device with the DRM
subsystem, initializing a drm_device structure and calling the driver's
.:c:func:`load` function.

NOTE: This function is deprecated, please use :c:func:`drm_dev_alloc` and
:c:func:`drm_dev_register` instead and remove your ->:c:func:`load` callback.

Return: 0 on success or a negative error code on failure.

