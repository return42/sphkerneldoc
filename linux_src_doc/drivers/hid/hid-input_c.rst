.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/hid/hid-input.c

.. _`hidinput_calc_abs_res`:

hidinput_calc_abs_res
=====================

.. c:function:: __s32 hidinput_calc_abs_res(const struct hid_field *field, __u16 code)

    calculate an absolute axis resolution

    :param const struct hid_field \*field:
        the HID report field to calculate resolution for

    :param __u16 code:
        axis code

.. _`hidinput_calc_abs_res.the-formula-is`:

The formula is
--------------

(logical_maximum - logical_minimum)
resolution = ----------------------------------------------------------
(physical_maximum - physical_minimum) \* 10 ^ unit_exponent

as seen in the HID specification v1.11 6.2.2.7 Global Items.

Only exponent 1 length units are processed. Centimeters and inches are
converted to millimeters. Degrees are converted to radians.

.. This file was automatic generated / don't edit.

