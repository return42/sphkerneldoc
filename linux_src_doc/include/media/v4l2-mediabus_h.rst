.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-mediabus.h

.. _`v4l2_mbus_type`:

enum v4l2_mbus_type
===================

.. c:type:: enum v4l2_mbus_type

    media bus type

.. _`v4l2_mbus_type.definition`:

Definition
----------

.. code-block:: c

    enum v4l2_mbus_type {
        V4L2_MBUS_UNKNOWN,
        V4L2_MBUS_PARALLEL,
        V4L2_MBUS_BT656,
        V4L2_MBUS_CSI1,
        V4L2_MBUS_CCP2,
        V4L2_MBUS_CSI2_DPHY,
        V4L2_MBUS_CSI2_CPHY
    };

.. _`v4l2_mbus_type.constants`:

Constants
---------

V4L2_MBUS_UNKNOWN
    unknown bus type, no V4L2 mediabus configuration

V4L2_MBUS_PARALLEL
    parallel interface with hsync and vsync

V4L2_MBUS_BT656
    parallel interface with embedded synchronisation, can
    also be used for BT.1120

V4L2_MBUS_CSI1
    MIPI CSI-1 serial interface

V4L2_MBUS_CCP2
    CCP2 (Compact Camera Port 2)

V4L2_MBUS_CSI2_DPHY
    MIPI CSI-2 serial interface, with D-PHY

V4L2_MBUS_CSI2_CPHY
    MIPI CSI-2 serial interface, with C-PHY

.. _`v4l2_mbus_config`:

struct v4l2_mbus_config
=======================

.. c:type:: struct v4l2_mbus_config

    media bus configuration

.. _`v4l2_mbus_config.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_mbus_config {
        enum v4l2_mbus_type type;
        unsigned int flags;
    }

.. _`v4l2_mbus_config.members`:

Members
-------

type
    in: interface type

flags
    in / out: configuration flags, depending on \ ``type``\ 

.. _`v4l2_fill_pix_format`:

v4l2_fill_pix_format
====================

.. c:function:: void v4l2_fill_pix_format(struct v4l2_pix_format *pix_fmt, const struct v4l2_mbus_framefmt *mbus_fmt)

    Ancillary routine that fills a \ :c:type:`struct v4l2_pix_format <v4l2_pix_format>`\  fields from a \ :c:type:`struct v4l2_mbus_framefmt <v4l2_mbus_framefmt>`\ .

    :param pix_fmt:
        pointer to \ :c:type:`struct v4l2_pix_format <v4l2_pix_format>`\  to be filled
    :type pix_fmt: struct v4l2_pix_format \*

    :param mbus_fmt:
        pointer to \ :c:type:`struct v4l2_mbus_framefmt <v4l2_mbus_framefmt>`\  to be used as model
    :type mbus_fmt: const struct v4l2_mbus_framefmt \*

.. _`v4l2_fill_mbus_format`:

v4l2_fill_mbus_format
=====================

.. c:function:: void v4l2_fill_mbus_format(struct v4l2_mbus_framefmt *mbus_fmt, const struct v4l2_pix_format *pix_fmt, u32 code)

    Ancillary routine that fills a \ :c:type:`struct v4l2_mbus_framefmt <v4l2_mbus_framefmt>`\  from a \ :c:type:`struct v4l2_pix_format <v4l2_pix_format>`\  and a data format code.

    :param mbus_fmt:
        pointer to \ :c:type:`struct v4l2_mbus_framefmt <v4l2_mbus_framefmt>`\  to be filled
    :type mbus_fmt: struct v4l2_mbus_framefmt \*

    :param pix_fmt:
        pointer to \ :c:type:`struct v4l2_pix_format <v4l2_pix_format>`\  to be used as model
    :type pix_fmt: const struct v4l2_pix_format \*

    :param code:
        data format code (from \ :c:type:`enum v4l2_mbus_pixelcode <v4l2_mbus_pixelcode>`\ )
    :type code: u32

.. _`v4l2_fill_pix_format_mplane`:

v4l2_fill_pix_format_mplane
===========================

.. c:function:: void v4l2_fill_pix_format_mplane(struct v4l2_pix_format_mplane *pix_mp_fmt, const struct v4l2_mbus_framefmt *mbus_fmt)

    Ancillary routine that fills a \ :c:type:`struct v4l2_pix_format_mplane <v4l2_pix_format_mplane>`\  fields from a media bus structure.

    :param pix_mp_fmt:
        pointer to \ :c:type:`struct v4l2_pix_format_mplane <v4l2_pix_format_mplane>`\  to be filled
    :type pix_mp_fmt: struct v4l2_pix_format_mplane \*

    :param mbus_fmt:
        pointer to \ :c:type:`struct v4l2_mbus_framefmt <v4l2_mbus_framefmt>`\  to be used as model
    :type mbus_fmt: const struct v4l2_mbus_framefmt \*

.. _`v4l2_fill_mbus_format_mplane`:

v4l2_fill_mbus_format_mplane
============================

.. c:function:: void v4l2_fill_mbus_format_mplane(struct v4l2_mbus_framefmt *mbus_fmt, const struct v4l2_pix_format_mplane *pix_mp_fmt)

    Ancillary routine that fills a \ :c:type:`struct v4l2_mbus_framefmt <v4l2_mbus_framefmt>`\  from a \ :c:type:`struct v4l2_pix_format_mplane <v4l2_pix_format_mplane>`\ .

    :param mbus_fmt:
        pointer to \ :c:type:`struct v4l2_mbus_framefmt <v4l2_mbus_framefmt>`\  to be filled
    :type mbus_fmt: struct v4l2_mbus_framefmt \*

    :param pix_mp_fmt:
        pointer to \ :c:type:`struct v4l2_pix_format_mplane <v4l2_pix_format_mplane>`\  to be used as model
    :type pix_mp_fmt: const struct v4l2_pix_format_mplane \*

.. This file was automatic generated / don't edit.

