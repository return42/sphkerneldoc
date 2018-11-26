.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_panel_orientation_quirks.c

.. _`drm_get_panel_orientation_quirk`:

drm_get_panel_orientation_quirk
===============================

.. c:function:: int drm_get_panel_orientation_quirk(int width, int height)

    Check for panel orientation quirks

    :param width:
        width in pixels of the panel
    :type width: int

    :param height:
        height in pixels of the panel
    :type height: int

.. _`drm_get_panel_orientation_quirk.description`:

Description
-----------

This function checks for platform specific (e.g. DMI based) quirks
providing info on panel_orientation for systems where this cannot be
probed from the hard-/firm-ware. To avoid false-positive this function
takes the panel resolution as argument and checks that against the
resolution expected by the quirk-table entry.

Note this function is also used outside of the drm-subsys, by for example
the efifb code. Because of this this function gets compiled into its own
kernel-module when built as a module.

.. _`drm_get_panel_orientation_quirk.return`:

Return
------

A DRM_MODE_PANEL_ORIENTATION_* value if there is a quirk for this system,
or DRM_MODE_PANEL_ORIENTATION_UNKNOWN if there is no quirk.

.. This file was automatic generated / don't edit.

