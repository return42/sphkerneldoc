.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-rect.h

.. _`v4l2_rect_set_size_to`:

v4l2_rect_set_size_to
=====================

.. c:function:: void v4l2_rect_set_size_to(struct v4l2_rect *r, const struct v4l2_rect *size)

    copy the width/height values.

    :param struct v4l2_rect \*r:
        rect whose width and height fields will be set

    :param const struct v4l2_rect \*size:
        rect containing the width and height fields you need.

.. _`v4l2_rect_set_min_size`:

v4l2_rect_set_min_size
======================

.. c:function:: void v4l2_rect_set_min_size(struct v4l2_rect *r, const struct v4l2_rect *min_size)

    width and height of r should be >= min_size.

    :param struct v4l2_rect \*r:
        rect whose width and height will be modified

    :param const struct v4l2_rect \*min_size:
        rect containing the minimal width and height

.. _`v4l2_rect_set_max_size`:

v4l2_rect_set_max_size
======================

.. c:function:: void v4l2_rect_set_max_size(struct v4l2_rect *r, const struct v4l2_rect *max_size)

    width and height of r should be <= max_size

    :param struct v4l2_rect \*r:
        rect whose width and height will be modified

    :param const struct v4l2_rect \*max_size:
        rect containing the maximum width and height

.. _`v4l2_rect_map_inside`:

v4l2_rect_map_inside
====================

.. c:function:: void v4l2_rect_map_inside(struct v4l2_rect *r, const struct v4l2_rect *boundary)

    r should be inside boundary.

    :param struct v4l2_rect \*r:
        rect that will be modified

    :param const struct v4l2_rect \*boundary:
        rect containing the boundary for \ ``r``\ 

.. _`v4l2_rect_same_size`:

v4l2_rect_same_size
===================

.. c:function:: bool v4l2_rect_same_size(const struct v4l2_rect *r1, const struct v4l2_rect *r2)

    return true if r1 has the same size as r2

    :param const struct v4l2_rect \*r1:
        rectangle.

    :param const struct v4l2_rect \*r2:
        rectangle.

.. _`v4l2_rect_same_size.description`:

Description
-----------

Return true if both rectangles have the same size.

.. _`v4l2_rect_intersect`:

v4l2_rect_intersect
===================

.. c:function:: void v4l2_rect_intersect(struct v4l2_rect *r, const struct v4l2_rect *r1, const struct v4l2_rect *r2)

    calculate the intersection of two rects.

    :param struct v4l2_rect \*r:
        intersection of \ ``r1``\  and \ ``r2``\ .

    :param const struct v4l2_rect \*r1:
        rectangle.

    :param const struct v4l2_rect \*r2:
        rectangle.

.. _`v4l2_rect_scale`:

v4l2_rect_scale
===============

.. c:function:: void v4l2_rect_scale(struct v4l2_rect *r, const struct v4l2_rect *from, const struct v4l2_rect *to)

    scale rect r by to/from

    :param struct v4l2_rect \*r:
        rect to be scaled.

    :param const struct v4l2_rect \*from:
        from rectangle.

    :param const struct v4l2_rect \*to:
        to rectangle.

.. _`v4l2_rect_scale.description`:

Description
-----------

This scales rectangle \ ``r``\  horizontally by \ ``to``\ ->width / \ ``from``\ ->width and
vertically by \ ``to``\ ->height / \ ``from``\ ->height.

Typically \ ``r``\  is a rectangle inside \ ``from``\  and you want the rectangle as
it would appear after scaling \ ``from``\  to \ ``to``\ . So the resulting \ ``r``\  will
be the scaled rectangle inside \ ``to``\ .

.. _`v4l2_rect_overlap`:

v4l2_rect_overlap
=================

.. c:function:: bool v4l2_rect_overlap(const struct v4l2_rect *r1, const struct v4l2_rect *r2)

    do r1 and r2 overlap?

    :param const struct v4l2_rect \*r1:
        rectangle.

    :param const struct v4l2_rect \*r2:
        rectangle.

.. _`v4l2_rect_overlap.description`:

Description
-----------

Returns true if \ ``r1``\  and \ ``r2``\  overlap.

.. This file was automatic generated / don't edit.

