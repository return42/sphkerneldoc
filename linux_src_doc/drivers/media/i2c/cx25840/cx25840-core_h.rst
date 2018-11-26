.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/cx25840/cx25840-core.h

.. _`cx25840_state`:

struct cx25840_state
====================

.. c:type:: struct cx25840_state

    a device instance private data

.. _`cx25840_state.definition`:

Definition
----------

.. code-block:: c

    struct cx25840_state {
        struct i2c_client *c;
        struct v4l2_subdev sd;
        struct v4l2_ctrl_handler hdl;
        struct {
            struct v4l2_ctrl *volume;
            struct v4l2_ctrl *mute;
        } ;
        int pvr150_workaround;
        int radio;
        v4l2_std_id std;
        enum cx25840_video_input vid_input;
        enum cx25840_audio_input aud_input;
        u32 audclk_freq;
        int audmode;
        int vbi_line_offset;
        enum cx25840_model id;
        u32 rev;
        int is_initialized;
        unsigned vbi_regs_offset;
        wait_queue_head_t fw_wait;
        struct work_struct fw_work;
        struct cx25840_ir_state *ir_state;
    #if defined(CONFIG_MEDIA_CONTROLLER)
        struct media_pad pads[CX25840_NUM_PADS];
    #endif
    }

.. _`cx25840_state.members`:

Members
-------

c
    i2c_client struct representing this device

sd
    our V4L2 sub-device

hdl
    our V4L2 control handler

{unnamed_struct}
    anonymous

volume
    audio volume V4L2 control (non-cx2583x devices only)

mute
    audio mute V4L2 control (non-cx2583x devices only)

pvr150_workaround
    whether we enable workaround for Hauppauge PVR150
    hardware bug (audio dropping out)

radio
    set if we are currently in the radio mode, otherwise
    the current mode is non-radio (that is, video)

std
    currently set video standard

vid_input
    currently set video input

aud_input
    currently set audio input

audclk_freq
    currently set audio sample rate

audmode
    currently set audio mode (when in non-radio mode)

vbi_line_offset
    vbi line number offset

id
    exact device model

rev
    raw device id read from the chip

is_initialized
    whether we have already loaded firmware into the chip
    and initialized it

vbi_regs_offset
    offset of vbi regs

fw_wait
    wait queue to wake an initalization function up when
    firmware loading (on a separate workqueue) finishes

fw_work
    a work that actually loads the firmware on a separate
    workqueue

ir_state
    a pointer to chip IR controller private data

pads
    array of supported chip pads (currently only a stub)

.. This file was automatic generated / don't edit.

