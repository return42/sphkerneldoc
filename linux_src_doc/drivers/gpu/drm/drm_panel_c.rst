.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_panel.c

.. _`drm-panel`:

drm panel
=========

The DRM panel helpers allow drivers to register panel objects with a
central registry and provide functions to retrieve those panels in display
drivers.

.. _`drm_panel_init`:

drm_panel_init
==============

.. c:function:: void drm_panel_init(struct drm_panel *panel)

    initialize a panel

    :param panel:
        DRM panel
    :type panel: struct drm_panel \*

.. _`drm_panel_init.description`:

Description
-----------

Sets up internal fields of the panel so that it can subsequently be added
to the registry.

.. _`drm_panel_add`:

drm_panel_add
=============

.. c:function:: int drm_panel_add(struct drm_panel *panel)

    add a panel to the global registry

    :param panel:
        panel to add
    :type panel: struct drm_panel \*

.. _`drm_panel_add.description`:

Description
-----------

Add a panel to the global registry so that it can be looked up by display
drivers.

.. _`drm_panel_add.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_panel_remove`:

drm_panel_remove
================

.. c:function:: void drm_panel_remove(struct drm_panel *panel)

    remove a panel from the global registry

    :param panel:
        DRM panel
    :type panel: struct drm_panel \*

.. _`drm_panel_remove.description`:

Description
-----------

Removes a panel from the global registry.

.. _`drm_panel_attach`:

drm_panel_attach
================

.. c:function:: int drm_panel_attach(struct drm_panel *panel, struct drm_connector *connector)

    attach a panel to a connector

    :param panel:
        DRM panel
    :type panel: struct drm_panel \*

    :param connector:
        DRM connector
    :type connector: struct drm_connector \*

.. _`drm_panel_attach.description`:

Description
-----------

After obtaining a pointer to a DRM panel a display driver calls this
function to attach a panel to a connector.

An error is returned if the panel is already attached to another connector.

When unloading, the driver should detach from the panel by calling
\ :c:func:`drm_panel_detach`\ .

.. _`drm_panel_attach.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_panel_detach`:

drm_panel_detach
================

.. c:function:: int drm_panel_detach(struct drm_panel *panel)

    detach a panel from a connector

    :param panel:
        DRM panel
    :type panel: struct drm_panel \*

.. _`drm_panel_detach.description`:

Description
-----------

Detaches a panel from the connector it is attached to. If a panel is not
attached to any connector this is effectively a no-op.

This function should not be called by the panel device itself. It
is only for the drm device that called \ :c:func:`drm_panel_attach`\ .

.. _`drm_panel_detach.return`:

Return
------

0 on success or a negative error code on failure.

.. _`of_drm_find_panel`:

of_drm_find_panel
=================

.. c:function:: struct drm_panel *of_drm_find_panel(const struct device_node *np)

    look up a panel using a device tree node

    :param np:
        device tree node of the panel
    :type np: const struct device_node \*

.. _`of_drm_find_panel.description`:

Description
-----------

Searches the set of registered panels for one that matches the given device
tree node. If a matching panel is found, return a pointer to it.

.. _`of_drm_find_panel.return`:

Return
------

A pointer to the panel registered for the specified device tree
node or an \ :c:func:`ERR_PTR`\  if no panel matching the device tree node can be found.

.. _`of_drm_find_panel.possible-error-codes-returned-by-this-function`:

Possible error codes returned by this function
----------------------------------------------


- EPROBE_DEFER: the panel device has not been probed yet, and the caller
  should retry later
- ENODEV: the device is not available (status != "okay" or "ok")

.. This file was automatic generated / don't edit.

