.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_rect.c

.. _`drm_rect_intersect`:

drm_rect_intersect
==================

.. c:function:: bool drm_rect_intersect(struct drm_rect *r1, const struct drm_rect *r2)

    intersect two rectangles

    :param r1:
        first rectangle
    :type r1: struct drm_rect \*

    :param r2:
        second rectangle
    :type r2: const struct drm_rect \*

.. _`drm_rect_intersect.description`:

Description
-----------

Calculate the intersection of rectangles \ ``r1``\  and \ ``r2``\ .
\ ``r1``\  will be overwritten with the intersection.

.. _`drm_rect_intersect.return`:

Return
------

\ ``true``\  if rectangle \ ``r1``\  is still visible after the operation,
\ ``false``\  otherwise.

.. _`drm_rect_clip_scaled`:

drm_rect_clip_scaled
====================

.. c:function:: bool drm_rect_clip_scaled(struct drm_rect *src, struct drm_rect *dst, const struct drm_rect *clip)

    perform a scaled clip operation

    :param src:
        source window rectangle
    :type src: struct drm_rect \*

    :param dst:
        destination window rectangle
    :type dst: struct drm_rect \*

    :param clip:
        clip rectangle
    :type clip: const struct drm_rect \*

.. _`drm_rect_clip_scaled.description`:

Description
-----------

Clip rectangle \ ``dst``\  by rectangle \ ``clip``\ . Clip rectangle \ ``src``\  by the
same amounts multiplied by \ ``hscale``\  and \ ``vscale``\ .

.. _`drm_rect_clip_scaled.return`:

Return
------

\ ``true``\  if rectangle \ ``dst``\  is still visible after being clipped,
\ ``false``\  otherwise

.. _`drm_rect_calc_hscale`:

drm_rect_calc_hscale
====================

.. c:function:: int drm_rect_calc_hscale(const struct drm_rect *src, const struct drm_rect *dst, int min_hscale, int max_hscale)

    calculate the horizontal scaling factor

    :param src:
        source window rectangle
    :type src: const struct drm_rect \*

    :param dst:
        destination window rectangle
    :type dst: const struct drm_rect \*

    :param min_hscale:
        minimum allowed horizontal scaling factor
    :type min_hscale: int

    :param max_hscale:
        maximum allowed horizontal scaling factor
    :type max_hscale: int

.. _`drm_rect_calc_hscale.description`:

Description
-----------

Calculate the horizontal scaling factor as
(@src width) / (@dst width).

If the scale is below 1 << 16, round down. If the scale is above
1 << 16, round up. This will calculate the scale with the most
pessimistic limit calculation.

.. _`drm_rect_calc_hscale.return`:

Return
------

The horizontal scaling factor, or errno of out of limits.

.. _`drm_rect_calc_vscale`:

drm_rect_calc_vscale
====================

.. c:function:: int drm_rect_calc_vscale(const struct drm_rect *src, const struct drm_rect *dst, int min_vscale, int max_vscale)

    calculate the vertical scaling factor

    :param src:
        source window rectangle
    :type src: const struct drm_rect \*

    :param dst:
        destination window rectangle
    :type dst: const struct drm_rect \*

    :param min_vscale:
        minimum allowed vertical scaling factor
    :type min_vscale: int

    :param max_vscale:
        maximum allowed vertical scaling factor
    :type max_vscale: int

.. _`drm_rect_calc_vscale.description`:

Description
-----------

Calculate the vertical scaling factor as
(@src height) / (@dst height).

If the scale is below 1 << 16, round down. If the scale is above
1 << 16, round up. This will calculate the scale with the most
pessimistic limit calculation.

.. _`drm_rect_calc_vscale.return`:

Return
------

The vertical scaling factor, or errno of out of limits.

.. _`drm_rect_calc_hscale_relaxed`:

drm_rect_calc_hscale_relaxed
============================

.. c:function:: int drm_rect_calc_hscale_relaxed(struct drm_rect *src, struct drm_rect *dst, int min_hscale, int max_hscale)

    calculate the horizontal scaling factor

    :param src:
        source window rectangle
    :type src: struct drm_rect \*

    :param dst:
        destination window rectangle
    :type dst: struct drm_rect \*

    :param min_hscale:
        minimum allowed horizontal scaling factor
    :type min_hscale: int

    :param max_hscale:
        maximum allowed horizontal scaling factor
    :type max_hscale: int

.. _`drm_rect_calc_hscale_relaxed.description`:

Description
-----------

Calculate the horizontal scaling factor as
(@src width) / (@dst width).

If the calculated scaling factor is below \ ``min_vscale``\ ,
decrease the height of rectangle \ ``dst``\  to compensate.

If the calculated scaling factor is above \ ``max_vscale``\ ,
decrease the height of rectangle \ ``src``\  to compensate.

If the scale is below 1 << 16, round down. If the scale is above
1 << 16, round up. This will calculate the scale with the most
pessimistic limit calculation.

.. _`drm_rect_calc_hscale_relaxed.return`:

Return
------

The horizontal scaling factor.

.. _`drm_rect_calc_vscale_relaxed`:

drm_rect_calc_vscale_relaxed
============================

.. c:function:: int drm_rect_calc_vscale_relaxed(struct drm_rect *src, struct drm_rect *dst, int min_vscale, int max_vscale)

    calculate the vertical scaling factor

    :param src:
        source window rectangle
    :type src: struct drm_rect \*

    :param dst:
        destination window rectangle
    :type dst: struct drm_rect \*

    :param min_vscale:
        minimum allowed vertical scaling factor
    :type min_vscale: int

    :param max_vscale:
        maximum allowed vertical scaling factor
    :type max_vscale: int

.. _`drm_rect_calc_vscale_relaxed.description`:

Description
-----------

Calculate the vertical scaling factor as
(@src height) / (@dst height).

If the calculated scaling factor is below \ ``min_vscale``\ ,
decrease the height of rectangle \ ``dst``\  to compensate.

If the calculated scaling factor is above \ ``max_vscale``\ ,
decrease the height of rectangle \ ``src``\  to compensate.

If the scale is below 1 << 16, round down. If the scale is above
1 << 16, round up. This will calculate the scale with the most
pessimistic limit calculation.

.. _`drm_rect_calc_vscale_relaxed.return`:

Return
------

The vertical scaling factor.

.. _`drm_rect_debug_print`:

drm_rect_debug_print
====================

.. c:function:: void drm_rect_debug_print(const char *prefix, const struct drm_rect *r, bool fixed_point)

    print the rectangle information

    :param prefix:
        prefix string
    :type prefix: const char \*

    :param r:
        rectangle to print
    :type r: const struct drm_rect \*

    :param fixed_point:
        rectangle is in 16.16 fixed point format
    :type fixed_point: bool

.. _`drm_rect_rotate`:

drm_rect_rotate
===============

.. c:function:: void drm_rect_rotate(struct drm_rect *r, int width, int height, unsigned int rotation)

    Rotate the rectangle

    :param r:
        rectangle to be rotated
    :type r: struct drm_rect \*

    :param width:
        Width of the coordinate space
    :type width: int

    :param height:
        Height of the coordinate space
    :type height: int

    :param rotation:
        Transformation to be applied
    :type rotation: unsigned int

.. _`drm_rect_rotate.description`:

Description
-----------

Apply \ ``rotation``\  to the coordinates of rectangle \ ``r``\ .

\ ``width``\  and \ ``height``\  combined with \ ``rotation``\  define
the location of the new origin.

\ ``width``\  correcsponds to the horizontal and \ ``height``\ 
to the vertical axis of the untransformed coordinate
space.

.. _`drm_rect_rotate_inv`:

drm_rect_rotate_inv
===================

.. c:function:: void drm_rect_rotate_inv(struct drm_rect *r, int width, int height, unsigned int rotation)

    Inverse rotate the rectangle

    :param r:
        rectangle to be rotated
    :type r: struct drm_rect \*

    :param width:
        Width of the coordinate space
    :type width: int

    :param height:
        Height of the coordinate space
    :type height: int

    :param rotation:
        Transformation whose inverse is to be applied
    :type rotation: unsigned int

.. _`drm_rect_rotate_inv.description`:

Description
-----------

Apply the inverse of \ ``rotation``\  to the coordinates
of rectangle \ ``r``\ .

\ ``width``\  and \ ``height``\  combined with \ ``rotation``\  define
the location of the new origin.

\ ``width``\  correcsponds to the horizontal and \ ``height``\ 
to the vertical axis of the original untransformed
coordinate space, so that you never have to flip
them when doing a rotatation and its inverse.
That is, if you do ::

    drm_rect_rotate(&r, width, height, rotation);
    drm_rect_rotate_inv(&r, width, height, rotation);

you will always get back the original rectangle.

.. This file was automatic generated / don't edit.

