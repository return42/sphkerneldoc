
.. _API-drm-helper-probe-single-connector-modes:

=======================================
drm_helper_probe_single_connector_modes
=======================================

*man drm_helper_probe_single_connector_modes(9)*

*4.6.0-rc1*

get complete set of display modes


Synopsis
========

.. c:function:: int drm_helper_probe_single_connector_modes( struct drm_connector * connector, uint32_t maxX, uint32_t maxY )

Arguments
=========

``connector``
    connector to probe

``maxX``
    max width for modes

``maxY``
    max height for modes


Description
===========

Based on the helper callbacks implemented by ``connector`` in struct ``drm_connector_helper_funcs`` try to detect all valid modes. Modes will first be added to the connector's
probed_modes list, then culled (based on validity and the ``maxX``, ``maxY`` parameters) and put into the normal modes list.

Intended to be used as a generic implementation of the ->``fill_modes`` ``connector`` vfunc for drivers that use the CRTC helpers for output mode filtering and detection.

The basic procedure is as follows

1. All modes currently on the connector's modes list are marked as stale

2. New modes are added to the connector's probed_modes list with ``drm_mode_probed_add``. New modes start their life with status as OK. Modes are added from a single source using
the following priority order.

- debugfs 'override_edid' (used for testing only) - firmware EDID (``drm_load_edid_firmware``) - connector helper ->``get_modes`` vfunc - if the connector status is
connector_status_connected, standard VESA DMT modes up to 1024x768 are automatically added (``drm_add_modes_noedid``)

Finally modes specified via the kernel command line (video=...) are added in addition to what the earlier probes produced (``drm_helper_probe_add_cmdline_mode``). These modes are
generated using the VESA GTF/CVT formulas.

3. Modes are moved from the probed_modes list to the modes list. Potential duplicates are merged together (see ``drm_mode_connector_list_update``). After this step the
probed_modes list will be empty again.

4. Any non-stale mode on the modes list then undergoes validation

- ``drm_mode_validate_basic`` performs basic sanity checks - ``drm_mode_validate_size`` filters out modes larger than ``maxX`` and ``maxY`` (if specified) -
``drm_mode_validate_flag`` checks the modes againt basic connector capabilites (interlace_allowed,doublescan_allowed,stereo_allowed) - the optional connector ->``mode_valid``
helper can perform driver and/or hardware specific checks

5. Any mode whose status is not OK is pruned from the connector's modes list, accompanied by a debug message indicating the reason for the mode's rejection (see
``drm_mode_prune_invalid``).


Returns
=======

The number of modes found on ``connector``.
