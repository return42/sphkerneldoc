.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/gma500/cdv_intel_lvds.c

.. _`brightness_max_level`:

BRIGHTNESS_MAX_LEVEL
====================

.. c:function::  BRIGHTNESS_MAX_LEVEL()

.. _`cdv_intel_lvds_set_backlight`:

cdv_intel_lvds_set_backlight
============================

.. c:function:: void cdv_intel_lvds_set_backlight(struct drm_device *dev, int level)

    :param struct drm_device \*dev:
        *undescribed*

    :param int level:
        *undescribed*

.. _`cdv_intel_lvds_set_backlight.description`:

Description
-----------

level backlight level, from 0 to \ :c:func:`cdv_intel_lvds_get_max_backlight`\ .

.. _`cdv_intel_lvds_set_power`:

cdv_intel_lvds_set_power
========================

.. c:function:: void cdv_intel_lvds_set_power(struct drm_device *dev, struct drm_encoder *encoder, bool on)

    :param struct drm_device \*dev:
        *undescribed*

    :param struct drm_encoder \*encoder:
        *undescribed*

    :param bool on:
        *undescribed*

.. _`cdv_intel_lvds_detect`:

cdv_intel_lvds_detect
=====================

.. c:function:: enum drm_connector_status cdv_intel_lvds_detect(struct drm_connector *connector, bool force)

    :param struct drm_connector \*connector:
        *undescribed*

    :param bool force:
        *undescribed*

.. _`cdv_intel_lvds_detect.description`:

Description
-----------

This always returns CONNECTOR_STATUS_CONNECTED.
This connector should only have
been set up if the LVDS was actually connected anyway.

.. _`cdv_intel_lvds_get_modes`:

cdv_intel_lvds_get_modes
========================

.. c:function:: int cdv_intel_lvds_get_modes(struct drm_connector *connector)

    :param struct drm_connector \*connector:
        *undescribed*

.. _`cdv_intel_lvds_destroy`:

cdv_intel_lvds_destroy
======================

.. c:function:: void cdv_intel_lvds_destroy(struct drm_connector *connector)

    unregister and free LVDS structures

    :param struct drm_connector \*connector:
        connector to free

.. _`cdv_intel_lvds_destroy.description`:

Description
-----------

Unregister the DDC bus for this connector then free the driver private
structure.

.. _`cdv_intel_lvds_init`:

cdv_intel_lvds_init
===================

.. c:function:: void cdv_intel_lvds_init(struct drm_device *dev, struct psb_intel_mode_device *mode_dev)

    setup LVDS connectors on this device

    :param struct drm_device \*dev:
        drm device

    :param struct psb_intel_mode_device \*mode_dev:
        *undescribed*

.. _`cdv_intel_lvds_init.description`:

Description
-----------

Create the connector, register the LVDS DDC bus, and try to figure out what
modes we can display on the LVDS panel (if present).

.. This file was automatic generated / don't edit.

