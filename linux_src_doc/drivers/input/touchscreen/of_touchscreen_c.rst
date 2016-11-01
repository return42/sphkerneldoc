.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/touchscreen/of_touchscreen.c

.. _`touchscreen_parse_properties`:

touchscreen_parse_properties
============================

.. c:function:: void touchscreen_parse_properties(struct input_dev *input, bool multitouch, struct touchscreen_properties *prop)

    parse common touchscreen DT properties

    :param struct input_dev \*input:
        input device that should be parsed

    :param bool multitouch:
        specifies whether parsed properties should be applied to
        single-touch or multi-touch axes

    :param struct touchscreen_properties \*prop:
        pointer to a struct touchscreen_properties into which to store
        axis swap and invert info for use with \ :c:func:`touchscreen_report_x_y`\ ;
        or \ ``NULL``\ 

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

    :param struct input_mt_pos \*pos:
        input_mt_pos to set coordinates of

    :param const struct touchscreen_properties \*prop:
        pointer to a struct touchscreen_properties

    :param unsigned int x:
        X coordinate to store in pos

    :param unsigned int y:
        Y coordinate to store in pos

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

    :param struct input_dev \*input:
        input_device to report coordinates for

    :param const struct touchscreen_properties \*prop:
        pointer to a struct touchscreen_properties

    :param unsigned int x:
        X coordinate to report

    :param unsigned int y:
        Y coordinate to report

    :param bool multitouch:
        Report coordinates on single-touch or multi-touch axes

.. _`touchscreen_report_pos.description`:

Description
-----------

Adjust the passed in x and y values applying any axis inversion and
swapping requested in the passed in touchscreen_properties and then
report the resulting coordinates on the input_dev's x and y axis.

.. This file was automatic generated / don't edit.

