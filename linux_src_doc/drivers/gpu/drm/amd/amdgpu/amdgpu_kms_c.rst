.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_kms.c

.. _`amdgpu_driver_unload_kms`:

amdgpu_driver_unload_kms
========================

.. c:function:: void amdgpu_driver_unload_kms(struct drm_device *dev)

    Main unload function for KMS.

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

.. _`amdgpu_driver_unload_kms.description`:

Description
-----------

This is the main unload function for KMS (all asics).
Returns 0 on success.

.. _`amdgpu_driver_load_kms`:

amdgpu_driver_load_kms
======================

.. c:function:: int amdgpu_driver_load_kms(struct drm_device *dev, unsigned long flags)

    Main load function for KMS.

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param flags:
        device flags
    :type flags: unsigned long

.. _`amdgpu_driver_load_kms.description`:

Description
-----------

This is the main load function for KMS (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_info_ioctl`:

amdgpu_info_ioctl
=================

.. c:function:: int amdgpu_info_ioctl(struct drm_device *dev, void *data, struct drm_file *filp)

    answer a device specific request.

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param data:
        request object
    :type data: void \*

    :param filp:
        drm filp
    :type filp: struct drm_file \*

.. _`amdgpu_info_ioctl.description`:

Description
-----------

This function is used to pass device specific parameters to the userspace
drivers.  Examples include: pci device id, pipeline parms, tiling params,
etc. (all asics).
Returns 0 on success, -EINVAL on failure.

.. _`amdgpu_driver_lastclose_kms`:

amdgpu_driver_lastclose_kms
===========================

.. c:function:: void amdgpu_driver_lastclose_kms(struct drm_device *dev)

    drm callback for last close

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

.. _`amdgpu_driver_lastclose_kms.description`:

Description
-----------

Switch vga_switcheroo state after last close (all asics).

.. _`amdgpu_driver_open_kms`:

amdgpu_driver_open_kms
======================

.. c:function:: int amdgpu_driver_open_kms(struct drm_device *dev, struct drm_file *file_priv)

    drm callback for open

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param file_priv:
        drm file
    :type file_priv: struct drm_file \*

.. _`amdgpu_driver_open_kms.description`:

Description
-----------

On device open, init vm on cayman+ (all asics).
Returns 0 on success, error on failure.

.. _`amdgpu_driver_postclose_kms`:

amdgpu_driver_postclose_kms
===========================

.. c:function:: void amdgpu_driver_postclose_kms(struct drm_device *dev, struct drm_file *file_priv)

    drm callback for post close

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param file_priv:
        drm file
    :type file_priv: struct drm_file \*

.. _`amdgpu_driver_postclose_kms.description`:

Description
-----------

On device post close, tear down vm on cayman+ (all asics).

.. _`amdgpu_get_vblank_counter_kms`:

amdgpu_get_vblank_counter_kms
=============================

.. c:function:: u32 amdgpu_get_vblank_counter_kms(struct drm_device *dev, unsigned int pipe)

    get frame count

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param pipe:
        crtc to get the frame count from
    :type pipe: unsigned int

.. _`amdgpu_get_vblank_counter_kms.description`:

Description
-----------

Gets the frame count on the requested crtc (all asics).
Returns frame count on success, -EINVAL on failure.

.. _`amdgpu_enable_vblank_kms`:

amdgpu_enable_vblank_kms
========================

.. c:function:: int amdgpu_enable_vblank_kms(struct drm_device *dev, unsigned int pipe)

    enable vblank interrupt

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param pipe:
        crtc to enable vblank interrupt for
    :type pipe: unsigned int

.. _`amdgpu_enable_vblank_kms.description`:

Description
-----------

Enable the interrupt on the requested crtc (all asics).
Returns 0 on success, -EINVAL on failure.

.. _`amdgpu_disable_vblank_kms`:

amdgpu_disable_vblank_kms
=========================

.. c:function:: void amdgpu_disable_vblank_kms(struct drm_device *dev, unsigned int pipe)

    disable vblank interrupt

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param pipe:
        crtc to disable vblank interrupt for
    :type pipe: unsigned int

.. _`amdgpu_disable_vblank_kms.description`:

Description
-----------

Disable the interrupt on the requested crtc (all asics).

.. This file was automatic generated / don't edit.

