.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_dvo.c

.. _`intel_dvo_detect`:

intel_dvo_detect
================

.. c:function:: enum drm_connector_status intel_dvo_detect(struct drm_connector *connector, bool force)

    :param struct drm_connector \*connector:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`intel_dvo_detect.description`:

Description
-----------

Unimplemented.

.. _`intel_dvo_get_current_mode`:

intel_dvo_get_current_mode
==========================

.. c:function:: struct drm_display_mode *intel_dvo_get_current_mode(struct drm_connector *connector)

    :param struct drm_connector \*connector:
        *undescribed*

.. _`intel_dvo_get_current_mode.description`:

Description
-----------

Other chips with DVO LVDS will need to extend this to deal with the LVDS
chip being on DVOB/C and having multiple pipes.

.. This file was automatic generated / don't edit.

