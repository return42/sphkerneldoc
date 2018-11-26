.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/radeon/radeon_irq_kms.c

.. _`radeon_driver_irq_handler_kms`:

radeon_driver_irq_handler_kms
=============================

.. c:function:: irqreturn_t radeon_driver_irq_handler_kms(int irq, void *arg)

    irq handler for KMS

    :param irq:
        *undescribed*
    :type irq: int

    :param arg:
        *undescribed*
    :type arg: void \*

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

    :param work:
        work struct
    :type work: struct work_struct \*

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

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

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

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

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

    :param dev:
        drm dev pointer
    :type dev: struct drm_device \*

.. _`radeon_driver_irq_uninstall_kms.description`:

Description
-----------

This function disables all interrupt sources on the GPU (all asics).

.. _`radeon_msi_ok`:

radeon_msi_ok
=============

.. c:function:: bool radeon_msi_ok(struct radeon_device *rdev)

    asic specific msi checks

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

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

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

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

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

.. _`radeon_irq_kms_fini.description`:

Description
-----------

Tears down the work irq handlers, vblank handlers, MSIs, etc. (all asics).

.. _`radeon_irq_kms_sw_irq_get`:

radeon_irq_kms_sw_irq_get
=========================

.. c:function:: void radeon_irq_kms_sw_irq_get(struct radeon_device *rdev, int ring)

    enable software interrupt

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        ring whose interrupt you want to enable
    :type ring: int

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

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        ring whose interrupt you want to enable
    :type ring: int

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

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param ring:
        ring whose interrupt you want to disable
    :type ring: int

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

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param crtc:
        crtc whose interrupt you want to enable
    :type crtc: int

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

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param crtc:
        crtc whose interrupt you want to disable
    :type crtc: int

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

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param block:
        afmt block whose interrupt you want to enable
    :type block: int

.. _`radeon_irq_kms_enable_afmt.description`:

Description
-----------

Enables the afmt change interrupt for a specific afmt block (all asics).

.. _`radeon_irq_kms_disable_afmt`:

radeon_irq_kms_disable_afmt
===========================

.. c:function:: void radeon_irq_kms_disable_afmt(struct radeon_device *rdev, int block)

    disable audio format change interrupt

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param block:
        afmt block whose interrupt you want to disable
    :type block: int

.. _`radeon_irq_kms_disable_afmt.description`:

Description
-----------

Disables the afmt change interrupt for a specific afmt block (all asics).

.. _`radeon_irq_kms_enable_hpd`:

radeon_irq_kms_enable_hpd
=========================

.. c:function:: void radeon_irq_kms_enable_hpd(struct radeon_device *rdev, unsigned hpd_mask)

    enable hotplug detect interrupt

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param hpd_mask:
        mask of hpd pins you want to enable.
    :type hpd_mask: unsigned

.. _`radeon_irq_kms_enable_hpd.description`:

Description
-----------

Enables the hotplug detect interrupt for a specific hpd pin (all asics).

.. _`radeon_irq_kms_disable_hpd`:

radeon_irq_kms_disable_hpd
==========================

.. c:function:: void radeon_irq_kms_disable_hpd(struct radeon_device *rdev, unsigned hpd_mask)

    disable hotplug detect interrupt

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param hpd_mask:
        mask of hpd pins you want to disable.
    :type hpd_mask: unsigned

.. _`radeon_irq_kms_disable_hpd.description`:

Description
-----------

Disables the hotplug detect interrupt for a specific hpd pin (all asics).

.. _`radeon_irq_kms_set_irq_n_enabled`:

radeon_irq_kms_set_irq_n_enabled
================================

.. c:function:: void radeon_irq_kms_set_irq_n_enabled(struct radeon_device *rdev, u32 reg, u32 mask, bool enable, const char *name, unsigned n)

    helper for updating interrupt enable registers

    :param rdev:
        radeon device pointer
    :type rdev: struct radeon_device \*

    :param reg:
        the register to write to enable/disable interrupts
    :type reg: u32

    :param mask:
        the mask that enables the interrupts
    :type mask: u32

    :param enable:
        whether to enable or disable the interrupt register
    :type enable: bool

    :param name:
        the name of the interrupt register to print to the kernel log
    :type name: const char \*

    :param n:
        *undescribed*
    :type n: unsigned

.. _`radeon_irq_kms_set_irq_n_enabled.description`:

Description
-----------

Helper for updating the enable state of interrupt registers. Checks whether
or not the interrupt matches the enable state we want. If it doesn't, then
we update it and print a debugging message to the kernel log indicating the
new state of the interrupt register.

Used for updating sequences of interrupts registers like HPD1, HPD2, etc.

.. This file was automatic generated / don't edit.

