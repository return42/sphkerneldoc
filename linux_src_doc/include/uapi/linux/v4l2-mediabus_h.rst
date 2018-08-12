.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/uapi/linux/v4l2-mediabus.h

.. _`v4l2_mbus_framefmt`:

struct v4l2_mbus_framefmt
=========================

.. c:type:: struct v4l2_mbus_framefmt

    frame format on the media bus

.. _`v4l2_mbus_framefmt.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_mbus_framefmt {
        __u32 width;
        __u32 height;
        __u32 code;
        __u32 field;
        __u32 colorspace;
        __u16 ycbcr_enc;
        __u16 quantization;
        __u16 xfer_func;
        __u16 reserved[11];
    }

.. _`v4l2_mbus_framefmt.members`:

Members
-------

width
    image width

height
    image height

code
    data format code (from enum v4l2_mbus_pixelcode)

field
    used interlacing type (from enum v4l2_field)

colorspace
    colorspace of the data (from enum v4l2_colorspace)

ycbcr_enc
    YCbCr encoding of the data (from enum v4l2_ycbcr_encoding)

quantization
    quantization of the data (from enum v4l2_quantization)

xfer_func
    transfer function of the data (from enum v4l2_xfer_func)

reserved
    *undescribed*

.. This file was automatic generated / don't edit.

