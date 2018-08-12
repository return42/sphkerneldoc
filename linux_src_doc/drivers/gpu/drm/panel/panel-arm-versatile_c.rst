.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/panel/panel-arm-versatile.c

.. _`versatile_panel_type`:

struct versatile_panel_type
===========================

.. c:type:: struct versatile_panel_type

    lookup struct for the supported panels

.. _`versatile_panel_type.definition`:

Definition
----------

.. code-block:: c

    struct versatile_panel_type {
        const char *name;
        u32 magic;
        struct drm_display_mode mode;
        u32 bus_flags;
        u32 width_mm;
        u32 height_mm;
        bool ib2;
    }

.. _`versatile_panel_type.members`:

Members
-------

name
    the name of this panel

magic
    the magic value from the detection register

mode
    the DRM display mode for this panel

bus_flags
    the DRM bus flags for this panel e.g. inverted clock

width_mm
    the panel width in mm

height_mm
    the panel height in mm

ib2
    the panel may be connected on an IB2 daughterboard

.. _`versatile_panel`:

struct versatile_panel
======================

.. c:type:: struct versatile_panel

    state container for the Versatile panels

.. _`versatile_panel.definition`:

Definition
----------

.. code-block:: c

    struct versatile_panel {
        struct device *dev;
        struct drm_panel panel;
        const struct versatile_panel_type *panel_type;
        struct regmap *map;
        struct regmap *ib2_map;
    }

.. _`versatile_panel.members`:

Members
-------

dev
    the container device

panel
    the DRM panel instance for this device

panel_type
    the Versatile panel type as detected

map
    map to the parent syscon where the main register reside

ib2_map
    map to the IB2 syscon, if applicable

.. This file was automatic generated / don't edit.

