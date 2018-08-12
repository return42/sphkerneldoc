.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/rcar-du/rcar_du_vsp.h

.. _`rcar_du_vsp_plane_state`:

struct rcar_du_vsp_plane_state
==============================

.. c:type:: struct rcar_du_vsp_plane_state

    Driver-specific plane state

.. _`rcar_du_vsp_plane_state.definition`:

Definition
----------

.. code-block:: c

    struct rcar_du_vsp_plane_state {
        struct drm_plane_state state;
        const struct rcar_du_format_info *format;
        struct sg_table sg_tables[3];
    }

.. _`rcar_du_vsp_plane_state.members`:

Members
-------

state
    base DRM plane state

format
    information about the pixel format used by the plane

sg_tables
    scatter-gather tables for the frame buffer memory

.. This file was automatic generated / don't edit.

