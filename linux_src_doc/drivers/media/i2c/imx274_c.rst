.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/imx274.c

.. _`imx274_read_mbreg`:

imx274_read_mbreg
=================

.. c:function:: int imx274_read_mbreg(struct stimx274 *priv, u16 addr, u32 *val, size_t nbytes)

    :param priv:
        Pointer to device structure
    :type priv: struct stimx274 \*

    :param addr:
        Address of the LSB register.  Other registers must be
        consecutive, least-to-most significant.
    :type addr: u16

    :param val:
        Pointer to store the register value (cpu endianness)
    :type val: u32 \*

    :param nbytes:
        Number of bytes to read (range: [1..3]).
        Other bytes are zet to 0.
    :type nbytes: size_t

.. _`imx274_read_mbreg.description`:

Description
-----------

Uses a bulk read where possible.

.. _`imx274_read_mbreg.return`:

Return
------

0 on success, errors otherwise

.. _`imx274_write_mbreg`:

imx274_write_mbreg
==================

.. c:function:: int imx274_write_mbreg(struct stimx274 *priv, u16 addr, u32 val, size_t nbytes)

    :param priv:
        Pointer to device structure
    :type priv: struct stimx274 \*

    :param addr:
        Address of the LSB register.  Other registers must be
        consecutive, least-to-most significant.
    :type addr: u16

    :param val:
        Value to be written to the register (cpu endianness)
    :type val: u32

    :param nbytes:
        Number of bytes to write (range: [1..3])
    :type nbytes: size_t

.. _`imx274_write_mbreg.description`:

Description
-----------

Uses a bulk write where possible.

.. _`imx274_s_ctrl`:

imx274_s_ctrl
=============

.. c:function:: int imx274_s_ctrl(struct v4l2_ctrl *ctrl)

    This is used to set the imx274 V4L2 controls

    :param ctrl:
        V4L2 control to be set
    :type ctrl: struct v4l2_ctrl \*

.. _`imx274_s_ctrl.description`:

Description
-----------

This function is used to set the V4L2 controls for the imx274 sensor.

.. _`imx274_s_ctrl.return`:

Return
------

0 on success, errors otherwise

.. _`__imx274_change_compose`:

\__imx274_change_compose
========================

.. c:function:: int __imx274_change_compose(struct stimx274 *imx274, struct v4l2_subdev_pad_config *cfg, u32 which, u32 *width, u32 *height, u32 flags)

    :param imx274:
        The device object
    :type imx274: struct stimx274 \*

    :param cfg:
        The pad config we are editing for TRY requests
    :type cfg: struct v4l2_subdev_pad_config \*

    :param which:
        V4L2_SUBDEV_FORMAT_ACTIVE or V4L2_SUBDEV_FORMAT_TRY from the caller
    :type which: u32

    :param width:
        Input-output parameter: set to the desired width before
        the call, contains the chosen value after returning successfully
    :type width: u32 \*

    :param height:
        Input-output parameter for height (see \ ``width``\ )
    :type height: u32 \*

    :param flags:
        Selection flags from struct v4l2_subdev_selection, or 0 if not
        available (when called from set_fmt)
    :type flags: u32

.. _`__imx274_change_compose.we-have-two-entry-points-to-change-binning`:

We have two entry points to change binning
------------------------------------------

set_fmt and
set_selection(COMPOSE). Both have to compute the new output size
and set it in both the compose rect and the frame format size. We
also need to do the same things after setting cropping to restore
1:1 binning.

This function contains the common code for these three cases, it
has many arguments in order to accommodate the needs of all of
them.

Must be called with imx274->lock locked.

.. _`imx274_get_fmt`:

imx274_get_fmt
==============

.. c:function:: int imx274_get_fmt(struct v4l2_subdev *sd, struct v4l2_subdev_pad_config *cfg, struct v4l2_subdev_format *fmt)

    Get the pad format

    :param sd:
        Pointer to V4L2 Sub device structure
    :type sd: struct v4l2_subdev \*

    :param cfg:
        Pointer to sub device pad information structure
    :type cfg: struct v4l2_subdev_pad_config \*

    :param fmt:
        Pointer to pad level media bus format
    :type fmt: struct v4l2_subdev_format \*

.. _`imx274_get_fmt.description`:

Description
-----------

This function is used to get the pad format information.

.. _`imx274_get_fmt.return`:

Return
------

0 on success

.. _`imx274_set_fmt`:

imx274_set_fmt
==============

.. c:function:: int imx274_set_fmt(struct v4l2_subdev *sd, struct v4l2_subdev_pad_config *cfg, struct v4l2_subdev_format *format)

    This is used to set the pad format

    :param sd:
        Pointer to V4L2 Sub device structure
    :type sd: struct v4l2_subdev \*

    :param cfg:
        Pointer to sub device pad information structure
    :type cfg: struct v4l2_subdev_pad_config \*

    :param format:
        Pointer to pad level media bus format
    :type format: struct v4l2_subdev_format \*

.. _`imx274_set_fmt.description`:

Description
-----------

This function is used to set the pad format.

.. _`imx274_set_fmt.return`:

Return
------

0 on success

.. _`imx274_g_frame_interval`:

imx274_g_frame_interval
=======================

.. c:function:: int imx274_g_frame_interval(struct v4l2_subdev *sd, struct v4l2_subdev_frame_interval *fi)

    Get the frame interval

    :param sd:
        Pointer to V4L2 Sub device structure
    :type sd: struct v4l2_subdev \*

    :param fi:
        Pointer to V4l2 Sub device frame interval structure
    :type fi: struct v4l2_subdev_frame_interval \*

.. _`imx274_g_frame_interval.description`:

Description
-----------

This function is used to get the frame interval.

.. _`imx274_g_frame_interval.return`:

Return
------

0 on success

.. _`imx274_s_frame_interval`:

imx274_s_frame_interval
=======================

.. c:function:: int imx274_s_frame_interval(struct v4l2_subdev *sd, struct v4l2_subdev_frame_interval *fi)

    Set the frame interval

    :param sd:
        Pointer to V4L2 Sub device structure
    :type sd: struct v4l2_subdev \*

    :param fi:
        Pointer to V4l2 Sub device frame interval structure
    :type fi: struct v4l2_subdev_frame_interval \*

.. _`imx274_s_frame_interval.description`:

Description
-----------

This function is used to set the frame intervavl.

.. _`imx274_s_frame_interval.return`:

Return
------

0 on success

.. _`imx274_load_default`:

imx274_load_default
===================

.. c:function:: int imx274_load_default(struct stimx274 *priv)

    load default control values

    :param priv:
        Pointer to device structure
    :type priv: struct stimx274 \*

.. _`imx274_load_default.return`:

Return
------

0 on success, errors otherwise

.. _`imx274_s_stream`:

imx274_s_stream
===============

.. c:function:: int imx274_s_stream(struct v4l2_subdev *sd, int on)

    It is used to start/stop the streaming.

    :param sd:
        V4L2 Sub device
    :type sd: struct v4l2_subdev \*

    :param on:
        Flag (True / False)
    :type on: int

.. _`imx274_s_stream.description`:

Description
-----------

This function controls the start or stop of streaming for the
imx274 sensor.

.. _`imx274_s_stream.return`:

Return
------

0 on success, errors otherwise

.. This file was automatic generated / don't edit.

