.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/oaktrail_lvds.c

.. _`oaktrail_lvds_set_power`:

oaktrail_lvds_set_power
=======================

.. c:function:: void oaktrail_lvds_set_power(struct drm_device *dev, struct gma_encoder *gma_encoder, bool on)

    :param struct drm_device \*dev:
        *undescribed*

    :param struct gma_encoder \*gma_encoder:
        *undescribed*

    :param bool on:
        *undescribed*

.. _`oaktrail_lvds_init`:

oaktrail_lvds_init
==================

.. c:function:: void oaktrail_lvds_init(struct drm_device *dev, struct psb_intel_mode_device *mode_dev)

    setup LVDS connectors on this device

    :param struct drm_device \*dev:
        drm device

    :param struct psb_intel_mode_device \*mode_dev:
        *undescribed*

.. _`oaktrail_lvds_init.description`:

Description
-----------

Create the connector, register the LVDS DDC bus, and try to figure out what
modes we can display on the LVDS panel (if present).

.. This file was automatic generated / don't edit.

