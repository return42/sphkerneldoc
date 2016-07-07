.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_rect.c

.. _`drm_rect_intersect`:

drm_rect_intersect
==================

.. c:function:: bool drm_rect_intersect(struct drm_rect *r1, const struct drm_rect *r2)

    intersect two rectangles

    :param struct drm_rect \*r1:
        first rectangle

    :param const struct drm_rect \*r2:
        second rectangle

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

.. c:function:: bool drm_rect_clip_scaled(struct drm_rect *src, struct drm_rect *dst, const struct drm_rect *clip, int hscale, int vscale)

    perform a scaled clip operation

    :param struct drm_rect \*src:
        source window rectangle

    :param struct drm_rect \*dst:
        destination window rectangle

    :param const struct drm_rect \*clip:
        clip rectangle

    :param int hscale:
        horizontal scaling factor

    :param int vscale:
        vertical scaling factor

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

    :param const struct drm_rect \*src:
        source window rectangle

    :param const struct drm_rect \*dst:
        destination window rectangle

    :param int min_hscale:
        minimum allowed horizontal scaling factor

    :param int max_hscale:
        maximum allowed horizontal scaling factor

.. _`drm_rect_calc_hscale.description`:

Description
-----------

Calculate the horizontal scaling factor as
(\ ``src``\  width) / (\ ``dst``\  width).

.. _`drm_rect_calc_hscale.return`:

Return
------

The horizontal scaling factor, or errno of out of limits.

.. _`drm_rect_calc_vscale`:

drm_rect_calc_vscale
====================

.. c:function:: int drm_rect_calc_vscale(const struct drm_rect *src, const struct drm_rect *dst, int min_vscale, int max_vscale)

    calculate the vertical scaling factor

    :param const struct drm_rect \*src:
        source window rectangle

    :param const struct drm_rect \*dst:
        destination window rectangle

    :param int min_vscale:
        minimum allowed vertical scaling factor

    :param int max_vscale:
        maximum allowed vertical scaling factor

.. _`drm_rect_calc_vscale.description`:

Description
-----------

Calculate the vertical scaling factor as
(\ ``src``\  height) / (\ ``dst``\  height).

.. _`drm_rect_calc_vscale.return`:

Return
------

The vertical scaling factor, or errno of out of limits.

.. _`drm_rect_calc_hscale_relaxed`:

drm_rect_calc_hscale_relaxed
============================

.. c:function:: int drm_rect_calc_hscale_relaxed(struct drm_rect *src, struct drm_rect *dst, int min_hscale, int max_hscale)

    calculate the horizontal scaling factor

    :param struct drm_rect \*src:
        source window rectangle

    :param struct drm_rect \*dst:
        destination window rectangle

    :param int min_hscale:
        minimum allowed horizontal scaling factor

    :param int max_hscale:
        maximum allowed horizontal scaling factor

.. _`drm_rect_calc_hscale_relaxed.description`:

Description
-----------

Calculate the horizontal scaling factor as
(\ ``src``\  width) / (\ ``dst``\  width).

If the calculated scaling factor is below \ ``min_vscale``\ ,
decrease the height of rectangle \ ``dst``\  to compensate.

If the calculated scaling factor is above \ ``max_vscale``\ ,
decrease the height of rectangle \ ``src``\  to compensate.

.. _`drm_rect_calc_hscale_relaxed.return`:

Return
------

The horizontal scaling factor.

.. _`drm_rect_calc_vscale_relaxed`:

drm_rect_calc_vscale_relaxed
============================

.. c:function:: int drm_rect_calc_vscale_relaxed(struct drm_rect *src, struct drm_rect *dst, int min_vscale, int max_vscale)

    calculate the vertical scaling factor

    :param struct drm_rect \*src:
        source window rectangle

    :param struct drm_rect \*dst:
        destination window rectangle

    :param int min_vscale:
        minimum allowed vertical scaling factor

    :param int max_vscale:
        maximum allowed vertical scaling factor

.. _`drm_rect_calc_vscale_relaxed.description`:

Description
-----------

Calculate the vertical scaling factor as
(\ ``src``\  height) / (\ ``dst``\  height).

If the calculated scaling factor is below \ ``min_vscale``\ ,
decrease the height of rectangle \ ``dst``\  to compensate.

If the calculated scaling factor is above \ ``max_vscale``\ ,
decrease the height of rectangle \ ``src``\  to compensate.

.. _`drm_rect_calc_vscale_relaxed.return`:

Return
------

The vertical scaling factor.

.. _`drm_rect_debug_print`:

drm_rect_debug_print
====================

.. c:function:: void drm_rect_debug_print(const char *prefix, const struct drm_rect *r, bool fixed_point)

    print the rectangle information

    :param const char \*prefix:
        prefix string

    :param const struct drm_rect \*r:
        rectangle to print

    :param bool fixed_point:
        rectangle is in 16.16 fixed point format

.. _`drm_rect_rotate`:

drm_rect_rotate
===============

.. c:function:: void drm_rect_rotate(struct drm_rect *r, int width, int height, unsigned int rotation)

    Rotate the rectangle

    :param struct drm_rect \*r:
        rectangle to be rotated

    :param int width:
        Width of the coordinate space

    :param int height:
        Height of the coordinate space

    :param unsigned int rotation:
        Transformation to be applied

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

    :param struct drm_rect \*r:
        rectangle to be rotated

    :param int width:
        Width of the coordinate space

    :param int height:
        Height of the coordinate space

    :param unsigned int rotation:
        Transformation whose inverse is to be applied

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
That is, if you do:

drm_rotate(\ :c:type:`struct r <r>`, width, height, rotation);
drm_rotate_inv(\ :c:type:`struct r <r>`, width, height, rotation);

you will always get back the original rectangle.

.. This file was automatic generated / don't edit.

