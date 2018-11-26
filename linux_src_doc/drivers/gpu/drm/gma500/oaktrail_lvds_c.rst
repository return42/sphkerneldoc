.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/oaktrail_lvds.c

.. _`oaktrail_lvds_set_power`:

oaktrail_lvds_set_power
=======================

.. c:function:: void oaktrail_lvds_set_power(struct drm_device *dev, struct gma_encoder *gma_encoder, bool on)

    :param dev:
        *undescribed*
    :type dev: struct drm_device \*

    :param gma_encoder:
        *undescribed*
    :type gma_encoder: struct gma_encoder \*

    :param on:
        *undescribed*
    :type on: bool

.. _`oaktrail_lvds_init`:

oaktrail_lvds_init
==================

.. c:function:: void oaktrail_lvds_init(struct drm_device *dev, struct psb_intel_mode_device *mode_dev)

    setup LVDS connectors on this device

    :param dev:
        drm device
    :type dev: struct drm_device \*

    :param mode_dev:
        *undescribed*
    :type mode_dev: struct psb_intel_mode_device \*

.. _`oaktrail_lvds_init.description`:

Description
-----------

Create the connector, register the LVDS DDC bus, and try to figure out what
modes we can display on the LVDS panel (if present).

.. This file was automatic generated / don't edit.

