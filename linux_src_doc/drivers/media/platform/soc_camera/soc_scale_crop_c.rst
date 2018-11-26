.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/soc_camera/soc_scale_crop.c

.. _`soc_camera_client_scale`:

soc_camera_client_scale
=======================

.. c:function:: int soc_camera_client_scale(struct soc_camera_device *icd, struct v4l2_rect *rect, struct v4l2_rect *subrect, struct v4l2_mbus_framefmt *mf, unsigned int *width, unsigned int *height, bool host_can_scale, unsigned int shift)

    :param icd:
        soc-camera device
    :type icd: struct soc_camera_device \*

    :param rect:
        camera cropping window
    :type rect: struct v4l2_rect \*

    :param subrect:
        part of rect, sent to the user
    :type subrect: struct v4l2_rect \*

    :param mf:
        in- / output camera output window
    :type mf: struct v4l2_mbus_framefmt \*

    :param width:
        on input: max host input width;
        on output: user width, mapped back to input
    :type width: unsigned int \*

    :param height:
        on input: max host input height;
        on output: user height, mapped back to input
    :type height: unsigned int \*

    :param host_can_scale:
        host can scale this pixel format
    :type host_can_scale: bool

    :param shift:
        shift, used for scaling
    :type shift: unsigned int

.. This file was automatic generated / don't edit.

