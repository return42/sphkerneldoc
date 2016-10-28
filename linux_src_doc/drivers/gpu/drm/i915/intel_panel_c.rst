.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_panel.c

.. _`intel_find_panel_downclock`:

intel_find_panel_downclock
==========================

.. c:function:: struct drm_display_mode *intel_find_panel_downclock(struct drm_device *dev, struct drm_display_mode *fixed_mode, struct drm_connector *connector)

    find the reduced downclock for LVDS in EDID

    :param struct drm_device \*dev:
        drm device

    :param struct drm_display_mode \*fixed_mode:
        panel native mode

    :param struct drm_connector \*connector:
        LVDS/eDP connector

.. _`intel_find_panel_downclock.description`:

Description
-----------

Return downclock_avail
Find the reduced downclock for LVDS/eDP in EDID.

.. _`scale`:

scale
=====

.. c:function:: uint32_t scale(uint32_t source_val, uint32_t source_min, uint32_t source_max, uint32_t target_min, uint32_t target_max)

    scale values from one range to another

    :param uint32_t source_val:
        value in range [\ ``source_min``\ ..\ ``source_max``\ ]

    :param uint32_t source_min:
        *undescribed*

    :param uint32_t source_max:
        *undescribed*

    :param uint32_t target_min:
        *undescribed*

    :param uint32_t target_max:
        *undescribed*

.. _`scale.description`:

Description
-----------

Return \ ``source_val``\  in range [\ ``source_min``\ ..\ ``source_max``\ ] scaled to range
[\ ``target_min``\ ..\ ``target_max``\ ].

.. This file was automatic generated / don't edit.

