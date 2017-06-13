.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/lis3lv02d/lis3lv02d.c

.. _`lis3lv02d_get_axis`:

lis3lv02d_get_axis
==================

.. c:function:: int lis3lv02d_get_axis(s8 axis, int hw_values)

    For the given axis, give the value converted

    :param s8 axis:
        1,2,3 - can also be negative

    :param int hw_values:
        raw values returned by the hardware

.. _`lis3lv02d_get_axis.description`:

Description
-----------

Returns the converted value.

.. _`lis3lv02d_get_xyz`:

lis3lv02d_get_xyz
=================

.. c:function:: void lis3lv02d_get_xyz(struct lis3lv02d *lis3, int *x, int *y, int *z)

    Get X, Y and Z axis values from the accelerometer

    :param struct lis3lv02d \*lis3:
        pointer to the device struct

    :param int \*x:
        where to store the X axis value

    :param int \*y:
        where to store the Y axis value

    :param int \*z:
        where to store the Z axis value

.. _`lis3lv02d_get_xyz.description`:

Description
-----------

Note that 40Hz input device can eat up about 10% CPU at 800MHZ

.. This file was automatic generated / don't edit.

