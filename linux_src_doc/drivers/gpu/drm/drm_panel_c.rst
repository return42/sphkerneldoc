.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_panel.c

.. _`drm_panel_init`:

drm_panel_init
==============

.. c:function:: void drm_panel_init(struct drm_panel *panel)

    initialize a panel

    :param struct drm_panel \*panel:
        DRM panel

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

    :param struct drm_panel \*panel:
        panel to add

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

    :param struct drm_panel \*panel:
        DRM panel

.. _`drm_panel_remove.description`:

Description
-----------

Removes a panel from the global registry.

.. _`drm_panel_attach`:

drm_panel_attach
================

.. c:function:: int drm_panel_attach(struct drm_panel *panel, struct drm_connector *connector)

    attach a panel to a connector

    :param struct drm_panel \*panel:
        DRM panel

    :param struct drm_connector \*connector:
        DRM connector

.. _`drm_panel_attach.description`:

Description
-----------

After obtaining a pointer to a DRM panel a display driver calls this
function to attach a panel to a connector.

An error is returned if the panel is already attached to another connector.

.. _`drm_panel_attach.return`:

Return
------

0 on success or a negative error code on failure.

.. _`drm_panel_detach`:

drm_panel_detach
================

.. c:function:: int drm_panel_detach(struct drm_panel *panel)

    detach a panel from a connector

    :param struct drm_panel \*panel:
        DRM panel

.. _`drm_panel_detach.description`:

Description
-----------

Detaches a panel from the connector it is attached to. If a panel is not
attached to any connector this is effectively a no-op.

.. _`drm_panel_detach.return`:

Return
------

0 on success or a negative error code on failure.

.. _`of_drm_find_panel`:

of_drm_find_panel
=================

.. c:function:: struct drm_panel *of_drm_find_panel(struct device_node *np)

    look up a panel using a device tree node

    :param struct device_node \*np:
        device tree node of the panel

.. _`of_drm_find_panel.description`:

Description
-----------

Searches the set of registered panels for one that matches the given device
tree node. If a matching panel is found, return a pointer to it.

.. _`of_drm_find_panel.return`:

Return
------

A pointer to the panel registered for the specified device tree
node or NULL if no panel matching the device tree node can be found.

.. This file was automatic generated / don't edit.
