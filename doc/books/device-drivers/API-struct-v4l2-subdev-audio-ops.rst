.. -*- coding: utf-8; mode: rst -*-

.. _API-struct-v4l2-subdev-audio-ops:

============================
struct v4l2_subdev_audio_ops
============================

*man struct v4l2_subdev_audio_ops(9)*

*4.6.0-rc5*

Callbacks used for audio-related settings


Synopsis
========

.. code-block:: c

    struct v4l2_subdev_audio_ops {
      int (* s_clock_freq) (struct v4l2_subdev *sd, u32 freq);
      int (* s_i2s_clock_freq) (struct v4l2_subdev *sd, u32 freq);
      int (* s_routing) (struct v4l2_subdev *sd, u32 input, u32 output, u32 config);
      int (* s_stream) (struct v4l2_subdev *sd, int enable);
    };


Members
=======

s_clock_freq
    set the frequency (in Hz) of the audio clock output. Used to slave
    an audio processor to the video decoder, ensuring that audio and
    video remain synchronized. Usual values for the frequency are 48000,
    44100 or 32000 Hz. If the frequency is not supported, then -EINVAL
    is returned.

s_i2s_clock_freq
    sets I2S speed in bps. This is used to provide a standard way to
    select I2S clock used by driving digital audio streams at some board
    designs. Usual values for the frequency are 1024000 and 2048000. If
    the frequency is not supported, then -EINVAL is returned.

s_routing
    used to define the input and/or output pins of an audio chip, and
    any additional configuration data. Never attempt to use user-level
    input IDs (e.g. Composite, S-Video, Tuner) at this level. An i2c
    device shouldn't know about whether an input pin is connected to a
    Composite connector, become on another board or platform it might be
    connected to something else entirely. The calling driver is
    responsible for mapping a user-level input to the right pins on the
    i2c device.

s_stream
    used to notify the audio code that stream will start or has stopped.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
