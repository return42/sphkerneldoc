.. -*- coding: utf-8; mode: rst -*-

==========
i915_irq.c
==========



.. _xref_i915_hotplug_interrupt_update:

i915_hotplug_interrupt_update
=============================

.. c:function:: void i915_hotplug_interrupt_update (struct drm_i915_private * dev_priv, uint32_t mask, uint32_t bits)

    update hotplug interrupt enable

    :param struct drm_i915_private * dev_priv:
        driver private

    :param uint32_t mask:
        bits to update

    :param uint32_t bits:
        bits to enable



NOTE
----

the HPD enable bits are modified both inside and outside
of an interrupt context. To avoid that read-modify-write cycles
interfer, these bits are protected by a spinlock. Since this
function is usually not called from a context where the lock is
held already, this function acquires the lock itself. A non-locking
version is also available.




.. _xref_ilk_update_display_irq:

ilk_update_display_irq
======================

.. c:function:: void ilk_update_display_irq (struct drm_i915_private * dev_priv, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update DEIMR

    :param struct drm_i915_private * dev_priv:
        driver private

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable




.. _xref_ilk_update_gt_irq:

ilk_update_gt_irq
=================

.. c:function:: void ilk_update_gt_irq (struct drm_i915_private * dev_priv, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update GTIMR

    :param struct drm_i915_private * dev_priv:
        driver private

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable




.. _xref_snb_update_pm_irq:

snb_update_pm_irq
=================

.. c:function:: void snb_update_pm_irq (struct drm_i915_private * dev_priv, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update GEN6_PMIMR

    :param struct drm_i915_private * dev_priv:
        driver private

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable




.. _xref_bdw_update_port_irq:

bdw_update_port_irq
===================

.. c:function:: void bdw_update_port_irq (struct drm_i915_private * dev_priv, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update DE port interrupt

    :param struct drm_i915_private * dev_priv:
        driver private

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable




.. _xref_bdw_update_pipe_irq:

bdw_update_pipe_irq
===================

.. c:function:: void bdw_update_pipe_irq (struct drm_i915_private * dev_priv, enum pipe pipe, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update DE pipe interrupt

    :param struct drm_i915_private * dev_priv:
        driver private

    :param enum pipe pipe:
        pipe whose interrupt to update

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable




.. _xref_ibx_display_interrupt_update:

ibx_display_interrupt_update
============================

.. c:function:: void ibx_display_interrupt_update (struct drm_i915_private * dev_priv, uint32_t interrupt_mask, uint32_t enabled_irq_mask)

    update SDEIMR

    :param struct drm_i915_private * dev_priv:
        driver private

    :param uint32_t interrupt_mask:
        mask of interrupt bits to update

    :param uint32_t enabled_irq_mask:
        mask of interrupt bits to enable




.. _xref_i915_enable_asle_pipestat:

i915_enable_asle_pipestat
=========================

.. c:function:: void i915_enable_asle_pipestat (struct drm_device * dev)

    enable ASLE pipestat for OpRegion

    :param struct drm_device * dev:
        drm device




.. _xref_ivybridge_parity_work:

ivybridge_parity_work
=====================

.. c:function:: void ivybridge_parity_work (struct work_struct * work)

    Workqueue called when a parity error interrupt occurred.

    :param struct work_struct * work:
        workqueue struct



Description
-----------

Doesn't actually do anything except notify userspace. As a consequence of
this event, userspace should try to remap the bad rows since statistically
it is likely the same row is more likely to go bad again.




.. _xref_i915_reset_and_wakeup:

i915_reset_and_wakeup
=====================

.. c:function:: void i915_reset_and_wakeup (struct drm_device * dev)

    do process context error handling work

    :param struct drm_device * dev:
        drm device



Description
-----------

Fire an error uevent so userspace can see that a hang or error
was detected.




.. _xref_i915_handle_error:

i915_handle_error
=================

.. c:function:: void i915_handle_error (struct drm_device * dev, bool wedged, const char * fmt,  ...)

    handle a gpu error

    :param struct drm_device * dev:
        drm device

    :param bool wedged:

        _undescribed_

    :param const char * fmt:

        _undescribed_

    :param ...:
        variable arguments



Description
-----------

Do some basic checking of register state at error time and
dump it to the syslog.  Also call :c:func:`i915_capture_error_state` to make
sure we get a record and make it available in debugfs.  Fire a uevent
so userspace knows something bad happened (should trigger collection
of a ring dump etc.).




.. _xref_intel_irq_init:

intel_irq_init
==============

.. c:function:: void intel_irq_init (struct drm_i915_private * dev_priv)

    initializes irq support

    :param struct drm_i915_private * dev_priv:
        i915 device instance



Description
-----------

This function initializes all the irq support including work items, timers
and all the vtables. It does not setup the interrupt itself though.




.. _xref_intel_irq_install:

intel_irq_install
=================

.. c:function:: int intel_irq_install (struct drm_i915_private * dev_priv)

    enables the hardware interrupt

    :param struct drm_i915_private * dev_priv:
        i915 device instance



Description
-----------

This function enables the hardware interrupt handling, but leaves the hotplug
handling still disabled. It is called after :c:func:`intel_irq_init`.


In the driver load and resume code we need working interrupts in a few places
but don't want to deal with the hassle of concurrent probe and hotplug
workers. Hence the split into this two-stage approach.




.. _xref_intel_irq_uninstall:

intel_irq_uninstall
===================

.. c:function:: void intel_irq_uninstall (struct drm_i915_private * dev_priv)

    finilizes all irq handling

    :param struct drm_i915_private * dev_priv:
        i915 device instance



Description
-----------

This stops interrupt and hotplug handling and unregisters and frees all
resources acquired in the init functions.




.. _xref_intel_runtime_pm_disable_interrupts:

intel_runtime_pm_disable_interrupts
===================================

.. c:function:: void intel_runtime_pm_disable_interrupts (struct drm_i915_private * dev_priv)

    runtime interrupt disabling

    :param struct drm_i915_private * dev_priv:
        i915 device instance



Description
-----------

This function is used to disable interrupts at runtime, both in the runtime
pm and the system suspend/resume code.




.. _xref_intel_runtime_pm_enable_interrupts:

intel_runtime_pm_enable_interrupts
==================================

.. c:function:: void intel_runtime_pm_enable_interrupts (struct drm_i915_private * dev_priv)

    runtime interrupt enabling

    :param struct drm_i915_private * dev_priv:
        i915 device instance



Description
-----------

This function is used to enable interrupts at runtime, both in the runtime
pm and the system suspend/resume code.


