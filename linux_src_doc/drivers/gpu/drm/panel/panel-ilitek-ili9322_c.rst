.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/panel/panel-ilitek-ili9322.c

.. _`ili9322_input`:

enum ili9322_input
==================

.. c:type:: enum ili9322_input

    the format of the incoming signal to the panel

.. _`ili9322_input.definition`:

Definition
----------

.. code-block:: c

    enum ili9322_input {
        ILI9322_INPUT_SRGB_THROUGH,
        ILI9322_INPUT_SRGB_ALIGNED,
        ILI9322_INPUT_SRGB_DUMMY_320X240,
        ILI9322_INPUT_SRGB_DUMMY_360X240,
        ILI9322_INPUT_DISABLED_1,
        ILI9322_INPUT_PRGB_THROUGH,
        ILI9322_INPUT_PRGB_ALIGNED,
        ILI9322_INPUT_YUV_640X320_YCBCR,
        ILI9322_INPUT_YUV_720X360_YCBCR,
        ILI9322_INPUT_DISABLED_2,
        ILI9322_INPUT_ITU_R_BT656_720X360_YCBCR,
        ILI9322_INPUT_ITU_R_BT656_640X320_YCBCR,
        ILI9322_INPUT_UNKNOWN
    };

.. _`ili9322_input.constants`:

Constants
---------

ILI9322_INPUT_SRGB_THROUGH
    *undescribed*

ILI9322_INPUT_SRGB_ALIGNED
    *undescribed*

ILI9322_INPUT_SRGB_DUMMY_320X240
    *undescribed*

ILI9322_INPUT_SRGB_DUMMY_360X240
    *undescribed*

ILI9322_INPUT_DISABLED_1
    *undescribed*

ILI9322_INPUT_PRGB_THROUGH
    *undescribed*

ILI9322_INPUT_PRGB_ALIGNED
    *undescribed*

ILI9322_INPUT_YUV_640X320_YCBCR
    *undescribed*

ILI9322_INPUT_YUV_720X360_YCBCR
    *undescribed*

ILI9322_INPUT_DISABLED_2
    *undescribed*

ILI9322_INPUT_ITU_R_BT656_720X360_YCBCR
    *undescribed*

ILI9322_INPUT_ITU_R_BT656_640X320_YCBCR
    *undescribed*

ILI9322_INPUT_UNKNOWN
    *undescribed*

.. _`ili9322_input.description`:

Description
-----------

The panel can be connected to various input streams and four of them can
be selected by electronic straps on the display. However it is possible
to select another mode or override the electronic default with this
setting.

.. _`ili9322_config`:

struct ili9322_config
=====================

.. c:type:: struct ili9322_config

    the system specific ILI9322 configuration

.. _`ili9322_config.definition`:

Definition
----------

.. code-block:: c

    struct ili9322_config {
        u32 width_mm;
        u32 height_mm;
        bool flip_horizontal;
        bool flip_vertical;
        enum ili9322_input input;
        u32 vreg1out_mv;
        u32 vcom_high_percent;
        u32 vcom_amplitude_percent;
        bool dclk_active_high;
        bool de_active_high;
        bool hsync_active_high;
        bool vsync_active_high;
        u8 syncmode;
        u8 gamma_corr_pos[8];
        u8 gamma_corr_neg[8];
    }

.. _`ili9322_config.members`:

Members
-------

width_mm
    physical panel width [mm]

height_mm
    physical panel height [mm]

flip_horizontal
    flip the image horizontally (right-to-left scan)
    (only in RGB and YUV modes)

flip_vertical
    flip the image vertically (down-to-up scan)
    (only in RGB and YUV modes)

input
    the input/entry type used in this system, if this is set to
    ILI9322_INPUT_UNKNOWN the driver will try to figure it out by probing
    the hardware

vreg1out_mv
    the output in microvolts for the VREGOUT1 regulator used
    to drive the physical display. Valid ranges are 3600 thru 6000 in 100
    microvolt increments. If not specified, hardware defaults will be
    used (4.5V).

vcom_high_percent
    the percentage of VREGOUT1 used for the peak
    voltage on the communications link. Valid ranges are 37 thru 100
    percent. If not specified, hardware defaults will be used (91%).

vcom_amplitude_percent
    the percentage of VREGOUT1 used for the
    peak-to-peak amplitude of the communcation signals to the physical
    display. Valid ranges are 70 thru 132 percent in increments if two
    percent. Odd percentages will be truncated. If not specified, hardware
    defaults will be used (114%).

dclk_active_high
    data/pixel clock active high, data will be clocked
    in on the rising edge of the DCLK (this is usually the case).

de_active_high
    DE (data entry) is active high

hsync_active_high
    HSYNC is active high

vsync_active_high
    VSYNC is active high

syncmode
    The synchronization mode, what sync signals are emitted.
    See the enum for details.

gamma_corr_pos
    a set of 8 nybbles describing positive
    gamma correction for voltages V1 thru V8. Valid range 0..15

gamma_corr_neg
    a set of 8 nybbles describing negative
    gamma correction for voltages V1 thru V8. Valid range 0..15

.. _`ili9322_config.description`:

Description
-----------

These adjust what grayscale voltage will be output for input data V1 = 0,
V2 = 16, V3 = 48, V4 = 96, V5 = 160, V6 = 208, V7 = 240 and V8 = 255.

.. _`ili9322_config.the-curve-is-shaped-like-this`:

The curve is shaped like this
-----------------------------


^
\|                                                        V8
\|                                                   V7
\|                                          V6
\|                               V5
\|                    V4
\|            V3
\|     V2
\| V1
+----------------------------------------------------------->
0   16     48      96         160        208      240  255

The negative and postive gamma values adjust the V1 thru V8 up/down
according to the datasheet specifications. This is a property of the
physical display connected to the display controller and may vary.
If defined, both arrays must be supplied in full. If the properties
are not supplied, hardware defaults will be used.

.. This file was automatic generated / don't edit.

