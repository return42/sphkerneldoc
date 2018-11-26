.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/misc/lis3lv02d/lis3lv02d.c

.. _`lis3lv02d_get_axis`:

lis3lv02d_get_axis
==================

.. c:function:: int lis3lv02d_get_axis(s8 axis, int hw_values)

    For the given axis, give the value converted

    :param axis:
        1,2,3 - can also be negative
    :type axis: s8

    :param hw_values:
        raw values returned by the hardware
    :type hw_values: int

.. _`lis3lv02d_get_axis.description`:

Description
-----------

Returns the converted value.

.. _`lis3lv02d_get_xyz`:

lis3lv02d_get_xyz
=================

.. c:function:: void lis3lv02d_get_xyz(struct lis3lv02d *lis3, int *x, int *y, int *z)

    Get X, Y and Z axis values from the accelerometer

    :param lis3:
        pointer to the device struct
    :type lis3: struct lis3lv02d \*

    :param x:
        where to store the X axis value
    :type x: int \*

    :param y:
        where to store the Y axis value
    :type y: int \*

    :param z:
        where to store the Z axis value
    :type z: int \*

.. _`lis3lv02d_get_xyz.description`:

Description
-----------

Note that 40Hz input device can eat up about 10% CPU at 800MHZ

.. This file was automatic generated / don't edit.

