.. -*- coding: utf-8; mode: rst -*-

================
m5mols_capture.c
================



.. _xref_m5mols_read_rational:

m5mols_read_rational
====================

.. c:function:: int m5mols_read_rational (struct v4l2_subdev * sd, u32 addr_num, u32 addr_den, u32 * val)

    I2C read of a rational number

    :param struct v4l2_subdev * sd:

        _undescribed_

    :param u32 addr_num:

        _undescribed_

    :param u32 addr_den:

        _undescribed_

    :param u32 * val:

        _undescribed_



Description
-----------



Read numerator and denominator from registers **addr_num** and **addr_den**
respectively and return the division result in **val**.




.. _xref_m5mols_capture_info:

m5mols_capture_info
===================

.. c:function:: int m5mols_capture_info (struct m5mols_info * info)

    Gather captured image information

    :param struct m5mols_info * info:

        _undescribed_



Description
-----------



For now it gathers only EXIF information and file size.


