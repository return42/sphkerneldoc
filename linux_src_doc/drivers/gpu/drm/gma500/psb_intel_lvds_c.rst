.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/psb_intel_lvds.c

.. _`psb_intel_lvds_destroy`:

psb_intel_lvds_destroy
======================

.. c:function:: void psb_intel_lvds_destroy(struct drm_connector *connector)

    unregister and free LVDS structures

    :param connector:
        connector to free
    :type connector: struct drm_connector \*

.. _`psb_intel_lvds_destroy.description`:

Description
-----------

Unregister the DDC bus for this connector then free the driver private
structure.

.. _`psb_intel_lvds_init`:

psb_intel_lvds_init
===================

.. c:function:: void psb_intel_lvds_init(struct drm_device *dev, struct psb_intel_mode_device *mode_dev)

    setup LVDS connectors on this device

    :param dev:
        drm device
    :type dev: struct drm_device \*

    :param mode_dev:
        *undescribed*
    :type mode_dev: struct psb_intel_mode_device \*

.. _`psb_intel_lvds_init.description`:

Description
-----------

Create the connector, register the LVDS DDC bus, and try to figure out what
modes we can display on the LVDS panel (if present).

.. This file was automatic generated / don't edit.

