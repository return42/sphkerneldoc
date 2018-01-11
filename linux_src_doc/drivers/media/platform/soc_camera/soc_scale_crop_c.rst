.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/platform/soc_camera/soc_scale_crop.c

.. _`soc_camera_client_scale`:

soc_camera_client_scale
=======================

.. c:function:: int soc_camera_client_scale(struct soc_camera_device *icd, struct v4l2_rect *rect, struct v4l2_rect *subrect, struct v4l2_mbus_framefmt *mf, unsigned int *width, unsigned int *height, bool host_can_scale, unsigned int shift)

    :param struct soc_camera_device \*icd:
        soc-camera device

    :param struct v4l2_rect \*rect:
        camera cropping window

    :param struct v4l2_rect \*subrect:
        part of rect, sent to the user

    :param struct v4l2_mbus_framefmt \*mf:
        in- / output camera output window

    :param unsigned int \*width:
        on input: max host input width;
        on output: user width, mapped back to input

    :param unsigned int \*height:
        on input: max host input height;
        on output: user height, mapped back to input

    :param bool host_can_scale:
        host can scale this pixel format

    :param unsigned int shift:
        shift, used for scaling

.. This file was automatic generated / don't edit.

