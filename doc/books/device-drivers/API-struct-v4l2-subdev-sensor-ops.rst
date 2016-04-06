
.. _API-struct-v4l2-subdev-sensor-ops:

=============================
struct v4l2_subdev_sensor_ops
=============================

*man struct v4l2_subdev_sensor_ops(9)*

*4.6.0-rc1*

v4l2-subdev sensor operations


Synopsis
========

.. code-block:: c

    struct v4l2_subdev_sensor_ops {
      int (* g_skip_top_lines) (struct v4l2_subdev *sd, u32 *lines);
      int (* g_skip_frames) (struct v4l2_subdev *sd, u32 *frames);
    };


Members
=======

g_skip_top_lines
    number of lines at the top of the image to be skipped. This is needed for some sensors, which always corrupt several top lines of the output image, or which send their metadata
    in them.

g_skip_frames
    number of frames to skip at stream start. This is needed for buggy sensors that generate faulty frames when they are turned on.
