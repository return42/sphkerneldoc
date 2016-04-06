.. -*- coding: utf-8; mode: rst -*-

===============
intel_hotplug.c
===============



.. _xref_intel_hpd_irq_storm_detect:

intel_hpd_irq_storm_detect
==========================

.. c:function:: bool intel_hpd_irq_storm_detect (struct drm_i915_private * dev_priv, enum hpd_pin pin)

    gather stats and detect HPD irq storm on a pin

    :param struct drm_i915_private * dev_priv:
        private driver data pointer

    :param enum hpd_pin pin:
        the pin to gather stats on



Description
-----------

Gather stats about HPD irqs from the specified **pin**, and detect irq
storms. Only the pin specific stats and state are changed, the caller is
responsible for further action.


**HPD_STORM_THRESHOLD** irqs are allowed within **HPD_STORM_DETECT_PERIOD** ms,
otherwise it's considered an irq storm, and the irq state is set to
**HPD_MARK_DISABLED**.


Return true if an irq storm was detected on **pin**.




.. _xref_intel_hpd_irq_handler:

intel_hpd_irq_handler
=====================

.. c:function:: void intel_hpd_irq_handler (struct drm_device * dev, u32 pin_mask, u32 long_mask)

    main hotplug irq handler

    :param struct drm_device * dev:
        drm device

    :param u32 pin_mask:
        a mask of hpd pins that have triggered the irq

    :param u32 long_mask:
        a mask of hpd pins that may be long hpd pulses



Description
-----------

This is the main hotplug irq handler for all platforms. The platform specific
irq handlers call the platform specific hotplug irq handlers, which read and
decode the appropriate registers into bitmasks about hpd pins that have
triggered (**pin_mask**), and which of those pins may be long pulses
(**long_mask**). The **long_mask** is ignored if the port corresponding to the pin
is not a digital port.


Here, we do hotplug irq storm detection and mitigation, and pass further
processing to appropriate bottom halves.




.. _xref_intel_hpd_init:

intel_hpd_init
==============

.. c:function:: void intel_hpd_init (struct drm_i915_private * dev_priv)

    initializes and enables hpd support

    :param struct drm_i915_private * dev_priv:
        i915 device instance



Description
-----------

This function enables the hotplug support. It requires that interrupts have
already been enabled with :c:func:`intel_irq_init_hw`. From this point on hotplug and
poll request can run concurrently to other code, so locking rules must be
obeyed.


This is a separate step from interrupt enabling to simplify the locking rules
in the driver load and resume code.


