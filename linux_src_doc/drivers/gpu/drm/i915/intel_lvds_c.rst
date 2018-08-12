.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_lvds.c

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

.. c:function:: void intel_lvds_init(struct drm_i915_private *dev_priv)

    setup LVDS connectors on this device

    :param struct drm_i915_private \*dev_priv:
        i915 device

.. _`intel_lvds_init.description`:

Description
-----------

Create the connector, register the LVDS DDC bus, and try to figure out what
modes we can display on the LVDS panel (if present).

.. This file was automatic generated / don't edit.

