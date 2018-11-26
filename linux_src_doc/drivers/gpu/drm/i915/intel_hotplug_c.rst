.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_hotplug.c

.. _`hotplug`:

Hotplug
=======

Simply put, hotplug occurs when a display is connected to or disconnected
from the system. However, there may be adapters and docking stations and
Display Port short pulses and MST devices involved, complicating matters.

Hotplug in i915 is handled in many different levels of abstraction.

The platform dependent interrupt handling code in i915_irq.c enables,
disables, and does preliminary handling of the interrupts. The interrupt
handlers gather the hotplug detect (HPD) information from relevant registers
into a platform independent mask of hotplug pins that have fired.

The platform independent interrupt handler \ :c:func:`intel_hpd_irq_handler`\  in
intel_hotplug.c does hotplug irq storm detection and mitigation, and passes
further processing to appropriate bottom halves (Display Port specific and
regular hotplug).

The Display Port work function \ :c:func:`i915_digport_work_func`\  calls into
\ :c:func:`intel_dp_hpd_pulse`\  via hooks, which handles DP short pulses and DP MST long
pulses, with failures and non-MST long pulses triggering regular hotplug
processing on the connector.

The regular hotplug work function \ :c:func:`i915_hotplug_work_func`\  calls connector
detect hooks, and, if connector status changes, triggers sending of hotplug
uevent to userspace via \ :c:func:`drm_kms_helper_hotplug_event`\ .

Finally, the userspace is responsible for triggering a modeset upon receiving
the hotplug uevent, disabling or enabling the crtc as needed.

The hotplug interrupt storm detection and mitigation code keeps track of the
number of interrupts per hotplug pin per a period of time, and if the number
of interrupts exceeds a certain threshold, the interrupt is disabled for a
while before being re-enabled. The intention is to mitigate issues raising
from broken hardware triggering massive amounts of interrupts and grinding
the system to a halt.

Current implementation expects that hotplug interrupt storm will not be
seen when display port sink is connected, hence on platforms whose DP
callback is handled by i915_digport_work_func reenabling of hpd is not
performed (it was never expected to be disabled in the first place ;) )
this is specific to DP sinks handled by this routine and any other display
such as HDMI or DVI enabled on the same port will have proper logic since
it will use i915_hotplug_work_func where this logic is handled.

.. _`intel_hpd_pin_default`:

intel_hpd_pin_default
=====================

.. c:function:: enum hpd_pin intel_hpd_pin_default(struct drm_i915_private *dev_priv, enum port port)

    return default pin associated with certain port.

    :param dev_priv:
        private driver data pointer
    :type dev_priv: struct drm_i915_private \*

    :param port:
        the hpd port to get associated pin
    :type port: enum port

.. _`intel_hpd_pin_default.description`:

Description
-----------

It is only valid and used by digital port encoder.

Return pin that is associatade with \ ``port``\  and HDP_NONE if no pin is
hard associated with that \ ``port``\ .

.. _`intel_hpd_irq_storm_detect`:

intel_hpd_irq_storm_detect
==========================

.. c:function:: bool intel_hpd_irq_storm_detect(struct drm_i915_private *dev_priv, enum hpd_pin pin)

    gather stats and detect HPD irq storm on a pin

    :param dev_priv:
        private driver data pointer
    :type dev_priv: struct drm_i915_private \*

    :param pin:
        the pin to gather stats on
    :type pin: enum hpd_pin

.. _`intel_hpd_irq_storm_detect.description`:

Description
-----------

Gather stats about HPD irqs from the specified \ ``pin``\ , and detect irq
storms. Only the pin specific stats and state are changed, the caller is
responsible for further action.

The number of irqs that are allowed within \ ``HPD_STORM_DETECT_PERIOD``\  is
stored in \ ``dev_priv->hotplug.hpd_storm_threshold``\  which defaults to
\ ``HPD_STORM_DEFAULT_THRESHOLD``\ . If this threshold is exceeded, it's
considered an irq storm and the irq state is set to \ ``HPD_MARK_DISABLED``\ .

The HPD threshold can be controlled through i915_hpd_storm_ctl in debugfs,
and should only be adjusted for automated hotplug testing.

Return true if an irq storm was detected on \ ``pin``\ .

.. _`intel_hpd_irq_handler`:

intel_hpd_irq_handler
=====================

.. c:function:: void intel_hpd_irq_handler(struct drm_i915_private *dev_priv, u32 pin_mask, u32 long_mask)

    main hotplug irq handler

    :param dev_priv:
        drm_i915_private
    :type dev_priv: struct drm_i915_private \*

    :param pin_mask:
        a mask of hpd pins that have triggered the irq
    :type pin_mask: u32

    :param long_mask:
        a mask of hpd pins that may be long hpd pulses
    :type long_mask: u32

.. _`intel_hpd_irq_handler.description`:

Description
-----------

This is the main hotplug irq handler for all platforms. The platform specific
irq handlers call the platform specific hotplug irq handlers, which read and
decode the appropriate registers into bitmasks about hpd pins that have
triggered (@pin_mask), and which of those pins may be long pulses
(@long_mask). The \ ``long_mask``\  is ignored if the port corresponding to the pin
is not a digital port.

Here, we do hotplug irq storm detection and mitigation, and pass further
processing to appropriate bottom halves.

.. _`intel_hpd_init`:

intel_hpd_init
==============

.. c:function:: void intel_hpd_init(struct drm_i915_private *dev_priv)

    initializes and enables hpd support

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_hpd_init.description`:

Description
-----------

This function enables the hotplug support. It requires that interrupts have
already been enabled with \ :c:func:`intel_irq_init_hw`\ . From this point on hotplug and
poll request can run concurrently to other code, so locking rules must be
obeyed.

This is a separate step from interrupt enabling to simplify the locking rules
in the driver load and resume code.

Also see: \ :c:func:`intel_hpd_poll_init`\ , which enables connector polling

.. _`intel_hpd_poll_init`:

intel_hpd_poll_init
===================

.. c:function:: void intel_hpd_poll_init(struct drm_i915_private *dev_priv)

    enables/disables polling for connectors with hpd

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

.. _`intel_hpd_poll_init.description`:

Description
-----------

This function enables polling for all connectors, regardless of whether or
not they support hotplug detection. Under certain conditions HPD may not be
functional. On most Intel GPUs, this happens when we enter runtime suspend.
On Valleyview and Cherryview systems, this also happens when we shut off all
of the powerwells.

Since this function can get called in contexts where we're already holding
dev->mode_config.mutex, we do the actual hotplug enabling in a seperate
worker.

Also see: \ :c:func:`intel_hpd_init`\ , which restores hpd handling.

.. This file was automatic generated / don't edit.

