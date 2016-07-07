.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_tv.c

.. _`intel_tv_detect_type`:

intel_tv_detect_type
====================

.. c:function:: int intel_tv_detect_type(struct intel_tv *intel_tv, struct drm_connector *connector)

    :param struct intel_tv \*intel_tv:
        *undescribed*

    :param struct drm_connector \*connector:
        *undescribed*

.. _`intel_tv_detect_type.description`:

Description
-----------

Requires that the current pipe's DPLL is active.
\return true if TV is connected.
\return false if TV is disconnected.

.. _`intel_tv_detect`:

intel_tv_detect
===============

.. c:function:: enum drm_connector_status intel_tv_detect(struct drm_connector *connector, bool force)

    :param struct drm_connector \*connector:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`intel_tv_detect.description`:

Description
-----------

Currently this always returns CONNECTOR_STATUS_UNKNOWN, as we need to be sure
we have a pipe programmed in order to probe the TV.

.. _`intel_tv_get_modes`:

intel_tv_get_modes
==================

.. c:function:: int intel_tv_get_modes(struct drm_connector *connector)

    :param struct drm_connector \*connector:
        *undescribed*

.. _`intel_tv_get_modes.description`:

Description
-----------

This should probably return a set of fixed modes, unless we can figure out
how to probe modes off of TV connections.

.. This file was automatic generated / don't edit.

