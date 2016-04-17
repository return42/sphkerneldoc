.. -*- coding: utf-8; mode: rst -*-

==========
drm_rect.h
==========


.. _`rect-utils`:

rect utils
==========

Utility functions to help manage rectangular areas for
clipping, scaling, etc. calculations.



.. _`drm_rect`:

struct drm_rect
===============

.. c:type:: drm_rect

    two dimensional rectangle


.. _`drm_rect.definition`:

Definition
----------

.. code-block:: c

  struct drm_rect {
    int x1;
    int y1;
    int x2;
    int y2;
  };


.. _`drm_rect.members`:

Members
-------

:``x1``:
    horizontal starting coordinate (inclusive)

:``y1``:
    vertical starting coordinate (inclusive)

:``x2``:
    horizontal ending coordinate (exclusive)

:``y2``:
    vertical ending coordinate (exclusive)




.. _`drm_rect_adjust_size`:

drm_rect_adjust_size
====================

.. c:function:: void drm_rect_adjust_size (struct drm_rect *r, int dw, int dh)

    adjust the size of the rectangle

    :param struct drm_rect \*r:
        rectangle to be adjusted

    :param int dw:
        horizontal adjustment

    :param int dh:
        vertical adjustment



.. _`drm_rect_adjust_size.description`:

Description
-----------

Change the size of rectangle ``r`` by ``dw`` in the horizontal direction,
and by ``dh`` in the vertical direction, while keeping the center
of ``r`` stationary.

Positive ``dw`` and ``dh`` increase the size, negative values decrease it.



.. _`drm_rect_translate`:

drm_rect_translate
==================

.. c:function:: void drm_rect_translate (struct drm_rect *r, int dx, int dy)

    translate the rectangle

    :param struct drm_rect \*r:
        rectangle to be tranlated

    :param int dx:
        horizontal translation

    :param int dy:
        vertical translation



.. _`drm_rect_translate.description`:

Description
-----------

Move rectangle ``r`` by ``dx`` in the horizontal direction,
and by ``dy`` in the vertical direction.



.. _`drm_rect_downscale`:

drm_rect_downscale
==================

.. c:function:: void drm_rect_downscale (struct drm_rect *r, int horz, int vert)

    downscale a rectangle

    :param struct drm_rect \*r:
        rectangle to be downscaled

    :param int horz:
        horizontal downscale factor

    :param int vert:
        vertical downscale factor



.. _`drm_rect_downscale.description`:

Description
-----------

Divide the coordinates of rectangle ``r`` by ``horz`` and ``vert``\ .



.. _`drm_rect_width`:

drm_rect_width
==============

.. c:function:: int drm_rect_width (const struct drm_rect *r)

    determine the rectangle width

    :param const struct drm_rect \*r:
        rectangle whose width is returned



.. _`drm_rect_width.returns`:

RETURNS
-------

The width of the rectangle.



.. _`drm_rect_height`:

drm_rect_height
===============

.. c:function:: int drm_rect_height (const struct drm_rect *r)

    determine the rectangle height

    :param const struct drm_rect \*r:
        rectangle whose height is returned



.. _`drm_rect_height.returns`:

RETURNS
-------

The height of the rectangle.



.. _`drm_rect_visible`:

drm_rect_visible
================

.. c:function:: bool drm_rect_visible (const struct drm_rect *r)

    determine if the the rectangle is visible

    :param const struct drm_rect \*r:
        rectangle whose visibility is returned



.. _`drm_rect_visible.returns`:

RETURNS
-------

``true`` if the rectangle is visible, ``false`` otherwise.



.. _`drm_rect_equals`:

drm_rect_equals
===============

.. c:function:: bool drm_rect_equals (const struct drm_rect *r1, const struct drm_rect *r2)

    determine if two rectangles are equal

    :param const struct drm_rect \*r1:
        first rectangle

    :param const struct drm_rect \*r2:
        second rectangle



.. _`drm_rect_equals.returns`:

RETURNS
-------

``true`` if the rectangles are equal, ``false`` otherwise.

