
.. _API-struct-v4l2-subdev-tuner-ops:

============================
struct v4l2_subdev_tuner_ops
============================

*man struct v4l2_subdev_tuner_ops(9)*

*4.6.0-rc1*

Callbacks used when v4l device was opened in radio mode.


Synopsis
========

.. code-block:: c

    struct v4l2_subdev_tuner_ops {
      int (* s_radio) (struct v4l2_subdev *sd);
      int (* s_frequency) (struct v4l2_subdev *sd, const struct v4l2_frequency *freq);
      int (* g_frequency) (struct v4l2_subdev *sd, struct v4l2_frequency *freq);
      int (* enum_freq_bands) (struct v4l2_subdev *sd, struct v4l2_frequency_band *band);
      int (* g_tuner) (struct v4l2_subdev *sd, struct v4l2_tuner *vt);
      int (* s_tuner) (struct v4l2_subdev *sd, const struct v4l2_tuner *vt);
      int (* g_modulator) (struct v4l2_subdev *sd, struct v4l2_modulator *vm);
      int (* s_modulator) (struct v4l2_subdev *sd, const struct v4l2_modulator *vm);
      int (* s_type_addr) (struct v4l2_subdev *sd, struct tuner_setup *type);
      int (* s_config) (struct v4l2_subdev *sd, const struct v4l2_priv_tun_config *config);
    };


Members
=======

s_radio
    callback for VIDIOC_S_RADIO ioctl handler code.

s_frequency
    callback for VIDIOC_S_FREQUENCY ioctl handler code.

g_frequency
    callback for VIDIOC_G_FREQUENCY ioctl handler code. freq->type must be filled in. Normally done by video_ioctl2 or the bridge driver.

enum_freq_bands
    callback for VIDIOC_ENUM_FREQ_BANDS ioctl handler code.

g_tuner
    callback for VIDIOC_G_TUNER ioctl handler code.

s_tuner
    callback for VIDIOC_S_TUNER ioctl handler code. vt->type must be filled in. Normally done by video_ioctl2 or the bridge driver.

g_modulator
    callback for VIDIOC_G_MODULATOR ioctl handler code.

s_modulator
    callback for VIDIOC_S_MODULATOR ioctl handler code.

s_type_addr
    sets tuner type and its I2C addr.

s_config
    sets tda9887 specific stuff, like port1, port2 and qss
