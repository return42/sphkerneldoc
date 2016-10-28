.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_lvds.c

.. _`intel_enable_lvds`:

intel_enable_lvds
=================

.. c:function:: void intel_enable_lvds(struct intel_encoder *encoder)

    :param struct intel_encoder \*encoder:
        *undescribed*

.. _`intel_lvds_detect`:

intel_lvds_detect
=================

.. c:function:: enum drm_connector_status intel_lvds_detect(struct drm_connector *connector, bool force)

    :param struct drm_connector \*connector:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`intel_lvds_detect.description`:

Description
-----------

Since LVDS doesn't have hotlug, we use the lid as a proxy.  Open means
connected and closed means disconnected.  We also send hotplug events as
needed, using lid status notification from the input layer.

.. _`intel_lvds_get_modes`:

intel_lvds_get_modes
====================

.. c:function:: int intel_lvds_get_modes(struct drm_connector *connector)

    :param struct drm_connector \*connector:
        *undescribed*

.. _`intel_lvds_destroy`:

intel_lvds_destroy
==================

.. c:function:: void intel_lvds_destroy(struct drm_connector *connector)

    unregister and free LVDS structures

    :param struct drm_connector \*connector:
        connector to free

.. _`intel_lvds_destroy.description`:

Description
-----------

Unregister the DDC bus for this connector then free the driver private
structure.

.. _`intel_lvds_init`:

intel_lvds_init
===============

.. c:function:: void intel_lvds_init(struct drm_device *dev)

    setup LVDS connectors on this device

    :param struct drm_device \*dev:
        drm device

.. _`intel_lvds_init.description`:

Description
-----------

Create the connector, register the LVDS DDC bus, and try to figure out what
modes we can display on the LVDS panel (if present).

.. This file was automatic generated / don't edit.

