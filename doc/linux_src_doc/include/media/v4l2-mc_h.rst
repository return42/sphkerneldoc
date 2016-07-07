.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-mc.h

.. _`tuner_pad_index`:

enum tuner_pad_index
====================

.. c:type:: enum tuner_pad_index

    tuner pad index for MEDIA_ENT_F_TUNER

.. _`tuner_pad_index.definition`:

Definition
----------

.. code-block:: c

    enum tuner_pad_index {
        TUNER_PAD_RF_INPUT,
        TUNER_PAD_OUTPUT,
        TUNER_PAD_AUD_OUT,
        TUNER_NUM_PADS
    };

.. _`tuner_pad_index.constants`:

Constants
---------

TUNER_PAD_RF_INPUT
    Radiofrequency (RF) sink pad, usually linked to a
    RF connector entity.

TUNER_PAD_OUTPUT
    Tuner video output source pad. Contains the video
    chrominance and luminance or the hole bandwidth
    of the signal converted to an Intermediate Frequency
    (IF) or to baseband (on zero-IF tuners).

TUNER_PAD_AUD_OUT
    Tuner audio output source pad. Tuners used to decode
    analog TV signals have an extra pad for audio output.
    Old tuners use an analog stage with a saw filter for
    the audio IF frequency. The output of the pad is, in
    this case, the audio IF, with should be decoded either
    by the bridge chipset (that's the case of cx2388x
    chipsets) or may require an external IF sound
    processor, like msp34xx. On modern silicon tuners,
    the audio IF decoder is usually incorporated at the
    tuner. On such case, the output of this pad is an
    audio sampled data.

TUNER_NUM_PADS
    Number of pads of the tuner.

.. _`if_vid_dec_pad_index`:

enum if_vid_dec_pad_index
=========================

.. c:type:: enum if_vid_dec_pad_index

    video IF-PLL pad index for MEDIA_ENT_F_IF_VID_DECODER

.. _`if_vid_dec_pad_index.definition`:

Definition
----------

.. code-block:: c

    enum if_vid_dec_pad_index {
        IF_VID_DEC_PAD_IF_INPUT,
        IF_VID_DEC_PAD_OUT,
        IF_VID_DEC_PAD_NUM_PADS
    };

.. _`if_vid_dec_pad_index.constants`:

Constants
---------

IF_VID_DEC_PAD_IF_INPUT
    video Intermediate Frequency (IF) sink pad

IF_VID_DEC_PAD_OUT
    IF-PLL video output source pad. Contains the
    video chrominance and luminance IF signals.

IF_VID_DEC_PAD_NUM_PADS
    Number of pads of the video IF-PLL.

.. _`if_aud_dec_pad_index`:

enum if_aud_dec_pad_index
=========================

.. c:type:: enum if_aud_dec_pad_index

    audio/sound IF-PLL pad index for MEDIA_ENT_F_IF_AUD_DECODER

.. _`if_aud_dec_pad_index.definition`:

Definition
----------

.. code-block:: c

    enum if_aud_dec_pad_index {
        IF_AUD_DEC_PAD_IF_INPUT,
        IF_AUD_DEC_PAD_OUT,
        IF_AUD_DEC_PAD_NUM_PADS
    };

.. _`if_aud_dec_pad_index.constants`:

Constants
---------

IF_AUD_DEC_PAD_IF_INPUT
    audio Intermediate Frequency (IF) sink pad

IF_AUD_DEC_PAD_OUT
    IF-PLL audio output source pad. Contains the
    audio sampled stream data, usually connected
    to the bridge bus via an Inter-IC Sound (I2S)
    bus.

IF_AUD_DEC_PAD_NUM_PADS
    Number of pads of the audio IF-PLL.

.. _`demod_pad_index`:

enum demod_pad_index
====================

.. c:type:: enum demod_pad_index

    analog TV pad index for MEDIA_ENT_F_ATV_DECODER

.. _`demod_pad_index.definition`:

Definition
----------

.. code-block:: c

    enum demod_pad_index {
        DEMOD_PAD_IF_INPUT,
        DEMOD_PAD_VID_OUT,
        DEMOD_PAD_VBI_OUT,
        DEMOD_PAD_AUDIO_OUT,
        DEMOD_NUM_PADS
    };

.. _`demod_pad_index.constants`:

Constants
---------

DEMOD_PAD_IF_INPUT
    IF input sink pad.

DEMOD_PAD_VID_OUT
    Video output source pad.

DEMOD_PAD_VBI_OUT
    Vertical Blank Interface (VBI) output source pad.

DEMOD_PAD_AUDIO_OUT
    Audio output source pad.

DEMOD_NUM_PADS
    Maximum number of output pads.

.. _`v4l2_mc_create_media_graph`:

v4l2_mc_create_media_graph
==========================

.. c:function:: int v4l2_mc_create_media_graph(struct media_device *mdev)

    create Media Controller links at the graph.

    :param struct media_device \*mdev:
        pointer to the \ :c:type:`struct media_device <media_device>` struct.

.. _`v4l2_mc_create_media_graph.description`:

Description
-----------

Add links between the entities commonly found on PC customer's hardware at

.. _`v4l2_mc_create_media_graph.the-v4l2-side`:

the V4L2 side
-------------

camera sensors, audio and video PLL-IF decoders, tuners,
analog TV decoder and I/O entities (video, VBI and Software Defined Radio).

.. _`v4l2_mc_create_media_graph.note`:

NOTE
----

webcams are modelled on a very simple way: the sensor is
connected directly to the I/O entity. All dirty details, like
scaler and crop HW are hidden. While such mapping is enough for v4l2
interface centric PC-consumer's hardware, V4L2 subdev centric camera
hardware should not use this routine, as it will not build the right graph.

.. _`v4l_enable_media_source`:

v4l_enable_media_source
=======================

.. c:function:: int v4l_enable_media_source(struct video_device *vdev)

    Hold media source for exclusive use if free

    :param struct video_device \*vdev:
        pointer to struct video_device

.. _`v4l_enable_media_source.description`:

Description
-----------

This interface calls enable_source handler to determine if
media source is free for use. The enable_source handler is
responsible for checking is the media source is free and
start a pipeline between the media source and the media
entity associated with the video device. This interface
should be called from v4l2-core and dvb-core interfaces
that change the source configuration.

.. _`v4l_enable_media_source.return`:

Return
------

returns zero on success or a negative error code.

.. _`v4l_disable_media_source`:

v4l_disable_media_source
========================

.. c:function:: void v4l_disable_media_source(struct video_device *vdev)

    Release media source

    :param struct video_device \*vdev:
        pointer to struct video_device

.. _`v4l_disable_media_source.description`:

Description
-----------

This interface calls disable_source handler to release
the media source. The disable_source handler stops the
active media pipeline between the media source and the
media entity associated with the video device.

.. _`v4l_disable_media_source.return`:

Return
------

returns zero on success or a negative error code.

.. _`v4l2_pipeline_pm_use`:

v4l2_pipeline_pm_use
====================

.. c:function:: int v4l2_pipeline_pm_use(struct media_entity *entity, int use)

    Update the use count of an entity

    :param struct media_entity \*entity:
        The entity

    :param int use:
        Use (1) or stop using (0) the entity

.. _`v4l2_pipeline_pm_use.description`:

Description
-----------

Update the use count of all entities in the pipeline and power entities on or
off accordingly.

This function is intended to be called in video node open (use ==
1) and release (use == 0). It uses struct media_entity.use_count to
track the power status. The use of this function should be paired
with \ :c:func:`v4l2_pipeline_link_notify`\ .

Return 0 on success or a negative error code on failure. Powering entities
off is assumed to never fail. No failure can occur when the use parameter is
set to 0.

.. _`v4l2_pipeline_link_notify`:

v4l2_pipeline_link_notify
=========================

.. c:function:: int v4l2_pipeline_link_notify(struct media_link *link, u32 flags, unsigned int notification)

    Link management notification callback

    :param struct media_link \*link:
        The link

    :param u32 flags:
        New link flags that will be applied

    :param unsigned int notification:
        The link's state change notification type (MEDIA_DEV_NOTIFY\_\*)

.. _`v4l2_pipeline_link_notify.description`:

Description
-----------

React to link management on powered pipelines by updating the use count of
all entities in the source and sink sides of the link. Entities are powered
on or off accordingly. The use of this function should be paired
with \ :c:func:`v4l2_pipeline_pm_use`\ .

Return 0 on success or a negative error code on failure. Powering entities
off is assumed to never fail. This function will not fail for disconnection
events.

.. This file was automatic generated / don't edit.

