.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_kms.c

.. _`radeon_driver_unload_kms`:

radeon_driver_unload_kms
========================

.. c:function:: void radeon_driver_unload_kms(struct drm_device *dev)

    Main unload function for KMS.

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

.. _`radeon_driver_unload_kms.description`:

Description
-----------

This is the main unload function for KMS (all asics).
It calls \ :c:func:`radeon_modeset_fini`\  to tear down the
displays, and \ :c:func:`radeon_device_fini`\  to tear down
the rest of the device (CP, writeback, etc.).
Returns 0 on success.

.. _`radeon_driver_load_kms`:

radeon_driver_load_kms
======================

.. c:function:: int radeon_driver_load_kms(struct drm_device *dev, unsigned long flags)

    Main load function for KMS.

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param flags:
        device flags
    :type flags: unsigned long

.. _`radeon_driver_load_kms.description`:

Description
-----------

This is the main load function for KMS (all asics).
It calls \ :c:func:`radeon_device_init`\  to set up the non-display
parts of the chip (asic init, CP, writeback, etc.), and
\ :c:func:`radeon_modeset_init`\  to set up the display parts
(crtcs, encoders, hotplug detect, etc.).
Returns 0 on success, error on failure.

.. _`radeon_set_filp_rights`:

radeon_set_filp_rights
======================

.. c:function:: void radeon_set_filp_rights(struct drm_device *dev, struct drm_file **owner, struct drm_file *applier, uint32_t *value)

    Set filp right.

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param owner:
        drm file
    :type owner: struct drm_file \*\*

    :param applier:
        drm file
    :type applier: struct drm_file \*

    :param value:
        value
    :type value: uint32_t \*

.. _`radeon_set_filp_rights.description`:

Description
-----------

Sets the filp rights for the device (all asics).

.. _`radeon_info_ioctl`:

radeon_info_ioctl
=================

.. c:function:: int radeon_info_ioctl(struct drm_device *dev, void *data, struct drm_file *filp)

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

.. _`radeon_info_ioctl.description`:

Description
-----------

This function is used to pass device specific parameters to the userspace
drivers.  Examples include: pci device id, pipeline parms, tiling params,
etc. (all asics).
Returns 0 on success, -EINVAL on failure.

.. _`radeon_driver_lastclose_kms`:

radeon_driver_lastclose_kms
===========================

.. c:function:: void radeon_driver_lastclose_kms(struct drm_device *dev)

    drm callback for last close

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

.. _`radeon_driver_lastclose_kms.description`:

Description
-----------

Switch vga_switcheroo state after last close (all asics).

.. _`radeon_driver_open_kms`:

radeon_driver_open_kms
======================

.. c:function:: int radeon_driver_open_kms(struct drm_device *dev, struct drm_file *file_priv)

    drm callback for open

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param file_priv:
        drm file
    :type file_priv: struct drm_file \*

.. _`radeon_driver_open_kms.description`:

Description
-----------

On device open, init vm on cayman+ (all asics).
Returns 0 on success, error on failure.

.. _`radeon_driver_postclose_kms`:

radeon_driver_postclose_kms
===========================

.. c:function:: void radeon_driver_postclose_kms(struct drm_device *dev, struct drm_file *file_priv)

    drm callback for post close

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param file_priv:
        drm file
    :type file_priv: struct drm_file \*

.. _`radeon_driver_postclose_kms.description`:

Description
-----------

On device close, tear down hyperz and cmask filps on r1xx-r5xx
(all asics).  And tear down vm on cayman+ (all asics).

.. _`radeon_get_vblank_counter_kms`:

radeon_get_vblank_counter_kms
=============================

.. c:function:: u32 radeon_get_vblank_counter_kms(struct drm_device *dev, unsigned int pipe)

    get frame count

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param pipe:
        crtc to get the frame count from
    :type pipe: unsigned int

.. _`radeon_get_vblank_counter_kms.description`:

Description
-----------

Gets the frame count on the requested crtc (all asics).
Returns frame count on success, -EINVAL on failure.

.. _`radeon_enable_vblank_kms`:

radeon_enable_vblank_kms
========================

.. c:function:: int radeon_enable_vblank_kms(struct drm_device *dev, int crtc)

    enable vblank interrupt

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param crtc:
        crtc to enable vblank interrupt for
    :type crtc: int

.. _`radeon_enable_vblank_kms.description`:

Description
-----------

Enable the interrupt on the requested crtc (all asics).
Returns 0 on success, -EINVAL on failure.

.. _`radeon_disable_vblank_kms`:

radeon_disable_vblank_kms
=========================

.. c:function:: void radeon_disable_vblank_kms(struct drm_device *dev, int crtc)

    disable vblank interrupt

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

    :param crtc:
        crtc to disable vblank interrupt for
    :type crtc: int

.. _`radeon_disable_vblank_kms.description`:

Description
-----------

Disable the interrupt on the requested crtc (all asics).

.. This file was automatic generated / don't edit.

