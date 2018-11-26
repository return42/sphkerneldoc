.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/exynos/exynos_drm_ipp.c

.. _`exynos_drm_ipp_register`:

exynos_drm_ipp_register
=======================

.. c:function:: int exynos_drm_ipp_register(struct drm_device *dev, struct exynos_drm_ipp *ipp, const struct exynos_drm_ipp_funcs *funcs, unsigned int caps, const struct exynos_drm_ipp_formats *formats, unsigned int num_formats, const char *name)

    Register a new picture processor hardware module

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param ipp:
        ipp module to init
    :type ipp: struct exynos_drm_ipp \*

    :param funcs:
        callbacks for the new ipp object
    :type funcs: const struct exynos_drm_ipp_funcs \*

    :param caps:
        bitmask of ipp capabilities (%DRM_EXYNOS_IPP_CAP\_\*)
    :type caps: unsigned int

    :param formats:
        array of supported formats
    :type formats: const struct exynos_drm_ipp_formats \*

    :param num_formats:
        size of the supported formats array
    :type num_formats: unsigned int

    :param name:
        name (for debugging purposes)
    :type name: const char \*

.. _`exynos_drm_ipp_register.description`:

Description
-----------

Initializes a ipp module.

.. _`exynos_drm_ipp_register.return`:

Return
------

Zero on success, error code on failure.

.. _`exynos_drm_ipp_unregister`:

exynos_drm_ipp_unregister
=========================

.. c:function:: void exynos_drm_ipp_unregister(struct drm_device *dev, struct exynos_drm_ipp *ipp)

    Unregister the picture processor module

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param ipp:
        ipp module
    :type ipp: struct exynos_drm_ipp \*

.. _`exynos_drm_ipp_get_res_ioctl`:

exynos_drm_ipp_get_res_ioctl
============================

.. c:function:: int exynos_drm_ipp_get_res_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    enumerate all ipp modules

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param data:
        ioctl data
    :type data: void \*

    :param file_priv:
        DRM file info
    :type file_priv: struct drm_file \*

.. _`exynos_drm_ipp_get_res_ioctl.description`:

Description
-----------

Construct a list of ipp ids.

Called by the user via ioctl.

.. _`exynos_drm_ipp_get_res_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`exynos_drm_ipp_get_caps_ioctl`:

exynos_drm_ipp_get_caps_ioctl
=============================

.. c:function:: int exynos_drm_ipp_get_caps_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get ipp module capabilities and formats

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param data:
        ioctl data
    :type data: void \*

    :param file_priv:
        DRM file info
    :type file_priv: struct drm_file \*

.. _`exynos_drm_ipp_get_caps_ioctl.description`:

Description
-----------

Construct a structure describing ipp module capabilities.

Called by the user via ioctl.

.. _`exynos_drm_ipp_get_caps_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`exynos_drm_ipp_get_limits_ioctl`:

exynos_drm_ipp_get_limits_ioctl
===============================

.. c:function:: int exynos_drm_ipp_get_limits_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    get ipp module limits

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param data:
        ioctl data
    :type data: void \*

    :param file_priv:
        DRM file info
    :type file_priv: struct drm_file \*

.. _`exynos_drm_ipp_get_limits_ioctl.description`:

Description
-----------

Construct a structure describing ipp module limitations for provided
picture format.

Called by the user via ioctl.

.. _`exynos_drm_ipp_get_limits_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. _`exynos_drm_ipp_task_done`:

exynos_drm_ipp_task_done
========================

.. c:function:: void exynos_drm_ipp_task_done(struct exynos_drm_ipp_task *task, int ret)

    finish given task and set return code

    :param task:
        ipp task to finish
    :type task: struct exynos_drm_ipp_task \*

    :param ret:
        error code or 0 if operation has been performed successfully
    :type ret: int

.. _`exynos_drm_ipp_commit_ioctl`:

exynos_drm_ipp_commit_ioctl
===========================

.. c:function:: int exynos_drm_ipp_commit_ioctl(struct drm_device *dev, void *data, struct drm_file *file_priv)

    perform image processing operation

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param data:
        ioctl data
    :type data: void \*

    :param file_priv:
        DRM file info
    :type file_priv: struct drm_file \*

.. _`exynos_drm_ipp_commit_ioctl.description`:

Description
-----------

Construct a ipp task from the set of properties provided from the user
and try to schedule it to framebuffer processor hardware.

Called by the user via ioctl.

.. _`exynos_drm_ipp_commit_ioctl.return`:

Return
------

Zero on success, negative errno on failure.

.. This file was automatic generated / don't edit.

