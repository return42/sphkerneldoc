
.. _API-struct-v4l2-subdev-video-ops:

============================
struct v4l2_subdev_video_ops
============================

*man struct v4l2_subdev_video_ops(9)*

*4.6.0-rc1*

Callbacks used when v4l device was opened in video mode.


Synopsis
========

.. code-block:: c

    struct v4l2_subdev_video_ops {
      int (* s_routing) (struct v4l2_subdev *sd, u32 input, u32 output, u32 config);
      int (* s_crystal_freq) (struct v4l2_subdev *sd, u32 freq, u32 flags);
      int (* g_std) (struct v4l2_subdev *sd, v4l2_std_id *norm);
      int (* s_std) (struct v4l2_subdev *sd, v4l2_std_id norm);
      int (* s_std_output) (struct v4l2_subdev *sd, v4l2_std_id std);
      int (* g_std_output) (struct v4l2_subdev *sd, v4l2_std_id *std);
      int (* querystd) (struct v4l2_subdev *sd, v4l2_std_id *std);
      int (* g_tvnorms) (struct v4l2_subdev *sd, v4l2_std_id *std);
      int (* g_tvnorms_output) (struct v4l2_subdev *sd, v4l2_std_id *std);
      int (* g_input_status) (struct v4l2_subdev *sd, u32 *status);
      int (* s_stream) (struct v4l2_subdev *sd, int enable);
      int (* cropcap) (struct v4l2_subdev *sd, struct v4l2_cropcap *cc);
      int (* g_crop) (struct v4l2_subdev *sd, struct v4l2_crop *crop);
      int (* s_crop) (struct v4l2_subdev *sd, const struct v4l2_crop *crop);
      int (* g_parm) (struct v4l2_subdev *sd, struct v4l2_streamparm *param);
      int (* s_parm) (struct v4l2_subdev *sd, struct v4l2_streamparm *param);
      int (* g_frame_interval) (struct v4l2_subdev *sd,struct v4l2_subdev_frame_interval *interval);
      int (* s_frame_interval) (struct v4l2_subdev *sd,struct v4l2_subdev_frame_interval *interval);
      int (* s_dv_timings) (struct v4l2_subdev *sd,struct v4l2_dv_timings *timings);
      int (* g_dv_timings) (struct v4l2_subdev *sd,struct v4l2_dv_timings *timings);
      int (* query_dv_timings) (struct v4l2_subdev *sd,struct v4l2_dv_timings *timings);
      int (* g_mbus_config) (struct v4l2_subdev *sd,struct v4l2_mbus_config *cfg);
      int (* s_mbus_config) (struct v4l2_subdev *sd,const struct v4l2_mbus_config *cfg);
      int (* s_rx_buffer) (struct v4l2_subdev *sd, void *buf,unsigned int *size);
    };


Members
=======

s_routing
    see s_routing in audio_ops, except this version is for video devices.

s_crystal_freq
    sets the frequency of the crystal used to generate the clocks in Hz. An extra flags field allows device specific configuration regarding clock frequency dividers, etc. If not
    used, then set flags to 0. If the frequency is not supported, then -EINVAL is returned.

g_std
    callback for VIDIOC_G_STD ioctl handler code.

s_std
    callback for VIDIOC_S_STD ioctl handler code.

s_std_output
    set v4l2_std_id for video OUTPUT devices. This is ignored by video input devices.

g_std_output
    get current standard for video OUTPUT devices. This is ignored by video input devices.

querystd
    callback for VIDIOC_QUERYSTD ioctl handler code.

g_tvnorms
    get v4l2_std_id with all standards supported by the video CAPTURE device. This is ignored by video output devices.

g_tvnorms_output
    get v4l2_std_id with all standards supported by the video OUTPUT device. This is ignored by video capture devices.

g_input_status
    get input status. Same as the status field in the v4l2_input struct.

s_stream
    used to notify the driver that a video stream will start or has stopped.

cropcap
    callback for VIDIOC_CROPCAP ioctl handler code.

g_crop
    callback for VIDIOC_G_CROP ioctl handler code.

s_crop
    callback for VIDIOC_S_CROP ioctl handler code.

g_parm
    callback for VIDIOC_G_PARM ioctl handler code.

s_parm
    callback for VIDIOC_S_PARM ioctl handler code.

g_frame_interval
    callback for VIDIOC_G_FRAMEINTERVAL ioctl handler code.

s_frame_interval
    callback for VIDIOC_S_FRAMEINTERVAL ioctl handler code.

s_dv_timings
    Set custom dv timings in the sub device. This is used when sub device is capable of setting detailed timing information in the hardware to generate/detect the video signal.

g_dv_timings
    Get custom dv timings in the sub device.

query_dv_timings
    callback for VIDIOC_QUERY_DV_TIMINGS ioctl handler code.

g_mbus_config
    get supported mediabus configurations

s_mbus_config
    set a certain mediabus configuration. This operation is added for compatibility with soc-camera drivers and should not be used by new software.

s_rx_buffer
    set a host allocated memory buffer for the subdev. The subdev can adjust ``size`` to a lower value and must not write more data to the buffer starting at ``data`` than the
    original value of ``size``.
