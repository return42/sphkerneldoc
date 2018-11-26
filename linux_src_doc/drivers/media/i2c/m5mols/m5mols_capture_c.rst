.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/m5mols/m5mols_capture.c

.. _`m5mols_read_rational`:

m5mols_read_rational
====================

.. c:function:: int m5mols_read_rational(struct v4l2_subdev *sd, u32 addr_num, u32 addr_den, u32 *val)

    I2C read of a rational number

    :param sd:
        sub-device, as pointed by struct v4l2_subdev
    :type sd: struct v4l2_subdev \*

    :param addr_num:
        numerator register
    :type addr_num: u32

    :param addr_den:
        denominator register
    :type addr_den: u32

    :param val:
        place to store the division result
    :type val: u32 \*

.. _`m5mols_read_rational.description`:

Description
-----------

Read numerator and denominator from registers \ ``addr_num``\  and \ ``addr_den``\ 
respectively and return the division result in \ ``val``\ .

.. _`m5mols_capture_info`:

m5mols_capture_info
===================

.. c:function:: int m5mols_capture_info(struct m5mols_info *info)

    Gather captured image information

    :param info:
        M-5MOLS driver data structure
    :type info: struct m5mols_info \*

.. _`m5mols_capture_info.description`:

Description
-----------

For now it gathers only EXIF information and file size.

.. This file was automatic generated / don't edit.

