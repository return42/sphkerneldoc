.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_lvds.c

.. _`intel_lvds_destroy`:

intel_lvds_destroy
==================

.. c:function:: void intel_lvds_destroy(struct drm_connector *connector)

    unregister and free LVDS structures

    :param connector:
        connector to free
    :type connector: struct drm_connector \*

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

    :param dev_priv:
        i915 device
    :type dev_priv: struct drm_i915_private \*

.. _`intel_lvds_init.description`:

Description
-----------

Create the connector, register the LVDS DDC bus, and try to figure out what
modes we can display on the LVDS panel (if present).

.. This file was automatic generated / don't edit.

