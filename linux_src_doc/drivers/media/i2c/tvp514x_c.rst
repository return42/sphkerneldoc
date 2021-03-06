.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/tvp514x.c

.. _`tvp514x_std_info`:

struct tvp514x_std_info
=======================

.. c:type:: struct tvp514x_std_info

    Structure to store standard informations

.. _`tvp514x_std_info.definition`:

Definition
----------

.. code-block:: c

    struct tvp514x_std_info {
        unsigned long width;
        unsigned long height;
        u8 video_std;
        struct v4l2_standard standard;
    }

.. _`tvp514x_std_info.members`:

Members
-------

width
    Line width in pixels

height
    Number of active lines

video_std
    Value to write in REG_VIDEO_STD register

standard
    v4l2 standard structure information

.. _`tvp514x_decoder`:

struct tvp514x_decoder
======================

.. c:type:: struct tvp514x_decoder

    TVP5146/47 decoder object

.. _`tvp514x_decoder.definition`:

Definition
----------

.. code-block:: c

    struct tvp514x_decoder {
        struct v4l2_subdev sd;
        struct v4l2_ctrl_handler hdl;
        struct tvp514x_reg tvp514x_regs[ARRAY_SIZE(tvp514x_reg_list_default)];
        const struct tvp514x_platform_data *pdata;
        int ver;
        int streaming;
        struct v4l2_pix_format pix;
        int num_fmts;
        const struct v4l2_fmtdesc *fmt_list;
        enum tvp514x_std current_std;
        int num_stds;
        const struct tvp514x_std_info *std_list;
        u32 input;
        u32 output;
        struct media_pad pad;
        struct v4l2_mbus_framefmt format;
        struct tvp514x_reg *int_seq;
    }

.. _`tvp514x_decoder.members`:

Members
-------

sd
    Subdevice Slave handle

hdl
    embedded \ :c:type:`struct v4l2_ctrl_handler <v4l2_ctrl_handler>`\ 

tvp514x_regs
    copy of hw's regs with preset values.

pdata
    Board specific

ver
    Chip version

streaming
    TVP5146/47 decoder streaming - enabled or disabled.

pix
    Current pixel format

num_fmts
    Number of formats

fmt_list
    Format list

current_std
    Current standard

num_stds
    Number of standards

std_list
    Standards list

input
    Input routing at chip level

output
    Output routing at chip level

pad
    subdev media pad associated with the decoder

format
    media bus frame format

int_seq
    driver's register init sequence

.. _`tvp514x_read_reg`:

tvp514x_read_reg
================

.. c:function:: int tvp514x_read_reg(struct v4l2_subdev *sd, u8 reg)

    Read a value from a register in an TVP5146/47.

    :param sd:
        ptr to v4l2_subdev struct
    :type sd: struct v4l2_subdev \*

    :param reg:
        TVP5146/47 register address
    :type reg: u8

.. _`tvp514x_read_reg.description`:

Description
-----------

Returns value read if successful, or non-zero (-1) otherwise.

.. _`dump_reg`:

dump_reg
========

.. c:function:: void dump_reg(struct v4l2_subdev *sd, u8 reg)

    dump the register content of TVP5146/47.

    :param sd:
        ptr to v4l2_subdev struct
    :type sd: struct v4l2_subdev \*

    :param reg:
        TVP5146/47 register address
    :type reg: u8

.. _`tvp514x_write_reg`:

tvp514x_write_reg
=================

.. c:function:: int tvp514x_write_reg(struct v4l2_subdev *sd, u8 reg, u8 val)

    Write a value to a register in TVP5146/47

    :param sd:
        ptr to v4l2_subdev struct
    :type sd: struct v4l2_subdev \*

    :param reg:
        TVP5146/47 register address
    :type reg: u8

    :param val:
        value to be written to the register
    :type val: u8

.. _`tvp514x_write_reg.description`:

Description
-----------

Write a value to a register in an TVP5146/47 decoder device.
Returns zero if successful, or non-zero otherwise.

.. _`tvp514x_write_regs`:

tvp514x_write_regs
==================

.. c:function:: int tvp514x_write_regs(struct v4l2_subdev *sd, const struct tvp514x_reg reglist)

    Initializes a list of TVP5146/47 registers

    :param sd:
        ptr to v4l2_subdev struct
    :type sd: struct v4l2_subdev \*

    :param reglist:
        list of TVP5146/47 registers and values
    :type reglist: const struct tvp514x_reg

.. _`tvp514x_write_regs.description`:

Description
-----------

Initializes a list of TVP5146/47 registers:-
if token is TOK_TERM, then entire write operation terminates
if token is TOK_DELAY, then a delay of 'val' msec is introduced
if token is TOK_SKIP, then the register write is skipped
if token is TOK_WRITE, then the register write is performed
Returns zero if successful, or non-zero otherwise.

.. _`tvp514x_query_current_std`:

tvp514x_query_current_std
=========================

.. c:function:: enum tvp514x_std tvp514x_query_current_std(struct v4l2_subdev *sd)

    Query the current standard detected by TVP5146/47

    :param sd:
        ptr to v4l2_subdev struct
    :type sd: struct v4l2_subdev \*

.. _`tvp514x_query_current_std.description`:

Description
-----------

Returns the current standard detected by TVP5146/47, STD_INVALID if there is no
standard detected.

.. _`tvp514x_configure`:

tvp514x_configure
=================

.. c:function:: int tvp514x_configure(struct v4l2_subdev *sd, struct tvp514x_decoder *decoder)

    Configure the TVP5146/47 registers

    :param sd:
        ptr to v4l2_subdev struct
    :type sd: struct v4l2_subdev \*

    :param decoder:
        ptr to tvp514x_decoder structure
    :type decoder: struct tvp514x_decoder \*

.. _`tvp514x_configure.description`:

Description
-----------

Returns zero if successful, or non-zero otherwise.

.. _`tvp514x_detect`:

tvp514x_detect
==============

.. c:function:: int tvp514x_detect(struct v4l2_subdev *sd, struct tvp514x_decoder *decoder)

    Detect if an tvp514x is present, and if so which revision.

    :param sd:
        pointer to standard V4L2 sub-device structure
    :type sd: struct v4l2_subdev \*

    :param decoder:
        pointer to tvp514x_decoder structure
    :type decoder: struct tvp514x_decoder \*

.. _`tvp514x_detect.description`:

Description
-----------

A device is considered to be detected if the chip ID (LSB and MSB)
registers match the expected values.
Any value of the rom version register is accepted.
Returns ENODEV error number if no device is detected, or zero
if a device is detected.

.. _`tvp514x_querystd`:

tvp514x_querystd
================

.. c:function:: int tvp514x_querystd(struct v4l2_subdev *sd, v4l2_std_id *std_id)

    V4L2 decoder interface handler for querystd

    :param sd:
        pointer to standard V4L2 sub-device structure
    :type sd: struct v4l2_subdev \*

    :param std_id:
        standard V4L2 std_id ioctl enum
    :type std_id: v4l2_std_id \*

.. _`tvp514x_querystd.description`:

Description
-----------

Returns the current standard detected by TVP5146/47. If no active input is
detected then \*std_id is set to 0 and the function returns 0.

.. _`tvp514x_s_std`:

tvp514x_s_std
=============

.. c:function:: int tvp514x_s_std(struct v4l2_subdev *sd, v4l2_std_id std_id)

    V4L2 decoder interface handler for s_std

    :param sd:
        pointer to standard V4L2 sub-device structure
    :type sd: struct v4l2_subdev \*

    :param std_id:
        standard V4L2 v4l2_std_id ioctl enum
    :type std_id: v4l2_std_id

.. _`tvp514x_s_std.description`:

Description
-----------

If std_id is supported, sets the requested standard. Otherwise, returns
-EINVAL

.. _`tvp514x_s_routing`:

tvp514x_s_routing
=================

.. c:function:: int tvp514x_s_routing(struct v4l2_subdev *sd, u32 input, u32 output, u32 config)

    V4L2 decoder interface handler for s_routing

    :param sd:
        pointer to standard V4L2 sub-device structure
    :type sd: struct v4l2_subdev \*

    :param input:
        input selector for routing the signal
    :type input: u32

    :param output:
        output selector for routing the signal
    :type output: u32

    :param config:
        config value. Not used
    :type config: u32

.. _`tvp514x_s_routing.description`:

Description
-----------

If index is valid, selects the requested input. Otherwise, returns -EINVAL if
the input is not supported or there is no active signal present in the
selected input.

.. _`tvp514x_s_ctrl`:

tvp514x_s_ctrl
==============

.. c:function:: int tvp514x_s_ctrl(struct v4l2_ctrl *ctrl)

    V4L2 decoder interface handler for s_ctrl

    :param ctrl:
        pointer to v4l2_ctrl structure
    :type ctrl: struct v4l2_ctrl \*

.. _`tvp514x_s_ctrl.description`:

Description
-----------

If the requested control is supported, sets the control's current
value in HW. Otherwise, returns -EINVAL if the control is not supported.

.. _`tvp514x_g_frame_interval`:

tvp514x_g_frame_interval
========================

.. c:function:: int tvp514x_g_frame_interval(struct v4l2_subdev *sd, struct v4l2_subdev_frame_interval *ival)

    V4L2 decoder interface handler

    :param sd:
        pointer to standard V4L2 sub-device structure
    :type sd: struct v4l2_subdev \*

    :param ival:
        pointer to a v4l2_subdev_frame_interval structure
    :type ival: struct v4l2_subdev_frame_interval \*

.. _`tvp514x_g_frame_interval.description`:

Description
-----------

Returns the decoder's video CAPTURE parameters.

.. _`tvp514x_s_frame_interval`:

tvp514x_s_frame_interval
========================

.. c:function:: int tvp514x_s_frame_interval(struct v4l2_subdev *sd, struct v4l2_subdev_frame_interval *ival)

    V4L2 decoder interface handler

    :param sd:
        pointer to standard V4L2 sub-device structure
    :type sd: struct v4l2_subdev \*

    :param ival:
        pointer to a v4l2_subdev_frame_interval structure
    :type ival: struct v4l2_subdev_frame_interval \*

.. _`tvp514x_s_frame_interval.description`:

Description
-----------

Configures the decoder to use the input parameters, if possible. If
not possible, returns the appropriate error code.

.. _`tvp514x_s_stream`:

tvp514x_s_stream
================

.. c:function:: int tvp514x_s_stream(struct v4l2_subdev *sd, int enable)

    V4L2 decoder i/f handler for s_stream

    :param sd:
        pointer to standard V4L2 sub-device structure
    :type sd: struct v4l2_subdev \*

    :param enable:
        streaming enable or disable
    :type enable: int

.. _`tvp514x_s_stream.description`:

Description
-----------

Sets streaming to enable or disable, if possible.

.. _`tvp514x_enum_mbus_code`:

tvp514x_enum_mbus_code
======================

.. c:function:: int tvp514x_enum_mbus_code(struct v4l2_subdev *sd, struct v4l2_subdev_pad_config *cfg, struct v4l2_subdev_mbus_code_enum *code)

    V4L2 decoder interface handler for enum_mbus_code

    :param sd:
        pointer to standard V4L2 sub-device structure
    :type sd: struct v4l2_subdev \*

    :param cfg:
        pad configuration
    :type cfg: struct v4l2_subdev_pad_config \*

    :param code:
        pointer to v4l2_subdev_mbus_code_enum structure
    :type code: struct v4l2_subdev_mbus_code_enum \*

.. _`tvp514x_enum_mbus_code.description`:

Description
-----------

Enumertaes mbus codes supported

.. _`tvp514x_get_pad_format`:

tvp514x_get_pad_format
======================

.. c:function:: int tvp514x_get_pad_format(struct v4l2_subdev *sd, struct v4l2_subdev_pad_config *cfg, struct v4l2_subdev_format *format)

    V4L2 decoder interface handler for get pad format

    :param sd:
        pointer to standard V4L2 sub-device structure
    :type sd: struct v4l2_subdev \*

    :param cfg:
        pad configuration
    :type cfg: struct v4l2_subdev_pad_config \*

    :param format:
        pointer to v4l2_subdev_format structure
    :type format: struct v4l2_subdev_format \*

.. _`tvp514x_get_pad_format.description`:

Description
-----------

Retrieves pad format which is active or tried based on requirement

.. _`tvp514x_set_pad_format`:

tvp514x_set_pad_format
======================

.. c:function:: int tvp514x_set_pad_format(struct v4l2_subdev *sd, struct v4l2_subdev_pad_config *cfg, struct v4l2_subdev_format *fmt)

    V4L2 decoder interface handler for set pad format

    :param sd:
        pointer to standard V4L2 sub-device structure
    :type sd: struct v4l2_subdev \*

    :param cfg:
        pad configuration
    :type cfg: struct v4l2_subdev_pad_config \*

    :param fmt:
        pointer to v4l2_subdev_format structure
    :type fmt: struct v4l2_subdev_format \*

.. _`tvp514x_set_pad_format.description`:

Description
-----------

Set pad format for the output pad

.. _`tvp514x_probe`:

tvp514x_probe
=============

.. c:function:: int tvp514x_probe(struct i2c_client *client, const struct i2c_device_id *id)

    decoder driver i2c probe handler

    :param client:
        i2c driver client device structure
    :type client: struct i2c_client \*

    :param id:
        i2c driver id table
    :type id: const struct i2c_device_id \*

.. _`tvp514x_probe.description`:

Description
-----------

Register decoder as an i2c client device and V4L2
device.

.. _`tvp514x_remove`:

tvp514x_remove
==============

.. c:function:: int tvp514x_remove(struct i2c_client *client)

    decoder driver i2c remove handler

    :param client:
        i2c driver client device structure
    :type client: struct i2c_client \*

.. _`tvp514x_remove.description`:

Description
-----------

Unregister decoder as an i2c client device and V4L2
device. Complement of \ :c:func:`tvp514x_probe`\ .

.. This file was automatic generated / don't edit.

