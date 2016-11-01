.. -*- coding: utf-8; mode: rst -*-
.. src-file: include/media/v4l2-subdev.h

.. _`v4l2_decode_vbi_line`:

struct v4l2_decode_vbi_line
===========================

.. c:type:: struct v4l2_decode_vbi_line

    used to decode_vbi_line

.. _`v4l2_decode_vbi_line.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_decode_vbi_line {
        u32 is_second_field;
        u8 *p;
        u32 line;
        u32 type;
    }

.. _`v4l2_decode_vbi_line.members`:

Members
-------

is_second_field
    Set to 0 for the first (odd) field;
    set to 1 for the second (even) field.

p
    Pointer to the sliced VBI data from the decoder. On exit, points to
    the start of the payload.

line
    Line number of the sliced VBI data (1-23)

type
    VBI service type (V4L2_SLICED_*). 0 if no service found

.. _`v4l2_subdev_io_pin_config`:

struct v4l2_subdev_io_pin_config
================================

.. c:type:: struct v4l2_subdev_io_pin_config

    Subdevice external IO pin configuration

.. _`v4l2_subdev_io_pin_config.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_io_pin_config {
        u32 flags;
        u8 pin;
        u8 function;
        u8 value;
        u8 strength;
    }

.. _`v4l2_subdev_io_pin_config.members`:

Members
-------

flags
    bitmask with flags for this pin's config:
    \ ``V4L2_SUBDEV_IO_PIN_DISABLE``\  - disables a pin config,
    \ ``V4L2_SUBDEV_IO_PIN_OUTPUT``\  - if pin is an output,
    \ ``V4L2_SUBDEV_IO_PIN_INPUT``\  - if pin is an input,
    \ ``V4L2_SUBDEV_IO_PIN_SET_VALUE``\  - to set the output value via \ ``value``\ 
    and \ ``V4L2_SUBDEV_IO_PIN_ACTIVE_LOW``\  - if active is 0.

pin
    Chip external IO pin to configure

function
    Internal signal pad/function to route to IO pin

value
    Initial value for pin - e.g. GPIO output value

strength
    Pin drive strength

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
        int (*log_status)(struct v4l2_subdev *sd);
        int (*s_io_pin_config)(struct v4l2_subdev *sd, size_t n,struct v4l2_subdev_io_pin_config *pincfg);
        int (*init)(struct v4l2_subdev *sd, u32 val);
        int (*load_fw)(struct v4l2_subdev *sd);
        int (*reset)(struct v4l2_subdev *sd, u32 val);
        int (*s_gpio)(struct v4l2_subdev *sd, u32 val);
        long (*ioctl)(struct v4l2_subdev *sd, unsigned int cmd, void *arg);
    #ifdef CONFIG_COMPAT
        long (*compat_ioctl32)(struct v4l2_subdev *sd, unsigned int cmd,unsigned long arg);
    #endif
    #ifdef CONFIG_VIDEO_ADV_DEBUG
        int (*g_register)(struct v4l2_subdev *sd, struct v4l2_dbg_register *reg);
        int (*s_register)(struct v4l2_subdev *sd, const struct v4l2_dbg_register *reg);
    #endif
        int (*s_power)(struct v4l2_subdev *sd, int on);
        int (*interrupt_service_routine)(struct v4l2_subdev *sd,u32 status, bool *handled);
        int (*subscribe_event)(struct v4l2_subdev *sd, struct v4l2_fh *fh,struct v4l2_event_subscription *sub);
        int (*unsubscribe_event)(struct v4l2_subdev *sd, struct v4l2_fh *fh,struct v4l2_event_subscription *sub);
    }

.. _`v4l2_subdev_core_ops.members`:

Members
-------

log_status
    callback for \ ``VIDIOC_LOG_STATUS``\  ioctl handler code.

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

ioctl
    called at the end of \ :c:func:`ioctl`\  syscall handler at the V4L2 core.
    used to provide support for private ioctls used on the driver.

compat_ioctl32
    called when a 32 bits application uses a 64 bits Kernel,
    in order to fix data passed from/to userspace.

g_register
    callback for \ ``VIDIOC_G_REGISTER``\  ioctl handler code.

s_register
    callback for \ ``VIDIOC_G_REGISTER``\  ioctl handler code.

s_power
    puts subdevice in power saving mode (on == 0) or normal operation
    mode (on == 1).

interrupt_service_routine
    Called by the bridge chip's interrupt service
    handler, when an interrupt status has be raised due to this subdev,
    so that this subdev can handle the details.  It may schedule work to be
    performed later.  It must not sleep. **Called from an IRQ context**.

subscribe_event
    used by the drivers to request the control framework that
    for it to be warned when the value of a control changes.

unsubscribe_event
    remove event subscription from the control framework.

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
        int (*s_radio)(struct v4l2_subdev *sd);
        int (*s_frequency)(struct v4l2_subdev *sd, const struct v4l2_frequency *freq);
        int (*g_frequency)(struct v4l2_subdev *sd, struct v4l2_frequency *freq);
        int (*enum_freq_bands)(struct v4l2_subdev *sd, struct v4l2_frequency_band *band);
        int (*g_tuner)(struct v4l2_subdev *sd, struct v4l2_tuner *vt);
        int (*s_tuner)(struct v4l2_subdev *sd, const struct v4l2_tuner *vt);
        int (*g_modulator)(struct v4l2_subdev *sd, struct v4l2_modulator *vm);
        int (*s_modulator)(struct v4l2_subdev *sd, const struct v4l2_modulator *vm);
        int (*s_type_addr)(struct v4l2_subdev *sd, struct tuner_setup *type);
        int (*s_config)(struct v4l2_subdev *sd, const struct v4l2_priv_tun_config *config);
    }

.. _`v4l2_subdev_tuner_ops.members`:

Members
-------

s_radio
    callback for \ ``VIDIOC_S_RADIO``\  ioctl handler code.

s_frequency
    callback for \ ``VIDIOC_S_FREQUENCY``\  ioctl handler code.

g_frequency
    callback for \ ``VIDIOC_G_FREQUENCY``\  ioctl handler code.
    freq->type must be filled in. Normally done by \ :c:func:`video_ioctl2`\ 
    or the bridge driver.

enum_freq_bands
    callback for \ ``VIDIOC_ENUM_FREQ_BANDS``\  ioctl handler code.

g_tuner
    callback for \ ``VIDIOC_G_TUNER``\  ioctl handler code.

s_tuner
    callback for \ ``VIDIOC_S_TUNER``\  ioctl handler code. \ ``vt``\ ->type must be
    filled in. Normally done by video_ioctl2 or the
    bridge driver.

g_modulator
    callback for \ ``VIDIOC_G_MODULATOR``\  ioctl handler code.

s_modulator
    callback for \ ``VIDIOC_S_MODULATOR``\  ioctl handler code.

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
        int (*s_clock_freq)(struct v4l2_subdev *sd, u32 freq);
        int (*s_i2s_clock_freq)(struct v4l2_subdev *sd, u32 freq);
        int (*s_routing)(struct v4l2_subdev *sd, u32 input, u32 output, u32 config);
        int (*s_stream)(struct v4l2_subdev *sd, int enable);
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
    If the frequency is not supported, then \ ``-EINVAL``\  is returned.

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
    bitmask flags: \ ``V4L2_MBUS_FRAME_DESC_FL_LEN_MAX``\  and
    \ ``V4L2_MBUS_FRAME_DESC_FL_BLOB``\ .

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
        int (*s_routing)(struct v4l2_subdev *sd, u32 input, u32 output, u32 config);
        int (*s_crystal_freq)(struct v4l2_subdev *sd, u32 freq, u32 flags);
        int (*g_std)(struct v4l2_subdev *sd, v4l2_std_id *norm);
        int (*s_std)(struct v4l2_subdev *sd, v4l2_std_id norm);
        int (*s_std_output)(struct v4l2_subdev *sd, v4l2_std_id std);
        int (*g_std_output)(struct v4l2_subdev *sd, v4l2_std_id *std);
        int (*querystd)(struct v4l2_subdev *sd, v4l2_std_id *std);
        int (*g_tvnorms)(struct v4l2_subdev *sd, v4l2_std_id *std);
        int (*g_tvnorms_output)(struct v4l2_subdev *sd, v4l2_std_id *std);
        int (*g_input_status)(struct v4l2_subdev *sd, u32 *status);
        int (*s_stream)(struct v4l2_subdev *sd, int enable);
        int (*g_pixelaspect)(struct v4l2_subdev *sd, struct v4l2_fract *aspect);
        int (*g_parm)(struct v4l2_subdev *sd, struct v4l2_streamparm *param);
        int (*s_parm)(struct v4l2_subdev *sd, struct v4l2_streamparm *param);
        int (*g_frame_interval)(struct v4l2_subdev *sd,struct v4l2_subdev_frame_interval *interval);
        int (*s_frame_interval)(struct v4l2_subdev *sd,struct v4l2_subdev_frame_interval *interval);
        int (*s_dv_timings)(struct v4l2_subdev *sd,struct v4l2_dv_timings *timings);
        int (*g_dv_timings)(struct v4l2_subdev *sd,struct v4l2_dv_timings *timings);
        int (*query_dv_timings)(struct v4l2_subdev *sd,struct v4l2_dv_timings *timings);
        int (*g_mbus_config)(struct v4l2_subdev *sd,struct v4l2_mbus_config *cfg);
        int (*s_mbus_config)(struct v4l2_subdev *sd,const struct v4l2_mbus_config *cfg);
        int (*s_rx_buffer)(struct v4l2_subdev *sd, void *buf,unsigned int *size);
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
    callback for \ ``VIDIOC_G_STD``\  ioctl handler code.

s_std
    callback for \ ``VIDIOC_S_STD``\  ioctl handler code.

s_std_output
    set v4l2_std_id for video OUTPUT devices. This is ignored by
    video input devices.

g_std_output
    get current standard for video OUTPUT devices. This is ignored
    by video input devices.

querystd
    callback for \ ``VIDIOC_QUERYSTD``\  ioctl handler code.

g_tvnorms
    get \ :c:type:`struct v4l2_std_id <v4l2_std_id>`\  with all standards supported by the video
    CAPTURE device. This is ignored by video output devices.

g_tvnorms_output
    get v4l2_std_id with all standards supported by the video
    OUTPUT device. This is ignored by video capture devices.

g_input_status
    get input status. Same as the status field in the
    \ :c:type:`struct struct <struct>`\  \ :c:type:`struct v4l2_input <v4l2_input>`\ 

s_stream
    used to notify the driver that a video stream will start or has
    stopped.

g_pixelaspect
    callback to return the pixelaspect ratio.

g_parm
    callback for \ ``VIDIOC_G_PARM``\  ioctl handler code.

s_parm
    callback for \ ``VIDIOC_S_PARM``\  ioctl handler code.

g_frame_interval
    callback for \ ``VIDIOC_G_FRAMEINTERVAL``\  ioctl handler code.

s_frame_interval
    callback for \ ``VIDIOC_S_FRAMEINTERVAL``\  ioctl handler code.

s_dv_timings
    Set custom dv timings in the sub device. This is used
    when sub device is capable of setting detailed timing information
    in the hardware to generate/detect the video signal.

g_dv_timings
    Get custom dv timings in the sub device.

query_dv_timings
    callback for \ ``VIDIOC_QUERY_DV_TIMINGS``\  ioctl handler code.

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
        int (*decode_vbi_line)(struct v4l2_subdev *sd, struct v4l2_decode_vbi_line *vbi_line);
        int (*s_vbi_data)(struct v4l2_subdev *sd, const struct v4l2_sliced_vbi_data *vbi_data);
        int (*g_vbi_data)(struct v4l2_subdev *sd, struct v4l2_sliced_vbi_data *vbi_data);
        int (*g_sliced_vbi_cap)(struct v4l2_subdev *sd, struct v4l2_sliced_vbi_cap *cap);
        int (*s_raw_fmt)(struct v4l2_subdev *sd, struct v4l2_vbi_format *fmt);
        int (*g_sliced_fmt)(struct v4l2_subdev *sd, struct v4l2_sliced_vbi_format *fmt);
        int (*s_sliced_fmt)(struct v4l2_subdev *sd, struct v4l2_sliced_vbi_format *fmt);
    }

.. _`v4l2_subdev_vbi_ops.members`:

Members
-------

decode_vbi_line
    video decoders that support sliced VBI need to implement
    this ioctl. Field p of the \ :c:type:`struct v4l2_decode_vbi_line <v4l2_decode_vbi_line>`\  is set to the
    start of the VBI data that was generated by the decoder. The driver
    then parses the sliced VBI data and sets the other fields in the
    struct accordingly. The pointer p is updated to point to the start of
    the payload which can be copied verbatim into the data field of the
    \ :c:type:`struct v4l2_sliced_vbi_data <v4l2_sliced_vbi_data>`\ . If no valid VBI data was found, then the
    type field is set to 0 on return.

s_vbi_data
    used to generate VBI signals on a video signal.
    \ :c:type:`struct v4l2_sliced_vbi_data <v4l2_sliced_vbi_data>`\  is filled with the data packets that
    should be output. Note that if you set the line field to 0, then that
    VBI signal is disabled. If no valid VBI data was found, then the type
    field is set to 0 on return.

g_vbi_data
    used to obtain the sliced VBI packet from a readback register.
    Not all video decoders support this. If no data is available because
    the readback register contains invalid or erroneous data \ ``-EIO``\  is
    returned. Note that you must fill in the 'id' member and the 'field'
    member (to determine whether CC data from the first or second field
    should be obtained).

g_sliced_vbi_cap
    callback for \ ``VIDIOC_SLICED_VBI_CAP``\  ioctl handler code.

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
        int (*g_skip_top_lines)(struct v4l2_subdev *sd, u32 *lines);
        int (*g_skip_frames)(struct v4l2_subdev *sd, u32 *frames);
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

.. _`v4l2_subdev_ir_mode`:

enum v4l2_subdev_ir_mode
========================

.. c:type:: enum v4l2_subdev_ir_mode

    describes the type of IR supported

.. _`v4l2_subdev_ir_mode.definition`:

Definition
----------

.. code-block:: c

    enum v4l2_subdev_ir_mode {
        V4L2_SUBDEV_IR_MODE_PULSE_WIDTH
    };

.. _`v4l2_subdev_ir_mode.constants`:

Constants
---------

V4L2_SUBDEV_IR_MODE_PULSE_WIDTH
    IR uses struct ir_raw_event records

.. _`v4l2_subdev_ir_parameters`:

struct v4l2_subdev_ir_parameters
================================

.. c:type:: struct v4l2_subdev_ir_parameters

    Parameters for IR TX or TX

.. _`v4l2_subdev_ir_parameters.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_ir_parameters {
        unsigned int bytes_per_data_element;
        enum v4l2_subdev_ir_mode mode;
        bool enable;
        bool interrupt_enable;
        bool shutdown;
        bool modulation;
        u32 max_pulse_width;
        unsigned int carrier_freq;
        unsigned int duty_cycle;
        bool invert_level;
        bool invert_carrier_sense;
        u32 noise_filter_min_width;
        unsigned int carrier_range_lower;
        unsigned int carrier_range_upper;
        u32 resolution;
    }

.. _`v4l2_subdev_ir_parameters.members`:

Members
-------

bytes_per_data_element
    bytes per data element of data in read or
    write call.

mode
    IR mode as defined by \ :c:type:`enum v4l2_subdev_ir_mode <v4l2_subdev_ir_mode>`\ .

enable
    device is active if true

interrupt_enable
    IR interrupts are enabled if true

shutdown
    if true: set hardware to low/no power, false: normal mode

modulation
    if true, it uses carrier, if false: baseband

max_pulse_width
    maximum pulse width in ns, valid only for baseband signal

carrier_freq
    carrier frequency in Hz, valid only for modulated signal

duty_cycle
    duty cycle percentage, valid only for modulated signal

invert_level
    invert signal level

invert_carrier_sense
    Send 0/space as a carrier burst. used only in TX.

noise_filter_min_width
    min time of a valid pulse, in ns. Used only for RX.

carrier_range_lower
    Lower carrier range, in Hz, valid only for modulated
    signal. Used only for RX.

carrier_range_upper
    Upper carrier range, in Hz, valid only for modulated
    signal. Used only for RX.

resolution
    The receive resolution, in ns . Used only for RX.

.. _`v4l2_subdev_ir_ops`:

struct v4l2_subdev_ir_ops
=========================

.. c:type:: struct v4l2_subdev_ir_ops

    operations for IR subdevices

.. _`v4l2_subdev_ir_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_ir_ops {
        int (*rx_read)(struct v4l2_subdev *sd, u8 *buf, size_t count,ssize_t *num);
        int (*rx_g_parameters)(struct v4l2_subdev *sd,struct v4l2_subdev_ir_parameters *params);
        int (*rx_s_parameters)(struct v4l2_subdev *sd,struct v4l2_subdev_ir_parameters *params);
        int (*tx_write)(struct v4l2_subdev *sd, u8 *buf, size_t count,ssize_t *num);
        int (*tx_g_parameters)(struct v4l2_subdev *sd,struct v4l2_subdev_ir_parameters *params);
        int (*tx_s_parameters)(struct v4l2_subdev *sd,struct v4l2_subdev_ir_parameters *params);
    }

.. _`v4l2_subdev_ir_ops.members`:

Members
-------

rx_read
    Reads received codes or pulse width data.
    The semantics are similar to a non-blocking \ :c:func:`read`\  call.

rx_g_parameters
    Get the current operating parameters and state of the
    the IR receiver.

rx_s_parameters
    Set the current operating parameters and state of the
    the IR receiver.  It is recommended to call
    [rt]x_g_parameters first to fill out the current state, and only change
    the fields that need to be changed.  Upon return, the actual device
    operating parameters and state will be returned.  Note that hardware
    limitations may prevent the actual settings from matching the requested
    settings - e.g. an actual carrier setting of 35,904 Hz when 36,000 Hz
    was requested.  An exception is when the shutdown parameter is true.
    The last used operational parameters will be returned, but the actual
    state of the hardware be different to minimize power consumption and
    processing when shutdown is true.

tx_write
    Writes codes or pulse width data for transmission.
    The semantics are similar to a non-blocking \ :c:func:`write`\  call.

tx_g_parameters
    Get the current operating parameters and state of the
    the IR transmitter.

tx_s_parameters
    Set the current operating parameters and state of the
    the IR transmitter.  It is recommended to call
    [rt]x_g_parameters first to fill out the current state, and only change
    the fields that need to be changed.  Upon return, the actual device
    operating parameters and state will be returned.  Note that hardware
    limitations may prevent the actual settings from matching the requested
    settings - e.g. an actual carrier setting of 35,904 Hz when 36,000 Hz
    was requested.  An exception is when the shutdown parameter is true.
    The last used operational parameters will be returned, but the actual
    state of the hardware be different to minimize power consumption and
    processing when shutdown is true.

.. _`v4l2_subdev_pad_config`:

struct v4l2_subdev_pad_config
=============================

.. c:type:: struct v4l2_subdev_pad_config

    Used for storing subdev pad information.

.. _`v4l2_subdev_pad_config.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_pad_config {
        struct v4l2_mbus_framefmt try_fmt;
        struct v4l2_rect try_crop;
        struct v4l2_rect try_compose;
    }

.. _`v4l2_subdev_pad_config.members`:

Members
-------

try_fmt
    pointer to \ :c:type:`struct v4l2_mbus_framefmt <v4l2_mbus_framefmt>`\ 

try_crop
    pointer to \ :c:type:`struct v4l2_rect <v4l2_rect>`\  to be used for crop

try_compose
    pointer to \ :c:type:`struct v4l2_rect <v4l2_rect>`\  to be used for compose

.. _`v4l2_subdev_pad_config.description`:

Description
-----------

This structure only needs to be passed to the pad op if the 'which' field
of the main argument is set to \ ``V4L2_SUBDEV_FORMAT_TRY``\ . For
\ ``V4L2_SUBDEV_FORMAT_ACTIVE``\  it is safe to pass \ ``NULL``\ .

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
        int (*init_cfg)(struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg);
        int (*enum_mbus_code)(struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_mbus_code_enum *code);
        int (*enum_frame_size)(struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_frame_size_enum *fse);
        int (*enum_frame_interval)(struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_frame_interval_enum *fie);
        int (*get_fmt)(struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_format *format);
        int (*set_fmt)(struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_format *format);
        int (*get_selection)(struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_selection *sel);
        int (*set_selection)(struct v4l2_subdev *sd,struct v4l2_subdev_pad_config *cfg,struct v4l2_subdev_selection *sel);
        int (*get_edid)(struct v4l2_subdev *sd, struct v4l2_edid *edid);
        int (*set_edid)(struct v4l2_subdev *sd, struct v4l2_edid *edid);
        int (*dv_timings_cap)(struct v4l2_subdev *sd,struct v4l2_dv_timings_cap *cap);
        int (*enum_dv_timings)(struct v4l2_subdev *sd,struct v4l2_enum_dv_timings *timings);
    #ifdef CONFIG_MEDIA_CONTROLLER
        int (*link_validate)(struct v4l2_subdev *sd, struct media_link *link,struct v4l2_subdev_format *source_fmt,struct v4l2_subdev_format *sink_fmt);
    #endif
        int (*get_frame_desc)(struct v4l2_subdev *sd, unsigned int pad,struct v4l2_mbus_frame_desc *fd);
        int (*set_frame_desc)(struct v4l2_subdev *sd, unsigned int pad,struct v4l2_mbus_frame_desc *fd);
    }

.. _`v4l2_subdev_pad_ops.members`:

Members
-------

init_cfg
    initialize the pad config to default values

enum_mbus_code
    callback for \ ``VIDIOC_SUBDEV_ENUM_MBUS_CODE``\  ioctl handler
    code.

enum_frame_size
    callback for \ ``VIDIOC_SUBDEV_ENUM_FRAME_SIZE``\  ioctl handler
    code.

enum_frame_interval
    callback for \ ``VIDIOC_SUBDEV_ENUM_FRAME_INTERVAL``\  ioctl
    handler code.

get_fmt
    callback for \ ``VIDIOC_SUBDEV_G_FMT``\  ioctl handler code.

set_fmt
    callback for \ ``VIDIOC_SUBDEV_S_FMT``\  ioctl handler code.

get_selection
    callback for \ ``VIDIOC_SUBDEV_G_SELECTION``\  ioctl handler code.

set_selection
    callback for \ ``VIDIOC_SUBDEV_S_SELECTION``\  ioctl handler code.

get_edid
    callback for \ ``VIDIOC_SUBDEV_G_EDID``\  ioctl handler code.

set_edid
    callback for \ ``VIDIOC_SUBDEV_S_EDID``\  ioctl handler code.

dv_timings_cap
    callback for \ ``VIDIOC_SUBDEV_DV_TIMINGS_CAP``\  ioctl handler
    code.

enum_dv_timings
    callback for \ ``VIDIOC_SUBDEV_ENUM_DV_TIMINGS``\  ioctl handler
    code.

link_validate
    used by the media controller code to check if the links
    that belongs to a pipeline can be used for stream.

get_frame_desc
    get the current low level media bus frame parameters.

set_frame_desc
    set the low level media bus frame parameters, \ ``fd``\  array
    may be adjusted by the subdev driver to device capabilities.

.. _`v4l2_subdev_ops`:

struct v4l2_subdev_ops
======================

.. c:type:: struct v4l2_subdev_ops

    Subdev operations

.. _`v4l2_subdev_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_ops {
        const struct v4l2_subdev_core_ops *core;
        const struct v4l2_subdev_tuner_ops *tuner;
        const struct v4l2_subdev_audio_ops *audio;
        const struct v4l2_subdev_video_ops *video;
        const struct v4l2_subdev_vbi_ops *vbi;
        const struct v4l2_subdev_ir_ops *ir;
        const struct v4l2_subdev_sensor_ops *sensor;
        const struct v4l2_subdev_pad_ops *pad;
    }

.. _`v4l2_subdev_ops.members`:

Members
-------

core
    pointer to \ :c:type:`struct v4l2_subdev_core_ops <v4l2_subdev_core_ops>`\ . Can be \ ``NULL``\ 

tuner
    pointer to \ :c:type:`struct v4l2_subdev_tuner_ops <v4l2_subdev_tuner_ops>`\ . Can be \ ``NULL``\ 

audio
    pointer to \ :c:type:`struct v4l2_subdev_audio_ops <v4l2_subdev_audio_ops>`\ . Can be \ ``NULL``\ 

video
    pointer to \ :c:type:`struct v4l2_subdev_video_ops <v4l2_subdev_video_ops>`\ . Can be \ ``NULL``\ 

vbi
    pointer to \ :c:type:`struct v4l2_subdev_vbi_ops <v4l2_subdev_vbi_ops>`\ . Can be \ ``NULL``\ 

ir
    pointer to \ :c:type:`struct v4l2_subdev_ir_ops <v4l2_subdev_ir_ops>`\ . Can be \ ``NULL``\ 

sensor
    pointer to \ :c:type:`struct v4l2_subdev_sensor_ops <v4l2_subdev_sensor_ops>`\ . Can be \ ``NULL``\ 

pad
    pointer to \ :c:type:`struct v4l2_subdev_pad_ops <v4l2_subdev_pad_ops>`\ . Can be \ ``NULL``\ 

.. _`v4l2_subdev_internal_ops`:

struct v4l2_subdev_internal_ops
===============================

.. c:type:: struct v4l2_subdev_internal_ops

    V4L2 subdev internal ops

.. _`v4l2_subdev_internal_ops.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_internal_ops {
        int (*registered)(struct v4l2_subdev *sd);
        void (*unregistered)(struct v4l2_subdev *sd);
        int (*open)(struct v4l2_subdev *sd, struct v4l2_subdev_fh *fh);
        int (*close)(struct v4l2_subdev *sd, struct v4l2_subdev_fh *fh);
    }

.. _`v4l2_subdev_internal_ops.members`:

Members
-------

registered
    called when this subdev is registered. When called the v4l2_dev
    field is set to the correct v4l2_device.

unregistered
    called when this subdev is unregistered. When called the
    v4l2_dev field is still set to the correct v4l2_device.

open
    called when the subdev device node is opened by an application.

close
    called when the subdev device node is closed.

.. _`v4l2_subdev_internal_ops.description`:

Description
-----------

.. note::
     Never call this from drivers, only the v4l2 framework can call
     these ops.

.. _`v4l2_subdev_platform_data`:

struct v4l2_subdev_platform_data
================================

.. c:type:: struct v4l2_subdev_platform_data

    regulators config struct

.. _`v4l2_subdev_platform_data.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_platform_data {
        struct regulator_bulk_data *regulators;
        int num_regulators;
        void *host_priv;
    }

.. _`v4l2_subdev_platform_data.members`:

Members
-------

regulators
    Optional regulators used to power on/off the subdevice

num_regulators
    Number of regululators

host_priv
    Per-subdevice data, specific for a certain video host device

.. _`v4l2_subdev`:

struct v4l2_subdev
==================

.. c:type:: struct v4l2_subdev

    describes a V4L2 sub-device

.. _`v4l2_subdev.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev {
    #if defined(CONFIG_MEDIA_CONTROLLER)
        struct media_entity entity;
    #endif
        struct list_head list;
        struct module *owner;
        bool owner_v4l2_dev;
        u32 flags;
        struct v4l2_device *v4l2_dev;
        const struct v4l2_subdev_ops *ops;
        const struct v4l2_subdev_internal_ops *internal_ops;
        struct v4l2_ctrl_handler *ctrl_handler;
        char name[V4L2_SUBDEV_NAME_SIZE];
        u32 grp_id;
        void *dev_priv;
        void *host_priv;
        struct video_device *devnode;
        struct device *dev;
        struct device_node *of_node;
        struct list_head async_list;
        struct v4l2_async_subdev *asd;
        struct v4l2_async_notifier *notifier;
        struct v4l2_subdev_platform_data *pdata;
    }

.. _`v4l2_subdev.members`:

Members
-------

entity
    pointer to \ :c:type:`struct media_entity <media_entity>`\ 

list
    List of sub-devices

owner
    The owner is the same as the driver's \ :c:type:`struct device <device>`\  owner.

owner_v4l2_dev
    true if the \ :c:type:`sd->owner <sd>`\  matches the owner of \ ``v4l2_dev``\ ->dev
    ownner. Initialized by \ :c:func:`v4l2_device_register_subdev`\ .

flags
    subdev flags. Can be:
    \ ``V4L2_SUBDEV_FL_IS_I2C``\  - Set this flag if this subdev is a i2c device;
    \ ``V4L2_SUBDEV_FL_IS_SPI``\  - Set this flag if this subdev is a spi device;
    \ ``V4L2_SUBDEV_FL_HAS_DEVNODE``\  - Set this flag if this subdev needs a
    device node;
    \ ``V4L2_SUBDEV_FL_HAS_EVENTS``\  -  Set this flag if this subdev generates
    events.

v4l2_dev
    pointer to struct \ :c:type:`struct v4l2_device <v4l2_device>`\ 

ops
    pointer to struct \ :c:type:`struct v4l2_subdev_ops <v4l2_subdev_ops>`\ 

internal_ops
    pointer to struct \ :c:type:`struct v4l2_subdev_internal_ops <v4l2_subdev_internal_ops>`\ .
    Never call these internal ops from within a driver!

ctrl_handler
    The control handler of this subdev. May be NULL.

name
    Name of the sub-device. Please notice that the name must be unique.

grp_id
    can be used to group similar subdevs. Value is driver-specific

dev_priv
    pointer to private data

host_priv
    pointer to private data used by the device where the subdev
    is attached.

devnode
    subdev device node

dev
    pointer to the physical device, if any

of_node
    The device_node of the subdev, usually the same as dev->of_node.

async_list
    Links this subdev to a global subdev_list or \ ``notifier``\ ->done
    list.

asd
    Pointer to respective \ :c:type:`struct v4l2_async_subdev <v4l2_async_subdev>`\ .

notifier
    Pointer to the managing notifier.

pdata
    common part of subdevice platform data

.. _`v4l2_subdev.description`:

Description
-----------

Each instance of a subdev driver should create this struct, either
stand-alone or embedded in a larger struct.

This structure should be initialized by \ :c:func:`v4l2_subdev_init`\  or one of
its variants: \ :c:func:`v4l2_spi_subdev_init`\ , \ :c:func:`v4l2_i2c_subdev_init`\ .

.. _`v4l2_subdev_fh`:

struct v4l2_subdev_fh
=====================

.. c:type:: struct v4l2_subdev_fh

    Used for storing subdev information per file handle

.. _`v4l2_subdev_fh.definition`:

Definition
----------

.. code-block:: c

    struct v4l2_subdev_fh {
        struct v4l2_fh vfh;
    #if defined(CONFIG_VIDEO_V4L2_SUBDEV_API)
        struct v4l2_subdev_pad_config *pad;
    #endif
    }

.. _`v4l2_subdev_fh.members`:

Members
-------

vfh
    pointer to struct v4l2_fh

pad
    pointer to v4l2_subdev_pad_config

.. _`v4l2_set_subdevdata`:

v4l2_set_subdevdata
===================

.. c:function:: void v4l2_set_subdevdata(struct v4l2_subdev *sd, void *p)

    Sets V4L2 dev private device data

    :param struct v4l2_subdev \*sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

    :param void \*p:
        pointer to the private device data to be stored.

.. _`v4l2_get_subdevdata`:

v4l2_get_subdevdata
===================

.. c:function:: void *v4l2_get_subdevdata(const struct v4l2_subdev *sd)

    Gets V4L2 dev private device data

    :param const struct v4l2_subdev \*sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

.. _`v4l2_get_subdevdata.description`:

Description
-----------

Returns the pointer to the private device data to be stored.

.. _`v4l2_set_subdev_hostdata`:

v4l2_set_subdev_hostdata
========================

.. c:function:: void v4l2_set_subdev_hostdata(struct v4l2_subdev *sd, void *p)

    Sets V4L2 dev private host data

    :param struct v4l2_subdev \*sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

    :param void \*p:
        pointer to the private data to be stored.

.. _`v4l2_get_subdev_hostdata`:

v4l2_get_subdev_hostdata
========================

.. c:function:: void *v4l2_get_subdev_hostdata(const struct v4l2_subdev *sd)

    Gets V4L2 dev private data

    :param const struct v4l2_subdev \*sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

.. _`v4l2_get_subdev_hostdata.description`:

Description
-----------

Returns the pointer to the private host data to be stored.

.. _`v4l2_subdev_link_validate_default`:

v4l2_subdev_link_validate_default
=================================

.. c:function:: int v4l2_subdev_link_validate_default(struct v4l2_subdev *sd, struct media_link *link, struct v4l2_subdev_format *source_fmt, struct v4l2_subdev_format *sink_fmt)

    validates a media link

    :param struct v4l2_subdev \*sd:
        pointer to \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\ 

    :param struct media_link \*link:
        pointer to \ :c:type:`struct media_link <media_link>`\ 

    :param struct v4l2_subdev_format \*source_fmt:
        pointer to \ :c:type:`struct v4l2_subdev_format <v4l2_subdev_format>`\ 

    :param struct v4l2_subdev_format \*sink_fmt:
        pointer to \ :c:type:`struct v4l2_subdev_format <v4l2_subdev_format>`\ 

.. _`v4l2_subdev_link_validate_default.description`:

Description
-----------

This function ensures that width, height and the media bus pixel
code are equal on both source and sink of the link.

.. _`v4l2_subdev_link_validate`:

v4l2_subdev_link_validate
=========================

.. c:function:: int v4l2_subdev_link_validate(struct media_link *link)

    validates a media link

    :param struct media_link \*link:
        pointer to \ :c:type:`struct media_link <media_link>`\ 

.. _`v4l2_subdev_link_validate.description`:

Description
-----------

This function calls the subdev's link_validate ops to validate
if a media link is valid for streaming. It also internally
calls \ :c:func:`v4l2_subdev_link_validate_default`\  to ensure that
width, height and the media bus pixel code are equal on both
source and sink of the link.

.. _`v4l2_subdev_alloc_pad_config`:

v4l2_subdev_alloc_pad_config
============================

.. c:function:: struct v4l2_subdev_pad_config *v4l2_subdev_alloc_pad_config(struct v4l2_subdev *sd)

    Allocates memory for pad config

    :param struct v4l2_subdev \*sd:
        pointer to struct v4l2_subdev

.. _`v4l2_subdev_free_pad_config`:

v4l2_subdev_free_pad_config
===========================

.. c:function:: void v4l2_subdev_free_pad_config(struct v4l2_subdev_pad_config *cfg)

    Frees memory allocated by \ :c:func:`v4l2_subdev_alloc_pad_config`\ .

    :param struct v4l2_subdev_pad_config \*cfg:
        pointer to \ :c:type:`struct v4l2_subdev_pad_config <v4l2_subdev_pad_config>`\ 

.. _`v4l2_subdev_init`:

v4l2_subdev_init
================

.. c:function:: void v4l2_subdev_init(struct v4l2_subdev *sd, const struct v4l2_subdev_ops *ops)

    initializes the sub-device struct

    :param struct v4l2_subdev \*sd:
        pointer to the \ :c:type:`struct v4l2_subdev <v4l2_subdev>`\  to be initialized

    :param const struct v4l2_subdev_ops \*ops:
        pointer to \ :c:type:`struct v4l2_subdev_ops <v4l2_subdev_ops>`\ .

.. _`v4l2_subdev_notify_event`:

v4l2_subdev_notify_event
========================

.. c:function:: void v4l2_subdev_notify_event(struct v4l2_subdev *sd, const struct v4l2_event *ev)

    Delivers event notification for subdevice

    :param struct v4l2_subdev \*sd:
        The subdev for which to deliver the event

    :param const struct v4l2_event \*ev:
        The event to deliver

.. _`v4l2_subdev_notify_event.description`:

Description
-----------

Will deliver the specified event to all userspace event listeners which are
subscribed to the v42l subdev event queue as well as to the bridge driver
using the notify callback. The notification type for the notify callback
will be \ ``V4L2_DEVICE_NOTIFY_EVENT``\ .

.. This file was automatic generated / don't edit.

