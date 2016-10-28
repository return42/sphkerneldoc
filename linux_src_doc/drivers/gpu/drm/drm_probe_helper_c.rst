.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_probe_helper.c

.. _`drm_kms_helper_poll_enable_locked`:

drm_kms_helper_poll_enable_locked
=================================

.. c:function:: void drm_kms_helper_poll_enable_locked(struct drm_device *dev)

    re-enable output polling.

    :param struct drm_device \*dev:
        drm_device

.. _`drm_kms_helper_poll_enable_locked.description`:

Description
-----------

This function re-enables the output polling work without
locking the mode_config mutex.

This is like \ :c:func:`drm_kms_helper_poll_enable`\  however it is to be
called from a context where the mode_config mutex is locked
already.

.. _`drm_helper_probe_single_connector_modes`:

drm_helper_probe_single_connector_modes
=======================================

.. c:function:: int drm_helper_probe_single_connector_modes(struct drm_connector *connector, uint32_t maxX, uint32_t maxY)

    get complete set of display modes

    :param struct drm_connector \*connector:
        connector to probe

    :param uint32_t maxX:
        max width for modes

    :param uint32_t maxY:
        max height for modes

.. _`drm_helper_probe_single_connector_modes.description`:

Description
-----------

Based on the helper callbacks implemented by \ ``connector``\  in struct
\ :c:type:`struct drm_connector_helper_funcs <drm_connector_helper_funcs>` try to detect all valid modes.  Modes will first
be added to the connector's probed_modes list, then culled (based on validity
and the \ ``maxX``\ , \ ``maxY``\  parameters) and put into the normal modes list.

Intended to be used as a generic implementation of the ->\ :c:func:`fill_modes`\ 
\ ``connector``\  vfunc for drivers that use the CRTC helpers for output mode
filtering and detection.

The basic procedure is as follows

1. All modes currently on the connector's modes list are marked as stale

2. New modes are added to the connector's probed_modes list with
\ :c:func:`drm_mode_probed_add`\ . New modes start their life with status as OK.
Modes are added from a single source using the following priority order.

- debugfs 'override_edid' (used for testing only)
- firmware EDID (\ :c:func:`drm_load_edid_firmware`\ )
- connector helper ->\ :c:func:`get_modes`\  vfunc
- if the connector status is connector_status_connected, standard
VESA DMT modes up to 1024x768 are automatically added
(\ :c:func:`drm_add_modes_noedid`\ )

Finally modes specified via the kernel command line (video=...) are
added in addition to what the earlier probes produced
(\ :c:func:`drm_helper_probe_add_cmdline_mode`\ ). These modes are generated
using the VESA GTF/CVT formulas.

3. Modes are moved from the probed_modes list to the modes list. Potential
duplicates are merged together (see \ :c:func:`drm_mode_connector_list_update`\ ).
After this step the probed_modes list will be empty again.

4. Any non-stale mode on the modes list then undergoes validation

- \ :c:func:`drm_mode_validate_basic`\  performs basic sanity checks
- \ :c:func:`drm_mode_validate_size`\  filters out modes larger than \ ``maxX``\  and \ ``maxY``\ 
(if specified)
- \ :c:func:`drm_mode_validate_flag`\  checks the modes againt basic connector
capabilites (interlace_allowed,doublescan_allowed,stereo_allowed)
- the optional connector ->\ :c:func:`mode_valid`\  helper can perform driver and/or
hardware specific checks

5. Any mode whose status is not OK is pruned from the connector's modes list,
accompanied by a debug message indicating the reason for the mode's
rejection (see \ :c:func:`drm_mode_prune_invalid`\ ).

.. _`drm_helper_probe_single_connector_modes.return`:

Return
------

The number of modes found on \ ``connector``\ .

.. _`drm_kms_helper_hotplug_event`:

drm_kms_helper_hotplug_event
============================

.. c:function:: void drm_kms_helper_hotplug_event(struct drm_device *dev)

    fire off KMS hotplug events

    :param struct drm_device \*dev:
        drm_device whose connector state changed

.. _`drm_kms_helper_hotplug_event.description`:

Description
-----------

This function fires off the uevent for userspace and also calls the
output_poll_changed function, which is most commonly used to inform the fbdev
emulation code and allow it to update the fbcon output configuration.

Drivers should call this from their hotplug handling code when a change is
detected. Note that this function does not do any output detection of its
own, like \ :c:func:`drm_helper_hpd_irq_event`\  does - this is assumed to be done by the
driver already.

This function must be called from process context with no mode
setting locks held.

.. _`drm_kms_helper_poll_disable`:

drm_kms_helper_poll_disable
===========================

.. c:function:: void drm_kms_helper_poll_disable(struct drm_device *dev)

    disable output polling

    :param struct drm_device \*dev:
        drm_device

.. _`drm_kms_helper_poll_disable.description`:

Description
-----------

This function disables the output polling work.

Drivers can call this helper from their device suspend implementation. It is
not an error to call this even when output polling isn't enabled or arlready
disabled.

.. _`drm_kms_helper_poll_enable`:

drm_kms_helper_poll_enable
==========================

.. c:function:: void drm_kms_helper_poll_enable(struct drm_device *dev)

    re-enable output polling.

    :param struct drm_device \*dev:
        drm_device

.. _`drm_kms_helper_poll_enable.description`:

Description
-----------

This function re-enables the output polling work.

Drivers can call this helper from their device resume implementation. It is
an error to call this when the output polling support has not yet been set
up.

.. _`drm_kms_helper_poll_init`:

drm_kms_helper_poll_init
========================

.. c:function:: void drm_kms_helper_poll_init(struct drm_device *dev)

    initialize and enable output polling

    :param struct drm_device \*dev:
        drm_device

.. _`drm_kms_helper_poll_init.description`:

Description
-----------

This function intializes and then also enables output polling support for
\ ``dev``\ . Drivers which do not have reliable hotplug support in hardware can use
this helper infrastructure to regularly poll such connectors for changes in
their connection state.

Drivers can control which connectors are polled by setting the
DRM_CONNECTOR_POLL_CONNECT and DRM_CONNECTOR_POLL_DISCONNECT flags. On
connectors where probing live outputs can result in visual distortion drivers
should not set the DRM_CONNECTOR_POLL_DISCONNECT flag to avoid this.
Connectors which have no flag or only DRM_CONNECTOR_POLL_HPD set are
completely ignored by the polling logic.

Note that a connector can be both polled and probed from the hotplug handler,
in case the hotplug interrupt is known to be unreliable.

.. _`drm_kms_helper_poll_fini`:

drm_kms_helper_poll_fini
========================

.. c:function:: void drm_kms_helper_poll_fini(struct drm_device *dev)

    disable output polling and clean it up

    :param struct drm_device \*dev:
        drm_device

.. _`drm_helper_hpd_irq_event`:

drm_helper_hpd_irq_event
========================

.. c:function:: bool drm_helper_hpd_irq_event(struct drm_device *dev)

    hotplug processing

    :param struct drm_device \*dev:
        drm_device

.. _`drm_helper_hpd_irq_event.description`:

Description
-----------

Drivers can use this helper function to run a detect cycle on all connectors
which have the DRM_CONNECTOR_POLL_HPD flag set in their \ :c:type:`struct polled <polled>` member. All
other connectors are ignored, which is useful to avoid reprobing fixed
panels.

This helper function is useful for drivers which can't or don't track hotplug
interrupts for each connector.

Drivers which support hotplug interrupts for each connector individually and
which have a more fine-grained detect logic should bypass this code and
directly call \ :c:func:`drm_kms_helper_hotplug_event`\  in case the connector state
changed.

This function must be called from process context with no mode
setting locks held.

Note that a connector can be both polled and probed from the hotplug handler,
in case the hotplug interrupt is known to be unreliable.

.. This file was automatic generated / don't edit.

