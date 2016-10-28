.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_irq_kms.c

.. _`radeon_driver_irq_handler_kms`:

radeon_driver_irq_handler_kms
=============================

.. c:function:: irqreturn_t radeon_driver_irq_handler_kms(int irq, void *arg)

    irq handler for KMS

    :param int irq:
        *undescribed*

    :param void \*arg:
        *undescribed*

.. _`radeon_driver_irq_handler_kms.description`:

Description
-----------

This is the irq handler for the radeon KMS driver (all asics).
radeon_irq_process is a macro that points to the per-asic
irq handler callback.

.. _`radeon_hotplug_work_func`:

radeon_hotplug_work_func
========================

.. c:function:: void radeon_hotplug_work_func(struct work_struct *work)

    display hotplug work handler

    :param struct work_struct \*work:
        work struct

.. _`radeon_hotplug_work_func.description`:

Description
-----------

This is the hot plug event work handler (all asics).
The work gets scheduled from the irq handler if there
was a hot plug interrupt.  It walks the connector table
and calls the hotplug handler for each one, then sends
a drm hotplug event to alert userspace.

.. _`radeon_driver_irq_preinstall_kms`:

radeon_driver_irq_preinstall_kms
================================

.. c:function:: void radeon_driver_irq_preinstall_kms(struct drm_device *dev)

    drm irq preinstall callback

    :param struct drm_device \*dev:
        drm dev pointer

.. _`radeon_driver_irq_preinstall_kms.description`:

Description
-----------

Gets the hw ready to enable irqs (all asics).
This function disables all interrupt sources on the GPU.

.. _`radeon_driver_irq_postinstall_kms`:

radeon_driver_irq_postinstall_kms
=================================

.. c:function:: int radeon_driver_irq_postinstall_kms(struct drm_device *dev)

    drm irq preinstall callback

    :param struct drm_device \*dev:
        drm dev pointer

.. _`radeon_driver_irq_postinstall_kms.description`:

Description
-----------

Handles stuff to be done after enabling irqs (all asics).
Returns 0 on success.

.. _`radeon_driver_irq_uninstall_kms`:

radeon_driver_irq_uninstall_kms
===============================

.. c:function:: void radeon_driver_irq_uninstall_kms(struct drm_device *dev)

    drm irq uninstall callback

    :param struct drm_device \*dev:
        drm dev pointer

.. _`radeon_driver_irq_uninstall_kms.description`:

Description
-----------

This function disables all interrupt sources on the GPU (all asics).

.. _`radeon_msi_ok`:

radeon_msi_ok
=============

.. c:function:: bool radeon_msi_ok(struct radeon_device *rdev)

    asic specific msi checks

    :param struct radeon_device \*rdev:
        radeon device pointer

.. _`radeon_msi_ok.description`:

Description
-----------

Handles asic specific MSI checks to determine if
MSIs should be enabled on a particular chip (all asics).
Returns true if MSIs should be enabled, false if MSIs
should not be enabled.

.. _`radeon_irq_kms_init`:

radeon_irq_kms_init
===================

.. c:function:: int radeon_irq_kms_init(struct radeon_device *rdev)

    init driver interrupt info

    :param struct radeon_device \*rdev:
        radeon device pointer

.. _`radeon_irq_kms_init.description`:

Description
-----------

Sets up the work irq handlers, vblank init, MSIs, etc. (all asics).
Returns 0 for success, error for failure.

.. _`radeon_irq_kms_fini`:

radeon_irq_kms_fini
===================

.. c:function:: void radeon_irq_kms_fini(struct radeon_device *rdev)

    tear down driver interrupt info

    :param struct radeon_device \*rdev:
        radeon device pointer

.. _`radeon_irq_kms_fini.description`:

Description
-----------

Tears down the work irq handlers, vblank handlers, MSIs, etc. (all asics).

.. _`radeon_irq_kms_sw_irq_get`:

radeon_irq_kms_sw_irq_get
=========================

.. c:function:: void radeon_irq_kms_sw_irq_get(struct radeon_device *rdev, int ring)

    enable software interrupt

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int ring:
        ring whose interrupt you want to enable

.. _`radeon_irq_kms_sw_irq_get.description`:

Description
-----------

Enables the software interrupt for a specific ring (all asics).
The software interrupt is generally used to signal a fence on
a particular ring.

.. _`radeon_irq_kms_sw_irq_get_delayed`:

radeon_irq_kms_sw_irq_get_delayed
=================================

.. c:function:: bool radeon_irq_kms_sw_irq_get_delayed(struct radeon_device *rdev, int ring)

    enable software interrupt

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int ring:
        ring whose interrupt you want to enable

.. _`radeon_irq_kms_sw_irq_get_delayed.description`:

Description
-----------

Enables the software interrupt for a specific ring (all asics).
The software interrupt is generally used to signal a fence on
a particular ring.

.. _`radeon_irq_kms_sw_irq_put`:

radeon_irq_kms_sw_irq_put
=========================

.. c:function:: void radeon_irq_kms_sw_irq_put(struct radeon_device *rdev, int ring)

    disable software interrupt

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int ring:
        ring whose interrupt you want to disable

.. _`radeon_irq_kms_sw_irq_put.description`:

Description
-----------

Disables the software interrupt for a specific ring (all asics).
The software interrupt is generally used to signal a fence on
a particular ring.

.. _`radeon_irq_kms_pflip_irq_get`:

radeon_irq_kms_pflip_irq_get
============================

.. c:function:: void radeon_irq_kms_pflip_irq_get(struct radeon_device *rdev, int crtc)

    enable pageflip interrupt

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int crtc:
        crtc whose interrupt you want to enable

.. _`radeon_irq_kms_pflip_irq_get.description`:

Description
-----------

Enables the pageflip interrupt for a specific crtc (all asics).
For pageflips we use the vblank interrupt source.

.. _`radeon_irq_kms_pflip_irq_put`:

radeon_irq_kms_pflip_irq_put
============================

.. c:function:: void radeon_irq_kms_pflip_irq_put(struct radeon_device *rdev, int crtc)

    disable pageflip interrupt

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int crtc:
        crtc whose interrupt you want to disable

.. _`radeon_irq_kms_pflip_irq_put.description`:

Description
-----------

Disables the pageflip interrupt for a specific crtc (all asics).
For pageflips we use the vblank interrupt source.

.. _`radeon_irq_kms_enable_afmt`:

radeon_irq_kms_enable_afmt
==========================

.. c:function:: void radeon_irq_kms_enable_afmt(struct radeon_device *rdev, int block)

    enable audio format change interrupt

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int block:
        afmt block whose interrupt you want to enable

.. _`radeon_irq_kms_enable_afmt.description`:

Description
-----------

Enables the afmt change interrupt for a specific afmt block (all asics).

.. _`radeon_irq_kms_disable_afmt`:

radeon_irq_kms_disable_afmt
===========================

.. c:function:: void radeon_irq_kms_disable_afmt(struct radeon_device *rdev, int block)

    disable audio format change interrupt

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param int block:
        afmt block whose interrupt you want to disable

.. _`radeon_irq_kms_disable_afmt.description`:

Description
-----------

Disables the afmt change interrupt for a specific afmt block (all asics).

.. _`radeon_irq_kms_enable_hpd`:

radeon_irq_kms_enable_hpd
=========================

.. c:function:: void radeon_irq_kms_enable_hpd(struct radeon_device *rdev, unsigned hpd_mask)

    enable hotplug detect interrupt

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param unsigned hpd_mask:
        mask of hpd pins you want to enable.

.. _`radeon_irq_kms_enable_hpd.description`:

Description
-----------

Enables the hotplug detect interrupt for a specific hpd pin (all asics).

.. _`radeon_irq_kms_disable_hpd`:

radeon_irq_kms_disable_hpd
==========================

.. c:function:: void radeon_irq_kms_disable_hpd(struct radeon_device *rdev, unsigned hpd_mask)

    disable hotplug detect interrupt

    :param struct radeon_device \*rdev:
        radeon device pointer

    :param unsigned hpd_mask:
        mask of hpd pins you want to disable.

.. _`radeon_irq_kms_disable_hpd.description`:

Description
-----------

Disables the hotplug detect interrupt for a specific hpd pin (all asics).

.. This file was automatic generated / don't edit.

