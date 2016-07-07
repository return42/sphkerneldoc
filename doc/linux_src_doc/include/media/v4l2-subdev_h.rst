.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-subdev.h

.. _`v4l2_subdev_core_ops`:

struct v4l2_subdev_core_ops
===========================

.. c:type:: struct v4l2_subdev_core_ops

    Define core ops callbacks for subdevs

.. _`v4l2_subdev_core_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_core_ops {
        int (* log_status) (struct v4l2_subdev *sd);
        int (* s_io_pin_config) (struct v4l2_subdev *sd, size_t n,struct v4l2_subdev_io_pin_config *pincfg);
        int (* init) (struct v4l2_subdev *sd, u32 val);
        int (* load_fw) (struct v4l2_subdev *sd);
        int (* reset) (struct v4l2_subdev *sd, u32 val);
        int (* s_gpio) (struct v4l2_subdev *sd, u32 val);
        int (* queryctrl) (struct v4l2_subdev *sd, struct v4l2_queryctrl *qc);
        int (* g_ctrl) (struct v4l2_subdev *sd, struct v4l2_control *ctrl);
        int (* s_ctrl) (struct v4l2_subdev *sd, struct v4l2_control *ctrl);
        int (* g_ext_ctrls) (struct v4l2_subdev *sd, struct v4l2_ext_controls *ctrls);
        int (* s_ext_ctrls) (struct v4l2_subdev *sd, struct v4l2_ext_controls *ctrls);
        int (* try_ext_ctrls) (struct v4l2_subdev *sd, struct v4l2_ext_controls *ctrls);
        int (* querymenu) (struct v4l2_subdev *sd, struct v4l2_querymenu *qm);
        long (* ioctl) (struct v4l2_subdev *sd, unsigned int cmd, void *arg);
        #ifdef CONFIG_COMPAT
        long (* compat_ioctl32) (struct v4l2_subdev *sd, unsigned int cmd,unsigned long arg);
        #endif
        #ifdef CONFIG_VIDEO_ADV_DEBUG
        int (* g_register) (struct v4l2_subdev *sd, struct v4l2_dbg_register *reg);
        int (* s_register) (struct v4l2_subdev *sd, const struct v4l2_dbg_register *reg);
        #endif
        int (* s_power) (struct v4l2_subdev *sd, int on);
        int (* interrupt_service_routine) (struct v4l2_subdev *sd,u32 status, bool *handled);
        int (* subscribe_event) (struct v4l2_subdev *sd, struct v4l2_fh *fh,struct v4l2_event_subscription *sub);
        int (* unsubscribe_event) (struct v4l2_subdev *sd, struct v4l2_fh *fh,struct v4l2_event_subscription *sub);
        int (* registered_async) (struct v4l2_subdev *sd);
    }

.. _`v4l2_subdev_core_ops.members`:

Members
-------

log_status
    callback for VIDIOC_LOG_STATUS ioctl handler code.

s_io_pin_config
    configure one or more chip I/O pins for chips that
    multiplex different internal signal pads out to IO pins.  This function
    takes a pointer to an array of 'n' pin configuration entries, one for
    each pin being configured.  This function could be called at times
    other than just subdevice initialization.

init
    initialize the sensor registers to some sort of reasonable default
    values. Do not use for new drivers and should be removed in existing
    drivers.

load_fw
    load firmware.

reset
    generic reset command. The argument selects which subsystems to
    reset. Passing 0 will always reset the whole chip. Do not use for new
    drivers without discussing this first on the linux-media mailinglist.
    There should be no reason normally to reset a device.

s_gpio
    set GPIO pins. Very simple right now, might need to be extended with
    a direction argument if needed.

queryctrl
    callback for VIDIOC_QUERYCTL ioctl handler code.

g_ctrl
    callback for VIDIOC_G_CTRL ioctl handler code.

s_ctrl
    callback for VIDIOC_S_CTRL ioctl handler code.

g_ext_ctrls
    callback for VIDIOC_G_EXT_CTRLS ioctl handler code.

s_ext_ctrls
    callback for VIDIOC_S_EXT_CTRLS ioctl handler code.

try_ext_ctrls
    callback for VIDIOC_TRY_EXT_CTRLS ioctl handler code.

querymenu
    callback for VIDIOC_QUERYMENU ioctl handler code.

ioctl
    called at the end of \ :c:func:`ioctl`\  syscall handler at the V4L2 core.
    used to provide support for private ioctls used on the driver.

compat_ioctl32
    called when a 32 bits application uses a 64 bits Kernel,
    in order to fix data passed from/to userspace.

g_register
    callback for VIDIOC_G_REGISTER ioctl handler code.

s_register
    callback for VIDIOC_G_REGISTER ioctl handler code.

s_power
    puts subdevice in power saving mode (on == 0) or normal operation
    mode (on == 1).

interrupt_service_routine
    Called by the bridge chip's interrupt service
    handler, when an interrupt status has be raised due to this subdev,
    so that this subdev can handle the details.  It may schedule work to be
    performed later.  It must not sleep.  \*Called from an IRQ context\*.

subscribe_event
    used by the drivers to request the control framework that
    for it to be warned when the value of a control changes.

unsubscribe_event
    remove event subscription from the control framework.

registered_async
    the subdevice has been registered async.

.. _`v4l2_subdev_tuner_ops`:

struct v4l2_subdev_tuner_ops
============================

.. c:type:: struct v4l2_subdev_tuner_ops

    Callbacks used when v4l device was opened in radio mode.

.. _`v4l2_subdev_tuner_ops.definition`:

Definition
----------

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
    }

.. _`v4l2_subdev_tuner_ops.members`:

Members
-------

s_radio
    callback for VIDIOC_S_RADIO ioctl handler code.

s_frequency
    callback for VIDIOC_S_FREQUENCY ioctl handler code.

g_frequency
    callback for VIDIOC_G_FREQUENCY ioctl handler code.
    freq->type must be filled in. Normally done by video_ioctl2
    or the bridge driver.

enum_freq_bands
    callback for VIDIOC_ENUM_FREQ_BANDS ioctl handler code.

g_tuner
    callback for VIDIOC_G_TUNER ioctl handler code.

s_tuner
    callback for VIDIOC_S_TUNER ioctl handler code. vt->type must be
    filled in. Normally done by video_ioctl2 or the
    bridge driver.

g_modulator
    callback for VIDIOC_G_MODULATOR ioctl handler code.

s_modulator
    callback for VIDIOC_S_MODULATOR ioctl handler code.

s_type_addr
    sets tuner type and its I2C addr.

s_config
    sets tda9887 specific stuff, like port1, port2 and qss

.. _`v4l2_subdev_audio_ops`:

struct v4l2_subdev_audio_ops
============================

.. c:type:: struct v4l2_subdev_audio_ops

    Callbacks used for audio-related settings

.. _`v4l2_subdev_audio_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_audio_ops {
        int (* s_clock_freq) (struct v4l2_subdev *sd, u32 freq);
        int (* s_i2s_clock_freq) (struct v4l2_subdev *sd, u32 freq);
        int (* s_routing) (struct v4l2_subdev *sd, u32 input, u32 output, u32 config);
        int (* s_stream) (struct v4l2_subdev *sd, int enable);
    }

.. _`v4l2_subdev_audio_ops.members`:

Members
-------

s_clock_freq
    set the frequency (in Hz) of the audio clock output.
    Used to slave an audio processor to the video decoder, ensuring that
    audio and video remain synchronized. Usual values for the frequency
    are 48000, 44100 or 32000 Hz. If the frequency is not supported, then
    -EINVAL is returned.

s_i2s_clock_freq
    sets I2S speed in bps. This is used to provide a standard
    way to select I2S clock used by driving digital audio streams at some
    board designs. Usual values for the frequency are 1024000 and 2048000.
    If the frequency is not supported, then -EINVAL is returned.

s_routing
    used to define the input and/or output pins of an audio chip,
    and any additional configuration data.
    Never attempt to use user-level input IDs (e.g. Composite, S-Video,
    Tuner) at this level. An i2c device shouldn't know about whether an
    input pin is connected to a Composite connector, become on another
    board or platform it might be connected to something else entirely.
    The calling driver is responsible for mapping a user-level input to
    the right pins on the i2c device.

s_stream
    used to notify the audio code that stream will start or has
    stopped.

.. _`v4l2_mbus_frame_desc_entry`:

struct v4l2_mbus_frame_desc_entry
=================================

.. c:type:: struct v4l2_mbus_frame_desc_entry

    media bus frame description structure

.. _`v4l2_mbus_frame_desc_entry.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_mbus_frame_desc_entry {
        u16 flags;
        u32 pixelcode;
        u32 length;
    }

.. _`v4l2_mbus_frame_desc_entry.members`:

Members
-------

flags
    V4L2_MBUS_FRAME_DESC_FL\_\* flags

pixelcode
    media bus pixel code, valid if FRAME_DESC_FL_BLOB is not set

length
    number of octets per frame, valid if V4L2_MBUS_FRAME_DESC_FL_BLOB
    is set

.. _`v4l2_mbus_frame_desc`:

struct v4l2_mbus_frame_desc
===========================

.. c:type:: struct v4l2_mbus_frame_desc

    media bus data frame description

.. _`v4l2_mbus_frame_desc.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_mbus_frame_desc {
        struct v4l2_mbus_frame_desc_entry entry[V4L2_FRAME_DESC_ENTRY_MAX];
        unsigned short num_entries;
    }

.. _`v4l2_mbus_frame_desc.members`:

Members
-------

entry
    frame descriptors array

num_entries
    number of entries in \ ``entry``\  array

.. _`v4l2_subdev_video_ops`:

struct v4l2_subdev_video_ops
============================

.. c:type:: struct v4l2_subdev_video_ops

    Callbacks used when v4l device was opened in video mode.

.. _`v4l2_subdev_video_ops.definition`:

Definition
----------

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
    }

.. _`v4l2_subdev_video_ops.members`:

Members
-------

s_routing
    see s_routing in audio_ops, except this version is for video
    devices.

s_crystal_freq
    sets the frequency of the crystal used to generate the
    clocks in Hz. An extra flags field allows device specific configuration
    regarding clock frequency dividers, etc. If not used, then set flags
    to 0. If the frequency is not supported, then -EINVAL is returned.

g_std
    callback for VIDIOC_G_STD ioctl handler code.

s_std
    callback for VIDIOC_S_STD ioctl handler code.

s_std_output
    set v4l2_std_id for video OUTPUT devices. This is ignored by
    video input devices.

g_std_output
    get current standard for video OUTPUT devices. This is ignored
    by video input devices.

querystd
    callback for VIDIOC_QUERYSTD ioctl handler code.

g_tvnorms
    get v4l2_std_id with all standards supported by the video
    CAPTURE device. This is ignored by video output devices.

g_tvnorms_output
    get v4l2_std_id with all standards supported by the video
    OUTPUT device. This is ignored by video capture devices.

g_input_status
    get input status. Same as the status field in the v4l2_input
    struct.

s_stream
    used to notify the driver that a video stream will start or has
    stopped.

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
    Set custom dv timings in the sub device. This is used
    when sub device is capable of setting detailed timing information
    in the hardware to generate/detect the video signal.

g_dv_timings
    Get custom dv timings in the sub device.

query_dv_timings
    callback for VIDIOC_QUERY_DV_TIMINGS ioctl handler code.

g_mbus_config
    get supported mediabus configurations

s_mbus_config
    set a certain mediabus configuration. This operation is added
    for compatibility with soc-camera drivers and should not be used by new
    software.

s_rx_buffer
    set a host allocated memory buffer for the subdev. The subdev
    can adjust \ ``size``\  to a lower value and must not write more data to the
    buffer starting at \ ``data``\  than the original value of \ ``size``\ .

.. _`v4l2_subdev_vbi_ops`:

struct v4l2_subdev_vbi_ops
==========================

.. c:type:: struct v4l2_subdev_vbi_ops

    Callbacks used when v4l device was opened in video mode via the vbi device node.

.. _`v4l2_subdev_vbi_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_vbi_ops {
        int (* decode_vbi_line) (struct v4l2_subdev *sd, struct v4l2_decode_vbi_line *vbi_line);
        int (* s_vbi_data) (struct v4l2_subdev *sd, const struct v4l2_sliced_vbi_data *vbi_data);
        int (* g_vbi_data) (struct v4l2_subdev *sd, struct v4l2_sliced_vbi_data *vbi_data);
        int (* g_sliced_vbi_cap) (struct v4l2_subdev *sd, struct v4l2_sliced_vbi_cap *cap);
        int (* s_raw_fmt) (struct v4l2_subdev *sd, struct v4l2_vbi_format *fmt);
        int (* g_sliced_fmt) (struct v4l2_subdev *sd, struct v4l2_sliced_vbi_format *fmt);
        int (* s_sliced_fmt) (struct v4l2_subdev *sd, struct v4l2_sliced_vbi_format *fmt);
    }

.. _`v4l2_subdev_vbi_ops.members`:

Members
-------

decode_vbi_line
    video decoders that support sliced VBI need to implement
    this ioctl. Field p of the v4l2_sliced_vbi_line struct is set to the
    start of the VBI data that was generated by the decoder. The driver
    then parses the sliced VBI data and sets the other fields in the
    struct accordingly. The pointer p is updated to point to the start of
    the payload which can be copied verbatim into the data field of the
    v4l2_sliced_vbi_data struct. If no valid VBI data was found, then the
    type field is set to 0 on return.

s_vbi_data
    used to generate VBI signals on a video signal.
    v4l2_sliced_vbi_data is filled with the data packets that should be
    output. Note that if you set the line field to 0, then that VBI signal
    is disabled. If no valid VBI data was found, then the type field is
    set to 0 on return.

g_vbi_data
    used to obtain the sliced VBI packet from a readback register.
    Not all video decoders support this. If no data is available because
    the readback register contains invalid or erroneous data -EIO is
    returned. Note that you must fill in the 'id' member and the 'field'
    member (to determine whether CC data from the first or second field
    should be obtained).

g_sliced_vbi_cap
    callback for VIDIOC_SLICED_VBI_CAP ioctl handler code.

s_raw_fmt
    setup the video encoder/decoder for raw VBI.

g_sliced_fmt
    retrieve the current sliced VBI settings.

s_sliced_fmt
    setup the sliced VBI settings.

.. _`v4l2_subdev_sensor_ops`:

struct v4l2_subdev_sensor_ops
=============================

.. c:type:: struct v4l2_subdev_sensor_ops

    v4l2-subdev sensor operations

.. _`v4l2_subdev_sensor_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_sensor_ops {
        int (* g_skip_top_lines) (struct v4l2_subdev *sd, u32 *lines);
        int (* g_skip_frames) (struct v4l2_subdev *sd, u32 *frames);
    }

.. _`v4l2_subdev_sensor_ops.members`:

Members
-------

g_skip_top_lines
    number of lines at the top of the image to be skipped.
    This is needed for some sensors, which always corrupt
    several top lines of the output image, or which send their
    metadata in them.

g_skip_frames
    number of frames to skip at stream start. This is needed for
    buggy sensors that generate faulty frames when they are
    turned on.

.. _`v4l2_subdev_pad_ops`:

struct v4l2_subdev_pad_ops
==========================

.. c:type:: struct v4l2_subdev_pad_ops

    v4l2-subdev pad level operations

.. _`v4l2_subdev_pad_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_pad_ops {
        int (* init_cfg) (struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg);
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
    }

.. _`v4l2_subdev_pad_ops.members`:

Members
-------

init_cfg
    initialize the pad config to default values

enum_mbus_code
    callback for VIDIOC_SUBDEV_ENUM_MBUS_CODE ioctl handler
    code.

enum_frame_size
    callback for VIDIOC_SUBDEV_ENUM_FRAME_SIZE ioctl handler
    code.

enum_frame_interval
    callback for VIDIOC_SUBDEV_ENUM_FRAME_INTERVAL ioctl
    handler code.

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
    callback for VIDIOC_SUBDEV_DV_TIMINGS_CAP ioctl handler
    code.

enum_dv_timings
    callback for VIDIOC_SUBDEV_ENUM_DV_TIMINGS ioctl handler
    code.

link_validate
    used by the media controller code to check if the links
    that belongs to a pipeline can be used for stream.

get_frame_desc
    get the current low level media bus frame parameters.

set_frame_desc
    set the low level media bus frame parameters, \ ``fd``\  array
    may be adjusted by the subdev driver to device capabilities.

.. This file was automatic generated / don't edit.

