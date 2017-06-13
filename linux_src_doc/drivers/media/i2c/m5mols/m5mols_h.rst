.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/media/i2c/m5mols/m5mols.h

.. _`m5mols_resolution`:

struct m5mols_resolution
========================

.. c:type:: struct m5mols_resolution

    structure for the resolution

.. _`m5mols_resolution.definition`:

Definition
----------

.. code-block:: c

    struct m5mols_resolution {
        u8 reg;
        enum m5mols_restype type;
        u16 width;
        u16 height;
    }

.. _`m5mols_resolution.members`:

Members
-------

reg
    resolution preset register value

type
    resolution type according to the pixel code

width
    width of the resolution

height
    height of the resolution

.. _`m5mols_exif`:

struct m5mols_exif
==================

.. c:type:: struct m5mols_exif

    structure for the EXIF information of M-5MOLS

.. _`m5mols_exif.definition`:

Definition
----------

.. code-block:: c

    struct m5mols_exif {
        u32 exposure_time;
        u32 shutter_speed;
        u32 aperture;
        u32 brightness;
        u32 exposure_bias;
        u16 iso_speed;
        u16 flash;
        u16 sdr;
        u16 qval;
    }

.. _`m5mols_exif.members`:

Members
-------

exposure_time
    exposure time register value

shutter_speed
    speed of the shutter register value

aperture
    aperture register value

brightness
    *undescribed*

exposure_bias
    it calls also EV bias

iso_speed
    ISO register value

flash
    status register value of the flash

sdr
    status register value of the Subject Distance Range

qval
    not written exact meaning in document

.. _`m5mols_capture`:

struct m5mols_capture
=====================

.. c:type:: struct m5mols_capture

    Structure for the capture capability

.. _`m5mols_capture.definition`:

Definition
----------

.. code-block:: c

    struct m5mols_capture {
        struct m5mols_exif exif;
        unsigned int buf_size;
        u32 main;
        u32 thumb;
        u32 total;
    }

.. _`m5mols_capture.members`:

Members
-------

exif
    EXIF information

buf_size
    internal JPEG frame buffer size, in bytes

main
    size in bytes of the main image

thumb
    size in bytes of the thumb image, if it was accompanied

total
    total size in bytes of the produced image

.. _`m5mols_scenemode`:

struct m5mols_scenemode
=======================

.. c:type:: struct m5mols_scenemode

    structure for the scenemode capability

.. _`m5mols_scenemode.definition`:

Definition
----------

.. code-block:: c

    struct m5mols_scenemode {
        u8 metering;
        u8 ev_bias;
        u8 wb_mode;
        u8 wb_preset;
        u8 chroma_en;
        u8 chroma_lvl;
        u8 edge_en;
        u8 edge_lvl;
        u8 af_range;
        u8 fd_mode;
        u8 mcc;
        u8 light;
        u8 flash;
        u8 tone;
        u8 iso;
        u8 capt_mode;
        u8 wdr;
    }

.. _`m5mols_scenemode.members`:

Members
-------

metering
    metering light register value

ev_bias
    EV bias register value

wb_mode
    mode which means the WhiteBalance is Auto or Manual

wb_preset
    whitebalance preset register value in the Manual mode

chroma_en
    register value whether the Chroma capability is enabled or not

chroma_lvl
    chroma's level register value

edge_en
    register value Whether the Edge capability is enabled or not

edge_lvl
    edge's level register value

af_range
    Auto Focus's range

fd_mode
    Face Detection mode

mcc
    Multi-axis Color Conversion which means emotion color

light
    status of the Light

flash
    status of the Flash

tone
    Tone color which means Contrast

iso
    ISO register value

capt_mode
    Mode of the Image Stabilization while the camera capturing

wdr
    Wide Dynamic Range register value

.. _`m5mols_scenemode.description`:

Description
-----------

The each value according to each scenemode is recommended in the documents.

.. _`m5mols_info`:

struct m5mols_info
==================

.. c:type:: struct m5mols_info

    M-5MOLS driver data structure

.. _`m5mols_info.definition`:

Definition
----------

.. code-block:: c

    struct m5mols_info {
        const struct m5mols_platform_data *pdata;
        struct v4l2_subdev sd;
        struct media_pad pad;
        wait_queue_head_t irq_waitq;
        atomic_t irq_done;
        struct v4l2_ctrl_handler handle;
        struct {unnamed_struct};
        struct v4l2_ctrl *auto_wb;
        struct v4l2_ctrl *lock_3a;
        struct v4l2_ctrl *colorfx;
        struct v4l2_ctrl *saturation;
        struct v4l2_ctrl *zoom;
        struct v4l2_ctrl *wdr;
        struct v4l2_ctrl *stabilization;
        struct v4l2_ctrl *jpeg_quality;
        int (*set_power)(struct device *dev, int on);
        struct mutex lock;
        struct v4l2_mbus_framefmt ffmt;
        int res_type;
        struct m5mols_version ver;
        struct m5mols_capture cap;
        unsigned int isp_ready:1;
        unsigned int power:1;
        unsigned int ctrl_sync:1;
        u8 resolution;
        u8 mode;
    }

.. _`m5mols_info.members`:

Members
-------

pdata
    platform data

sd
    v4l-subdev instance

pad
    media pad

irq_waitq
    waitqueue for the capture

irq_done
    set to 1 in the interrupt handler

handle
    control handler

{unnamed_struct}
    anonymous


auto_wb
    auto white balance control

lock_3a
    3A lock control

colorfx
    color effect control

saturation
    saturation control

zoom
    zoom control

wdr
    wide dynamic range control

stabilization
    image stabilization control

jpeg_quality
    JPEG compression quality control

set_power
    optional power callback to the board code

lock
    mutex protecting the structure fields below

ffmt
    current fmt according to resolution type

res_type
    current resolution type

ver
    information of the version

cap
    the capture mode attributes

isp_ready
    1 when the ISP controller has completed booting

power
    current sensor's power status

ctrl_sync
    1 when the control handler state is restored in H/W

resolution
    register value for current resolution

mode
    register value for current operation mode

.. This file was automatic generated / don't edit.

