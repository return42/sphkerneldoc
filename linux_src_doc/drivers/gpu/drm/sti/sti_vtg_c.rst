.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/sti/sti_vtg.c

.. _`sti_vtg_get_line_number`:

sti_vtg_get_line_number
=======================

.. c:function:: u32 sti_vtg_get_line_number(struct drm_display_mode mode, int y)

    :param mode:
        display mode to be used
    :type mode: struct drm_display_mode

    :param y:
        line
    :type y: int

.. _`sti_vtg_get_line_number.description`:

Description
-----------

Return the line number according to the display mode taking
into account the Sync and Back Porch information.
Video frame line numbers start at 1, y starts at 0.
In interlaced modes the start line is the field line number of the odd
field, but y is still defined as a progressive frame.

.. _`sti_vtg_get_pixel_number`:

sti_vtg_get_pixel_number
========================

.. c:function:: u32 sti_vtg_get_pixel_number(struct drm_display_mode mode, int x)

    :param mode:
        display mode to be used
    :type mode: struct drm_display_mode

    :param x:
        row
    :type x: int

.. _`sti_vtg_get_pixel_number.description`:

Description
-----------

Return the pixel number according to the display mode taking
into account the Sync and Back Porch information.
Pixels are counted from 0.

.. This file was automatic generated / don't edit.

