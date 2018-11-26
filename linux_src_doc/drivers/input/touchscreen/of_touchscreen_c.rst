.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/touchscreen/of_touchscreen.c

.. _`touchscreen_parse_properties`:

touchscreen_parse_properties
============================

.. c:function:: void touchscreen_parse_properties(struct input_dev *input, bool multitouch, struct touchscreen_properties *prop)

    parse common touchscreen DT properties

    :param input:
        input device that should be parsed
    :type input: struct input_dev \*

    :param multitouch:
        specifies whether parsed properties should be applied to
        single-touch or multi-touch axes
    :type multitouch: bool

    :param prop:
        pointer to a struct touchscreen_properties into which to store
        axis swap and invert info for use with \ :c:func:`touchscreen_report_x_y`\ ;
        or \ ``NULL``\ 
    :type prop: struct touchscreen_properties \*

.. _`touchscreen_parse_properties.description`:

Description
-----------

This function parses common DT properties for touchscreens and setups the
input device accordingly. The function keeps previously set up default
values if no value is specified via DT.

.. _`touchscreen_set_mt_pos`:

touchscreen_set_mt_pos
======================

.. c:function:: void touchscreen_set_mt_pos(struct input_mt_pos *pos, const struct touchscreen_properties *prop, unsigned int x, unsigned int y)

    Set input_mt_pos coordinates

    :param pos:
        input_mt_pos to set coordinates of
    :type pos: struct input_mt_pos \*

    :param prop:
        pointer to a struct touchscreen_properties
    :type prop: const struct touchscreen_properties \*

    :param x:
        X coordinate to store in pos
    :type x: unsigned int

    :param y:
        Y coordinate to store in pos
    :type y: unsigned int

.. _`touchscreen_set_mt_pos.description`:

Description
-----------

Adjust the passed in x and y values applying any axis inversion and
swapping requested in the passed in touchscreen_properties and store
the result in a struct input_mt_pos.

.. _`touchscreen_report_pos`:

touchscreen_report_pos
======================

.. c:function:: void touchscreen_report_pos(struct input_dev *input, const struct touchscreen_properties *prop, unsigned int x, unsigned int y, bool multitouch)

    Report touchscreen coordinates

    :param input:
        input_device to report coordinates for
    :type input: struct input_dev \*

    :param prop:
        pointer to a struct touchscreen_properties
    :type prop: const struct touchscreen_properties \*

    :param x:
        X coordinate to report
    :type x: unsigned int

    :param y:
        Y coordinate to report
    :type y: unsigned int

    :param multitouch:
        Report coordinates on single-touch or multi-touch axes
    :type multitouch: bool

.. _`touchscreen_report_pos.description`:

Description
-----------

Adjust the passed in x and y values applying any axis inversion and
swapping requested in the passed in touchscreen_properties and then
report the resulting coordinates on the input_dev's x and y axis.

.. This file was automatic generated / don't edit.

