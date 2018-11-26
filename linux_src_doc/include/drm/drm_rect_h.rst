.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/drm/drm_rect.h

.. _`rect-utils`:

rect utils
==========

Utility functions to help manage rectangular areas for
clipping, scaling, etc. calculations.

.. _`drm_rect`:

struct drm_rect
===============

.. c:type:: struct drm_rect

    two dimensional rectangle

.. _`drm_rect.definition`:

Definition
----------

.. code-block:: c

    struct drm_rect {
        int x1, y1, x2, y2;
    }

.. _`drm_rect.members`:

Members
-------

x1
    horizontal starting coordinate (inclusive)

y1
    vertical starting coordinate (inclusive)

x2
    horizontal ending coordinate (exclusive)

y2
    vertical ending coordinate (exclusive)

.. _`drm_rect_fmt`:

DRM_RECT_FMT
============

.. c:function::  DRM_RECT_FMT()

    printf string for \ :c:type:`struct drm_rect <drm_rect>`\ 

.. _`drm_rect_arg`:

DRM_RECT_ARG
============

.. c:function::  DRM_RECT_ARG( r)

    printf arguments for \ :c:type:`struct drm_rect <drm_rect>`\ 

    :param r:
        rectangle struct
    :type r: 

.. _`drm_rect_fp_fmt`:

DRM_RECT_FP_FMT
===============

.. c:function::  DRM_RECT_FP_FMT()

    printf string for \ :c:type:`struct drm_rect <drm_rect>`\  in 16.16 fixed point

.. _`drm_rect_fp_arg`:

DRM_RECT_FP_ARG
===============

.. c:function::  DRM_RECT_FP_ARG( r)

    printf arguments for \ :c:type:`struct drm_rect <drm_rect>`\  in 16.16 fixed point

    :param r:
        rectangle struct
    :type r: 

.. _`drm_rect_fp_arg.description`:

Description
-----------

This is useful for e.g. printing plane source rectangles, which are in 16.16
fixed point.

.. _`drm_rect_adjust_size`:

drm_rect_adjust_size
====================

.. c:function:: void drm_rect_adjust_size(struct drm_rect *r, int dw, int dh)

    adjust the size of the rectangle

    :param r:
        rectangle to be adjusted
    :type r: struct drm_rect \*

    :param dw:
        horizontal adjustment
    :type dw: int

    :param dh:
        vertical adjustment
    :type dh: int

.. _`drm_rect_adjust_size.description`:

Description
-----------

Change the size of rectangle \ ``r``\  by \ ``dw``\  in the horizontal direction,
and by \ ``dh``\  in the vertical direction, while keeping the center
of \ ``r``\  stationary.

Positive \ ``dw``\  and \ ``dh``\  increase the size, negative values decrease it.

.. _`drm_rect_translate`:

drm_rect_translate
==================

.. c:function:: void drm_rect_translate(struct drm_rect *r, int dx, int dy)

    translate the rectangle

    :param r:
        rectangle to be tranlated
    :type r: struct drm_rect \*

    :param dx:
        horizontal translation
    :type dx: int

    :param dy:
        vertical translation
    :type dy: int

.. _`drm_rect_translate.description`:

Description
-----------

Move rectangle \ ``r``\  by \ ``dx``\  in the horizontal direction,
and by \ ``dy``\  in the vertical direction.

.. _`drm_rect_downscale`:

drm_rect_downscale
==================

.. c:function:: void drm_rect_downscale(struct drm_rect *r, int horz, int vert)

    downscale a rectangle

    :param r:
        rectangle to be downscaled
    :type r: struct drm_rect \*

    :param horz:
        horizontal downscale factor
    :type horz: int

    :param vert:
        vertical downscale factor
    :type vert: int

.. _`drm_rect_downscale.description`:

Description
-----------

Divide the coordinates of rectangle \ ``r``\  by \ ``horz``\  and \ ``vert``\ .

.. _`drm_rect_width`:

drm_rect_width
==============

.. c:function:: int drm_rect_width(const struct drm_rect *r)

    determine the rectangle width

    :param r:
        rectangle whose width is returned
    :type r: const struct drm_rect \*

.. _`drm_rect_width.return`:

Return
------

The width of the rectangle.

.. _`drm_rect_height`:

drm_rect_height
===============

.. c:function:: int drm_rect_height(const struct drm_rect *r)

    determine the rectangle height

    :param r:
        rectangle whose height is returned
    :type r: const struct drm_rect \*

.. _`drm_rect_height.return`:

Return
------

The height of the rectangle.

.. _`drm_rect_visible`:

drm_rect_visible
================

.. c:function:: bool drm_rect_visible(const struct drm_rect *r)

    determine if the the rectangle is visible

    :param r:
        rectangle whose visibility is returned
    :type r: const struct drm_rect \*

.. _`drm_rect_visible.return`:

Return
------

\ ``true``\  if the rectangle is visible, \ ``false``\  otherwise.

.. _`drm_rect_equals`:

drm_rect_equals
===============

.. c:function:: bool drm_rect_equals(const struct drm_rect *r1, const struct drm_rect *r2)

    determine if two rectangles are equal

    :param r1:
        first rectangle
    :type r1: const struct drm_rect \*

    :param r2:
        second rectangle
    :type r2: const struct drm_rect \*

.. _`drm_rect_equals.return`:

Return
------

\ ``true``\  if the rectangles are equal, \ ``false``\  otherwise.

.. This file was automatic generated / don't edit.

