.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-subdev-pad-ops:

==========================
struct v4l2_subdev_pad_ops
==========================

*man struct v4l2_subdev_pad_ops(9)*

*4.6.0-rc5*

v4l2-subdev pad level operations


Synopsis
========

.. code-block:: c

    struct v4l2_subdev_pad_ops {
      int (* enum_mbus_code) (struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_mbus_code_enum *code);
      int (* enum_frame_size) (struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_frame_size_enum *fse);
      int (* enum_frame_interval) (struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_frame_interval_enum *fie);
      int (* get_fmt) (struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_format *format);
      int (* set_fmt) (struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_format *format);
      int (* get_selection) (struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_selection *sel);
      int (* set_selection) (struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_selection *sel);
      int (* get_edid) (struct v4l2_subdev *sd, struct v4l2_edid *edid);
      int (* set_edid) (struct v4l2_subdev *sd, struct v4l2_edid *edid);
      int (* dv_timings_cap) (struct v4l2_subdev *sd,struct v4l2_dv_timings_cap *cap);
      int (* enum_dv_timings) (struct v4l2_subdev *sd,struct v4l2_enum_dv_timings *timings);
    #ifdef CONFIG_MEDIA_CONTROLLER
      int (* link_validate) (struct v4l2_subdev *sd, struct media_link *link,struct v4l2_subdev_format *source_fmt,struct v4l2_subdev_format *sink_fmt);
    #endif
      int (* get_frame_desc) (struct v4l2_subdev *sd, unsigned int pad,struct v4l2_mbus_frame_desc *fd);
      int (* set_frame_desc) (struct v4l2_subdev *sd, unsigned int pad,struct v4l2_mbus_frame_desc *fd);
    };


Members
=======

enum_mbus_code
    callback for VIDIOC_SUBDEV_ENUM_MBUS_CODE ioctl handler code.

enum_frame_size
    callback for VIDIOC_SUBDEV_ENUM_FRAME_SIZE ioctl handler code.

enum_frame_interval
    callback for VIDIOC_SUBDEV_ENUM_FRAME_INTERVAL ioctl handler
    code.

get_fmt
    callback for VIDIOC_SUBDEV_G_FMT ioctl handler code.

set_fmt
    callback for VIDIOC_SUBDEV_S_FMT ioctl handler code.

get_selection
    callback for VIDIOC_SUBDEV_G_SELECTION ioctl handler code.

set_selection
    callback for VIDIOC_SUBDEV_S_SELECTION ioctl handler code.

get_edid
    callback for VIDIOC_SUBDEV_G_EDID ioctl handler code.

set_edid
    callback for VIDIOC_SUBDEV_S_EDID ioctl handler code.

dv_timings_cap
    callback for VIDIOC_SUBDEV_DV_TIMINGS_CAP ioctl handler code.

enum_dv_timings
    callback for VIDIOC_SUBDEV_ENUM_DV_TIMINGS ioctl handler code.

link_validate
    used by the media controller code to check if the links that belongs
    to a pipeline can be used for stream.

get_frame_desc
    get the current low level media bus frame parameters.

set_frame_desc
    set the low level media bus frame parameters, ``fd`` array may be
    adjusted by the subdev driver to device capabilities.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
