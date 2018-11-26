.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_panel.c

.. _`intel_find_panel_downclock`:

intel_find_panel_downclock
==========================

.. c:function:: struct drm_display_mode *intel_find_panel_downclock(struct drm_i915_private *dev_priv, struct drm_display_mode *fixed_mode, struct drm_connector *connector)

    find the reduced downclock for LVDS in EDID

    :param dev_priv:
        i915 device instance
    :type dev_priv: struct drm_i915_private \*

    :param fixed_mode:
        panel native mode
    :type fixed_mode: struct drm_display_mode \*

    :param connector:
        LVDS/eDP connector
    :type connector: struct drm_connector \*

.. _`intel_find_panel_downclock.description`:

Description
-----------

Return downclock_avail
Find the reduced downclock for LVDS/eDP in EDID.

.. _`scale`:

scale
=====

.. c:function:: u32 scale(u32 source_val, u32 source_min, u32 source_max, u32 target_min, u32 target_max)

    scale values from one range to another

    :param source_val:
        value in range [@source_min..@source_max]
    :type source_val: u32

    :param source_min:
        minimum legal value for \ ``source_val``\ 
    :type source_min: u32

    :param source_max:
        maximum legal value for \ ``source_val``\ 
    :type source_max: u32

    :param target_min:
        corresponding target value for \ ``source_min``\ 
    :type target_min: u32

    :param target_max:
        corresponding target value for \ ``source_max``\ 
    :type target_max: u32

.. _`scale.description`:

Description
-----------

Return \ ``source_val``\  in range [@source_min..@source_max] scaled to range
[@target_min..@target_max].

.. This file was automatic generated / don't edit.

