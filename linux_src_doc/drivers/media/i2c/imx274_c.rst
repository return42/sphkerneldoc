.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/imx274.c

.. _`imx274_s_ctrl`:

imx274_s_ctrl
=============

.. c:function:: int imx274_s_ctrl(struct v4l2_ctrl *ctrl)

    This is used to set the imx274 V4L2 controls

    :param struct v4l2_ctrl \*ctrl:
        V4L2 control to be set

.. _`imx274_s_ctrl.description`:

Description
-----------

This function is used to set the V4L2 controls for the imx274 sensor.

.. _`imx274_s_ctrl.return`:

Return
------

0 on success, errors otherwise

.. _`imx274_get_fmt`:

imx274_get_fmt
==============

.. c:function:: int imx274_get_fmt(struct v4l2_subdev *sd, struct v4l2_subdev_pad_config *cfg, struct v4l2_subdev_format *fmt)

    Get the pad format

    :param struct v4l2_subdev \*sd:
        Pointer to V4L2 Sub device structure

    :param struct v4l2_subdev_pad_config \*cfg:
        Pointer to sub device pad information structure

    :param struct v4l2_subdev_format \*fmt:
        Pointer to pad level media bus format

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

    :param struct v4l2_subdev \*sd:
        Pointer to V4L2 Sub device structure

    :param struct v4l2_subdev_pad_config \*cfg:
        Pointer to sub device pad information structure

    :param struct v4l2_subdev_format \*format:
        Pointer to pad level media bus format

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

    :param struct v4l2_subdev \*sd:
        Pointer to V4L2 Sub device structure

    :param struct v4l2_subdev_frame_interval \*fi:
        Pointer to V4l2 Sub device frame interval structure

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

    :param struct v4l2_subdev \*sd:
        Pointer to V4L2 Sub device structure

    :param struct v4l2_subdev_frame_interval \*fi:
        Pointer to V4l2 Sub device frame interval structure

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

    :param struct stimx274 \*priv:
        Pointer to device structure

.. _`imx274_load_default.return`:

Return
------

0 on success, errors otherwise

.. _`imx274_s_stream`:

imx274_s_stream
===============

.. c:function:: int imx274_s_stream(struct v4l2_subdev *sd, int on)

    It is used to start/stop the streaming.

    :param struct v4l2_subdev \*sd:
        V4L2 Sub device

    :param int on:
        Flag (True / False)

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

