.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/amd/amdgpu/amdgpu_kms.c

.. _`amdgpu_driver_unload_kms`:

amdgpu_driver_unload_kms
========================

.. c:function:: void amdgpu_driver_unload_kms(struct drm_device *dev)

    Main unload function for KMS.

    :param struct drm_device \*dev:
        drm dev pointer

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

    :param struct drm_device \*dev:
        drm dev pointer

    :param unsigned long flags:
        device flags

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

    :param struct drm_device \*dev:
        *undescribed*

    :param void \*data:
        request object

    :param struct drm_file \*filp:
        drm filp

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

    :param struct drm_device \*dev:
        drm dev pointer

.. _`amdgpu_driver_lastclose_kms.description`:

Description
-----------

Switch vga_switcheroo state after last close (all asics).

.. _`amdgpu_driver_open_kms`:

amdgpu_driver_open_kms
======================

.. c:function:: int amdgpu_driver_open_kms(struct drm_device *dev, struct drm_file *file_priv)

    drm callback for open

    :param struct drm_device \*dev:
        drm dev pointer

    :param struct drm_file \*file_priv:
        drm file

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

    :param struct drm_device \*dev:
        drm dev pointer

    :param struct drm_file \*file_priv:
        drm file

.. _`amdgpu_driver_postclose_kms.description`:

Description
-----------

On device post close, tear down vm on cayman+ (all asics).

.. _`amdgpu_get_vblank_counter_kms`:

amdgpu_get_vblank_counter_kms
=============================

.. c:function:: u32 amdgpu_get_vblank_counter_kms(struct drm_device *dev, unsigned int pipe)

    get frame count

    :param struct drm_device \*dev:
        drm dev pointer

    :param unsigned int pipe:
        crtc to get the frame count from

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

    :param struct drm_device \*dev:
        drm dev pointer

    :param unsigned int pipe:
        crtc to enable vblank interrupt for

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

    :param struct drm_device \*dev:
        drm dev pointer

    :param unsigned int pipe:
        crtc to disable vblank interrupt for

.. _`amdgpu_disable_vblank_kms.description`:

Description
-----------

Disable the interrupt on the requested crtc (all asics).

.. _`amdgpu_get_vblank_timestamp_kms`:

amdgpu_get_vblank_timestamp_kms
===============================

.. c:function:: int amdgpu_get_vblank_timestamp_kms(struct drm_device *dev, unsigned int pipe, int *max_error, struct timeval *vblank_time, unsigned flags)

    get vblank timestamp

    :param struct drm_device \*dev:
        drm dev pointer

    :param unsigned int pipe:
        *undescribed*

    :param int \*max_error:
        max error

    :param struct timeval \*vblank_time:
        time value

    :param unsigned flags:
        flags passed to the driver

.. _`amdgpu_get_vblank_timestamp_kms.description`:

Description
-----------

Gets the timestamp on the requested crtc based on the
scanout position.  (all asics).
Returns postive status flags on success, negative error on failure.

.. This file was automatic generated / don't edit.

