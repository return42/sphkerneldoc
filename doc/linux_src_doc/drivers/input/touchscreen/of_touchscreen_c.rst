.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/input/touchscreen/of_touchscreen.c

.. _`touchscreen_parse_properties`:

touchscreen_parse_properties
============================

.. c:function:: void touchscreen_parse_properties(struct input_dev *input, bool multitouch)

    parse common touchscreen DT properties

    :param struct input_dev \*input:
        input device that should be parsed

    :param bool multitouch:
        specifies whether parsed properties should be applied to
        single-touch or multi-touch axes

.. _`touchscreen_parse_properties.description`:

Description
-----------

This function parses common DT properties for touchscreens and setups the
input device accordingly. The function keeps previously set up default
values if no value is specified via DT.

.. This file was automatic generated / don't edit.

