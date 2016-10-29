.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/rcar-du/rcar_du_plane.h

.. _`rcar_du_plane_state`:

struct rcar_du_plane_state
==========================

.. c:type:: struct rcar_du_plane_state

    Driver-specific plane state

.. _`rcar_du_plane_state.definition`:

Definition
----------

.. code-block:: c

    struct rcar_du_plane_state {
        struct drm_plane_state state;
        const struct rcar_du_format_info *format;
        int hwindex;
        enum rcar_du_plane_source source;
        unsigned int alpha;
        unsigned int colorkey;
        unsigned int zpos;
    }

.. _`rcar_du_plane_state.members`:

Members
-------

state
    base DRM plane state

format
    information about the pixel format used by the plane

hwindex
    0-based hardware plane index, -1 means unused

source
    *undescribed*

alpha
    value of the plane alpha property

colorkey
    value of the plane colorkey property

zpos
    value of the plane zpos property

.. This file was automatic generated / don't edit.
