.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/bridge/panel.c

.. _`drm_panel_bridge_add`:

drm_panel_bridge_add
====================

.. c:function:: struct drm_bridge *drm_panel_bridge_add(struct drm_panel *panel, u32 connector_type)

    Creates a drm_bridge and drm_connector that just calls the appropriate functions from drm_panel.

    :param panel:
        The drm_panel being wrapped.  Must be non-NULL.
    :type panel: struct drm_panel \*

    :param connector_type:
        The DRM_MODE_CONNECTOR_* for the connector to be
        created.
    :type connector_type: u32

.. _`drm_panel_bridge_add.description`:

Description
-----------

For drivers converting from directly using drm_panel: The expected
usage pattern is that during either encoder module probe or DSI
host attach, a drm_panel will be looked up through
\ :c:func:`drm_of_find_panel_or_bridge`\ .  \ :c:func:`drm_panel_bridge_add`\  is used to
wrap that panel in the new bridge, and the result can then be
passed to \ :c:func:`drm_bridge_attach`\ .  The \ :c:func:`drm_panel_prepare`\  and related
functions can be dropped from the encoder driver (they're now
called by the KMS helpers before calling into the encoder), along
with connector creation.  When done with the bridge,
\ :c:func:`drm_bridge_detach`\  should be called as normal, then
\ :c:func:`drm_panel_bridge_remove`\  to free it.

.. _`drm_panel_bridge_remove`:

drm_panel_bridge_remove
=======================

.. c:function:: void drm_panel_bridge_remove(struct drm_bridge *bridge)

    Unregisters and frees a drm_bridge created by \ :c:func:`drm_panel_bridge_add`\ .

    :param bridge:
        The drm_bridge being freed.
    :type bridge: struct drm_bridge \*

.. This file was automatic generated / don't edit.

