.. -*- coding: utf-8; mode: rst -*-

========
m5mols.h
========



.. _xref_struct_m5mols_resolution:

struct m5mols_resolution
========================

.. c:type:: struct m5mols_resolution

    structure for the resolution



Definition
----------

.. code-block:: c

  struct m5mols_resolution {
    u8 reg;
    enum m5mols_restype type;
    u16 width;
    u16 height;
  };



Members
-------

:``u8 reg``:
    resolution preset register value

:``enum m5mols_restype type``:
    resolution type according to the pixel code

:``u16 width``:
    width of the resolution

:``u16 height``:
    height of the resolution





.. _xref_struct_m5mols_exif:

struct m5mols_exif
==================

.. c:type:: struct m5mols_exif

    structure for the EXIF information of M-5MOLS



Definition
----------

.. code-block:: c

  struct m5mols_exif {
    u32 exposure_time;
    u32 shutter_speed;
    u32 aperture;
    u32 exposure_bias;
    u16 iso_speed;
    u16 flash;
    u16 sdr;
    u16 qval;
  };



Members
-------

:``u32 exposure_time``:
    exposure time register value

:``u32 shutter_speed``:
    speed of the shutter register value

:``u32 aperture``:
    aperture register value

:``u32 exposure_bias``:
    it calls also EV bias

:``u16 iso_speed``:
    ISO register value

:``u16 flash``:
    status register value of the flash

:``u16 sdr``:
    status register value of the Subject Distance Range

:``u16 qval``:
    not written exact meaning in document





.. _xref_struct_m5mols_capture:

struct m5mols_capture
=====================

.. c:type:: struct m5mols_capture

    Structure for the capture capability



Definition
----------

.. code-block:: c

  struct m5mols_capture {
    struct m5mols_exif exif;
    unsigned int buf_size;
    u32 main;
    u32 thumb;
    u32 total;
  };



Members
-------

:``struct m5mols_exif exif``:
    EXIF information

:``unsigned int buf_size``:
    internal JPEG frame buffer size, in bytes

:``u32 main``:
    size in bytes of the main image

:``u32 thumb``:
    size in bytes of the thumb image, if it was accompanied

:``u32 total``:
    total size in bytes of the produced image





.. _xref_struct_m5mols_scenemode:

struct m5mols_scenemode
=======================

.. c:type:: struct m5mols_scenemode

    structure for the scenemode capability



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
  };



Members
-------

:``u8 metering``:
    metering light register value

:``u8 ev_bias``:
    EV bias register value

:``u8 wb_mode``:
    mode which means the WhiteBalance is Auto or Manual

:``u8 wb_preset``:
    whitebalance preset register value in the Manual mode

:``u8 chroma_en``:
    register value whether the Chroma capability is enabled or not

:``u8 chroma_lvl``:
    chroma's level register value

:``u8 edge_en``:
    register value Whether the Edge capability is enabled or not

:``u8 edge_lvl``:
    edge's level register value

:``u8 af_range``:
    Auto Focus's range

:``u8 fd_mode``:
    Face Detection mode

:``u8 mcc``:
    Multi-axis Color Conversion which means emotion color

:``u8 light``:
    status of the Light

:``u8 flash``:
    status of the Flash

:``u8 tone``:
    Tone color which means Contrast

:``u8 iso``:
    ISO register value

:``u8 capt_mode``:
    Mode of the Image Stabilization while the camera capturing

:``u8 wdr``:
    Wide Dynamic Range register value




Description
-----------

The each value according to each scenemode is recommended in the documents.




.. _xref_struct_m5mols_info:

struct m5mols_info
==================

.. c:type:: struct m5mols_info

    M-5MOLS driver data structure



Definition
----------

.. code-block:: c

  struct m5mols_info {
    const struct m5mols_platform_data * pdata;
    struct v4l2_subdev sd;
    struct media_pad pad;
    wait_queue_head_t irq_waitq;
    atomic_t irq_done;
    struct v4l2_ctrl_handler handle;
    struct {unnamed_struct};
    struct v4l2_ctrl * auto_wb;
    struct v4l2_ctrl * lock_3a;
    struct v4l2_ctrl * colorfx;
    struct v4l2_ctrl * saturation;
    struct v4l2_ctrl * zoom;
    struct v4l2_ctrl * wdr;
    struct v4l2_ctrl * stabilization;
    struct v4l2_ctrl * jpeg_quality;
    int (* set_power) (struct device *dev, int on);
    struct mutex lock;
    struct v4l2_mbus_framefmt ffmt[M5MOLS_RESTYPE_MAX];
    int res_type;
    struct m5mols_version ver;
    struct m5mols_capture cap;
    unsigned int isp_ready:1;
    unsigned int power:1;
    unsigned int ctrl_sync:1;
    u8 resolution;
    u8 mode;
  };



Members
-------

:``const struct m5mols_platform_data * pdata``:
    platform data

:``struct v4l2_subdev sd``:
    v4l-subdev instance

:``struct media_pad pad``:
    media pad

:``wait_queue_head_t irq_waitq``:
    waitqueue for the capture

:``atomic_t irq_done``:
    set to 1 in the interrupt handler

:``struct v4l2_ctrl_handler handle``:
    control handler

:``struct {unnamed_struct}``:
    anonymous

:``struct v4l2_ctrl * auto_wb``:
    auto white balance control

:``struct v4l2_ctrl * lock_3a``:
    3A lock control

:``struct v4l2_ctrl * colorfx``:
    color effect control

:``struct v4l2_ctrl * saturation``:
    saturation control

:``struct v4l2_ctrl * zoom``:
    zoom control

:``struct v4l2_ctrl * wdr``:
    wide dynamic range control

:``struct v4l2_ctrl * stabilization``:
    image stabilization control

:``struct v4l2_ctrl * jpeg_quality``:
    JPEG compression quality control

:``int (*)(struct device *dev, int on) set_power``:
    optional power callback to the board code

:``struct mutex lock``:
    mutex protecting the structure fields below

:``struct v4l2_mbus_framefmt ffmt[M5MOLS_RESTYPE_MAX]``:
    current fmt according to resolution type

:``int res_type``:
    current resolution type

:``struct m5mols_version ver``:
    information of the version

:``struct m5mols_capture cap``:
    the capture mode attributes

:``unsigned int:1 isp_ready``:
    1 when the ISP controller has completed booting

:``unsigned int:1 power``:
    current sensor's power status

:``unsigned int:1 ctrl_sync``:
    1 when the control handler state is restored in H/W

:``u8 resolution``:
    register value for current resolution

:``u8 mode``:
    register value for current operation mode



