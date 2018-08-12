.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/i915_irq.c

.. _`interrupt-handling`:

interrupt handling
==================

These functions provide the basic support for enabling and disabling the
interrupt handling support. There's a lot more functionality in i915_irq.c
and related files, but that will be described in separate chapters.

.. _`i915_hotplug_interrupt_update`:

i915_hotplug_interrupt_update
=============================

.. c:function:: void i915_hotplug_interrupt_update(struct drm_i915_private *dev_priv, uint32_t mask, uint32_t bits)

    update hotplug interrupt enable

    :param struct drm_i915_private \*dev_priv:
        driver private

    :param uint32_t mask:
        bits to update

    :param uint32_t bits:
        bits to enable
        NOTE: the HPD enable bits are modified both inside and outside
        of an interrupt context. To avoid that read-modify-write cycles
        interfer, these bits are protected by a spinlock. Since this
        function is usually not called from a context where the lock is
        held already, this function acquires the lock itself. A non-locking
        version is also available.

.. _`ilk_update_display_irq`:

ilk_update_display_irq
======================

.. c:function:: void ilk_update_display_irq(struct drm_i915_private *dev_priv, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update DEIMR

    :param struct drm_i915_private \*dev_priv:
        driver private

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable

.. _`ilk_update_gt_irq`:

ilk_update_gt_irq
=================

.. c:function:: void ilk_update_gt_irq(struct drm_i915_private *dev_priv, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update GTIMR

    :param struct drm_i915_private \*dev_priv:
        driver private

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable

.. _`snb_update_pm_irq`:

snb_update_pm_irq
=================

.. c:function:: void snb_update_pm_irq(struct drm_i915_private *dev_priv, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update GEN6_PMIMR

    :param struct drm_i915_private \*dev_priv:
        driver private

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable

.. _`bdw_update_port_irq`:

bdw_update_port_irq
===================

.. c:function:: void bdw_update_port_irq(struct drm_i915_private *dev_priv, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update DE port interrupt

    :param struct drm_i915_private \*dev_priv:
        driver private

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable

.. _`bdw_update_pipe_irq`:

bdw_update_pipe_irq
===================

.. c:function:: void bdw_update_pipe_irq(struct drm_i915_private *dev_priv, enum pipe pipe, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update DE pipe interrupt

    :param struct drm_i915_private \*dev_priv:
        driver private

    :param enum pipe pipe:
        pipe whose interrupt to update

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable

.. _`ibx_display_interrupt_update`:

ibx_display_interrupt_update
============================

.. c:function:: void ibx_display_interrupt_update(struct drm_i915_private *dev_priv, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update SDEIMR

    :param struct drm_i915_private \*dev_priv:
        driver private

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable

.. _`i915_enable_asle_pipestat`:

i915_enable_asle_pipestat
=========================

.. c:function:: void i915_enable_asle_pipestat(struct drm_i915_private *dev_priv)

    enable ASLE pipestat for OpRegion

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. _`ivybridge_parity_work`:

ivybridge_parity_work
=====================

.. c:function:: void ivybridge_parity_work(struct work_struct *work)

    Workqueue called when a parity error interrupt occurred.

    :param struct work_struct \*work:
        workqueue struct

.. _`ivybridge_parity_work.description`:

Description
-----------

Doesn't actually do anything except notify userspace. As a consequence of
this event, userspace should try to remap the bad rows since statistically
it is likely the same row is more likely to go bad again.

.. _`i915_handle_error`:

i915_handle_error
=================

.. c:function:: void i915_handle_error(struct drm_i915_private *dev_priv, u32 engine_mask, unsigned long flags, const char *fmt,  ...)

    handle a gpu error

    :param struct drm_i915_private \*dev_priv:
        i915 device private

    :param u32 engine_mask:
        mask representing engines that are hung

    :param unsigned long flags:
        control flags

    :param const char \*fmt:
        Error message format string

    :param ellipsis ellipsis:
        variable arguments

.. _`i915_handle_error.description`:

Description
-----------

Do some basic checking of register state at error time and
dump it to the syslog.  Also call \ :c:func:`i915_capture_error_state`\  to make
sure we get a record and make it available in debugfs.  Fire a uevent
so userspace knows something bad happened (should trigger collection
of a ring dump etc.).

.. _`intel_irq_init`:

intel_irq_init
==============

.. c:function:: void intel_irq_init(struct drm_i915_private *dev_priv)

    initializes irq support

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

.. _`intel_irq_init.description`:

Description
-----------

This function initializes all the irq support including work items, timers
and all the vtables. It does not setup the interrupt itself though.

.. _`intel_irq_fini`:

intel_irq_fini
==============

.. c:function:: void intel_irq_fini(struct drm_i915_private *i915)

    deinitializes IRQ support

    :param struct drm_i915_private \*i915:
        i915 device instance

.. _`intel_irq_fini.description`:

Description
-----------

This function deinitializes all the IRQ support.

.. _`intel_irq_install`:

intel_irq_install
=================

.. c:function:: int intel_irq_install(struct drm_i915_private *dev_priv)

    enables the hardware interrupt

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

.. _`intel_irq_install.description`:

Description
-----------

This function enables the hardware interrupt handling, but leaves the hotplug
handling still disabled. It is called after \ :c:func:`intel_irq_init`\ .

In the driver load and resume code we need working interrupts in a few places
but don't want to deal with the hassle of concurrent probe and hotplug
workers. Hence the split into this two-stage approach.

.. _`intel_irq_uninstall`:

intel_irq_uninstall
===================

.. c:function:: void intel_irq_uninstall(struct drm_i915_private *dev_priv)

    finilizes all irq handling

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

.. _`intel_irq_uninstall.description`:

Description
-----------

This stops interrupt and hotplug handling and unregisters and frees all
resources acquired in the init functions.

.. _`intel_runtime_pm_disable_interrupts`:

intel_runtime_pm_disable_interrupts
===================================

.. c:function:: void intel_runtime_pm_disable_interrupts(struct drm_i915_private *dev_priv)

    runtime interrupt disabling

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

.. _`intel_runtime_pm_disable_interrupts.description`:

Description
-----------

This function is used to disable interrupts at runtime, both in the runtime
pm and the system suspend/resume code.

.. _`intel_runtime_pm_enable_interrupts`:

intel_runtime_pm_enable_interrupts
==================================

.. c:function:: void intel_runtime_pm_enable_interrupts(struct drm_i915_private *dev_priv)

    runtime interrupt enabling

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

.. _`intel_runtime_pm_enable_interrupts.description`:

Description
-----------

This function is used to enable interrupts at runtime, both in the runtime
pm and the system suspend/resume code.

.. This file was automatic generated / don't edit.

