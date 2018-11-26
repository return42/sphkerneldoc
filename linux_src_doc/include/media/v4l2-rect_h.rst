.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-rect.h

.. _`v4l2_rect_set_size_to`:

v4l2_rect_set_size_to
=====================

.. c:function:: void v4l2_rect_set_size_to(struct v4l2_rect *r, const struct v4l2_rect *size)

    copy the width/height values.

    :param r:
        rect whose width and height fields will be set
    :type r: struct v4l2_rect \*

    :param size:
        rect containing the width and height fields you need.
    :type size: const struct v4l2_rect \*

.. _`v4l2_rect_set_min_size`:

v4l2_rect_set_min_size
======================

.. c:function:: void v4l2_rect_set_min_size(struct v4l2_rect *r, const struct v4l2_rect *min_size)

    width and height of r should be >= min_size.

    :param r:
        rect whose width and height will be modified
    :type r: struct v4l2_rect \*

    :param min_size:
        rect containing the minimal width and height
    :type min_size: const struct v4l2_rect \*

.. _`v4l2_rect_set_max_size`:

v4l2_rect_set_max_size
======================

.. c:function:: void v4l2_rect_set_max_size(struct v4l2_rect *r, const struct v4l2_rect *max_size)

    width and height of r should be <= max_size

    :param r:
        rect whose width and height will be modified
    :type r: struct v4l2_rect \*

    :param max_size:
        rect containing the maximum width and height
    :type max_size: const struct v4l2_rect \*

.. _`v4l2_rect_map_inside`:

v4l2_rect_map_inside
====================

.. c:function:: void v4l2_rect_map_inside(struct v4l2_rect *r, const struct v4l2_rect *boundary)

    r should be inside boundary.

    :param r:
        rect that will be modified
    :type r: struct v4l2_rect \*

    :param boundary:
        rect containing the boundary for \ ``r``\ 
    :type boundary: const struct v4l2_rect \*

.. _`v4l2_rect_same_size`:

v4l2_rect_same_size
===================

.. c:function:: bool v4l2_rect_same_size(const struct v4l2_rect *r1, const struct v4l2_rect *r2)

    return true if r1 has the same size as r2

    :param r1:
        rectangle.
    :type r1: const struct v4l2_rect \*

    :param r2:
        rectangle.
    :type r2: const struct v4l2_rect \*

.. _`v4l2_rect_same_size.description`:

Description
-----------

Return true if both rectangles have the same size.

.. _`v4l2_rect_same_position`:

v4l2_rect_same_position
=======================

.. c:function:: bool v4l2_rect_same_position(const struct v4l2_rect *r1, const struct v4l2_rect *r2)

    return true if r1 has the same position as r2

    :param r1:
        rectangle.
    :type r1: const struct v4l2_rect \*

    :param r2:
        rectangle.
    :type r2: const struct v4l2_rect \*

.. _`v4l2_rect_same_position.description`:

Description
-----------

Return true if both rectangles have the same position

.. _`v4l2_rect_equal`:

v4l2_rect_equal
===============

.. c:function:: bool v4l2_rect_equal(const struct v4l2_rect *r1, const struct v4l2_rect *r2)

    return true if r1 equals r2

    :param r1:
        rectangle.
    :type r1: const struct v4l2_rect \*

    :param r2:
        rectangle.
    :type r2: const struct v4l2_rect \*

.. _`v4l2_rect_equal.description`:

Description
-----------

Return true if both rectangles have the same size and position.

.. _`v4l2_rect_intersect`:

v4l2_rect_intersect
===================

.. c:function:: void v4l2_rect_intersect(struct v4l2_rect *r, const struct v4l2_rect *r1, const struct v4l2_rect *r2)

    calculate the intersection of two rects.

    :param r:
        intersection of \ ``r1``\  and \ ``r2``\ .
    :type r: struct v4l2_rect \*

    :param r1:
        rectangle.
    :type r1: const struct v4l2_rect \*

    :param r2:
        rectangle.
    :type r2: const struct v4l2_rect \*

.. _`v4l2_rect_scale`:

v4l2_rect_scale
===============

.. c:function:: void v4l2_rect_scale(struct v4l2_rect *r, const struct v4l2_rect *from, const struct v4l2_rect *to)

    scale rect r by to/from

    :param r:
        rect to be scaled.
    :type r: struct v4l2_rect \*

    :param from:
        from rectangle.
    :type from: const struct v4l2_rect \*

    :param to:
        to rectangle.
    :type to: const struct v4l2_rect \*

.. _`v4l2_rect_scale.description`:

Description
-----------

This scales rectangle \ ``r``\  horizontally by \ ``to->width``\  / \ ``from->width``\  and
vertically by \ ``to->height``\  / \ ``from->height``\ .

Typically \ ``r``\  is a rectangle inside \ ``from``\  and you want the rectangle as
it would appear after scaling \ ``from``\  to \ ``to``\ . So the resulting \ ``r``\  will
be the scaled rectangle inside \ ``to``\ .

.. _`v4l2_rect_overlap`:

v4l2_rect_overlap
=================

.. c:function:: bool v4l2_rect_overlap(const struct v4l2_rect *r1, const struct v4l2_rect *r2)

    do r1 and r2 overlap?

    :param r1:
        rectangle.
    :type r1: const struct v4l2_rect \*

    :param r2:
        rectangle.
    :type r2: const struct v4l2_rect \*

.. _`v4l2_rect_overlap.description`:

Description
-----------

Returns true if \ ``r1``\  and \ ``r2``\  overlap.

.. This file was automatic generated / don't edit.

