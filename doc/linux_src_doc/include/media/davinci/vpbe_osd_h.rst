.. -*- coding: utf-8; mode: rst -*-

==========
vpbe_osd.h
==========


.. _`osd_layer`:

enum osd_layer
==============

.. c:type:: osd_layer

    


.. _`osd_layer.definition`:

Definition
----------

.. code-block:: c

    enum osd_layer {
      WIN_OSD0,
      WIN_VID0,
      WIN_OSD1,
      WIN_VID1
    };


.. _`osd_layer.constants`:

Constants
---------

:``WIN_OSD0``:
    On-Screen Display Window 0

:``WIN_VID0``:
    Video Window 0

:``WIN_OSD1``:
    On-Screen Display Window 1

:``WIN_VID1``:
    Video Window 1


.. _`osd_layer.description`:

Description
-----------

An enumeration of the osd display layers.



.. _`osd_win_layer`:

enum osd_win_layer
==================

.. c:type:: osd_win_layer

    


.. _`osd_win_layer.definition`:

Definition
----------

.. code-block:: c

    enum osd_win_layer {
      OSDWIN_OSD0,
      OSDWIN_OSD1
    };


.. _`osd_win_layer.constants`:

Constants
---------

:``OSDWIN_OSD0``:
    On-Screen Display Window 0

:``OSDWIN_OSD1``:
    On-Screen Display Window 1


.. _`osd_win_layer.description`:

Description
-----------

An enumeration of the OSD Window layers.



.. _`osd_pix_format`:

enum osd_pix_format
===================

.. c:type:: osd_pix_format

    


.. _`osd_pix_format.definition`:

Definition
----------

.. code-block:: c

    enum osd_pix_format {
      PIXFMT_1BPP,
      PIXFMT_2BPP,
      PIXFMT_4BPP,
      PIXFMT_8BPP,
      PIXFMT_RGB565,
      PIXFMT_YCBCRI,
      PIXFMT_RGB888,
      PIXFMT_YCRCBI,
      PIXFMT_NV12,
      PIXFMT_OSD_ATTR
    };


.. _`osd_pix_format.constants`:

Constants
---------

:``PIXFMT_1BPP``:
    1-bit-per-pixel bitmap

:``PIXFMT_2BPP``:
    2-bits-per-pixel bitmap

:``PIXFMT_4BPP``:
    4-bits-per-pixel bitmap

:``PIXFMT_8BPP``:
    8-bits-per-pixel bitmap

:``PIXFMT_RGB565``:
    16-bits-per-pixel RGB565

:``PIXFMT_YCBCRI``:
-- undescribed --

:``PIXFMT_RGB888``:
    24-bits-per-pixel RGB888

:``PIXFMT_YCRCBI``:
-- undescribed --

:``PIXFMT_NV12``:
    YUV 4:2:0 planar

:``PIXFMT_OSD_ATTR``:
    OSD Attribute Window pixel format (4bpp)


.. _`osd_pix_format.description`:

Description
-----------

An enumeration of the DaVinci pixel formats.



.. _`osd_h_exp_ratio`:

enum osd_h_exp_ratio
====================

.. c:type:: osd_h_exp_ratio

    


.. _`osd_h_exp_ratio.definition`:

Definition
----------

.. code-block:: c

    enum osd_h_exp_ratio {
      H_EXP_OFF,
      H_EXP_9_OVER_8,
      H_EXP_3_OVER_2
    };


.. _`osd_h_exp_ratio.constants`:

Constants
---------

:``H_EXP_OFF``:
    no expansion (1/1)

:``H_EXP_9_OVER_8``:
    9/8 expansion ratio

:``H_EXP_3_OVER_2``:
    3/2 expansion ratio


.. _`osd_h_exp_ratio.description`:

Description
-----------

An enumeration of the available horizontal expansion ratios.



.. _`osd_v_exp_ratio`:

enum osd_v_exp_ratio
====================

.. c:type:: osd_v_exp_ratio

    


.. _`osd_v_exp_ratio.definition`:

Definition
----------

.. code-block:: c

    enum osd_v_exp_ratio {
      V_EXP_OFF,
      V_EXP_6_OVER_5
    };


.. _`osd_v_exp_ratio.constants`:

Constants
---------

:``V_EXP_OFF``:
    no expansion (1/1)

:``V_EXP_6_OVER_5``:
    6/5 expansion ratio


.. _`osd_v_exp_ratio.description`:

Description
-----------

An enumeration of the available vertical expansion ratios.



.. _`osd_zoom_factor`:

enum osd_zoom_factor
====================

.. c:type:: osd_zoom_factor

    


.. _`osd_zoom_factor.definition`:

Definition
----------

.. code-block:: c

    enum osd_zoom_factor {
      ZOOM_X1,
      ZOOM_X2,
      ZOOM_X4
    };


.. _`osd_zoom_factor.constants`:

Constants
---------

:``ZOOM_X1``:
    no zoom (x1)

:``ZOOM_X2``:
    x2 zoom

:``ZOOM_X4``:
    x4 zoom


.. _`osd_zoom_factor.description`:

Description
-----------

An enumeration of the available zoom factors.



.. _`osd_clut`:

enum osd_clut
=============

.. c:type:: osd_clut

    


.. _`osd_clut.definition`:

Definition
----------

.. code-block:: c

    enum osd_clut {
      ROM_CLUT,
      RAM_CLUT
    };


.. _`osd_clut.constants`:

Constants
---------

:``ROM_CLUT``:
    ROM CLUT

:``RAM_CLUT``:
    RAM CLUT


.. _`osd_clut.description`:

Description
-----------

An enumeration of the available Color Lookup Tables (CLUTs).



.. _`osd_rom_clut`:

enum osd_rom_clut
=================

.. c:type:: osd_rom_clut

    


.. _`osd_rom_clut.definition`:

Definition
----------

.. code-block:: c

    enum osd_rom_clut {
      ROM_CLUT0,
      ROM_CLUT1
    };


.. _`osd_rom_clut.constants`:

Constants
---------

:``ROM_CLUT0``:
    Macintosh CLUT

:``ROM_CLUT1``:
    CLUT from DM270 and prior devices


.. _`osd_rom_clut.description`:

Description
-----------

An enumeration of the ROM Color Lookup Table (CLUT) options.



.. _`osd_blending_factor`:

enum osd_blending_factor
========================

.. c:type:: osd_blending_factor

    


.. _`osd_blending_factor.definition`:

Definition
----------

.. code-block:: c

    enum osd_blending_factor {
      OSD_0_VID_8,
      OSD_1_VID_7,
      OSD_2_VID_6,
      OSD_3_VID_5,
      OSD_4_VID_4,
      OSD_5_VID_3,
      OSD_6_VID_2,
      OSD_8_VID_0
    };


.. _`osd_blending_factor.constants`:

Constants
---------

:``OSD_0_VID_8``:
    OSD pixels are fully transparent

:``OSD_1_VID_7``:
    OSD pixels contribute 1/8, video pixels contribute 7/8

:``OSD_2_VID_6``:
    OSD pixels contribute 2/8, video pixels contribute 6/8

:``OSD_3_VID_5``:
    OSD pixels contribute 3/8, video pixels contribute 5/8

:``OSD_4_VID_4``:
    OSD pixels contribute 4/8, video pixels contribute 4/8

:``OSD_5_VID_3``:
    OSD pixels contribute 5/8, video pixels contribute 3/8

:``OSD_6_VID_2``:
    OSD pixels contribute 6/8, video pixels contribute 2/8

:``OSD_8_VID_0``:
    OSD pixels are fully opaque


.. _`osd_blending_factor.description`:

Description
-----------

An enumeration of the DaVinci pixel blending factor options.



.. _`osd_blink_interval`:

enum osd_blink_interval
=======================

.. c:type:: osd_blink_interval

    


.. _`osd_blink_interval.definition`:

Definition
----------

.. code-block:: c

    enum osd_blink_interval {
      BLINK_X1,
      BLINK_X2,
      BLINK_X3,
      BLINK_X4
    };


.. _`osd_blink_interval.constants`:

Constants
---------

:``BLINK_X1``:
    blink interval is 1 vertical refresh cycle

:``BLINK_X2``:
    blink interval is 2 vertical refresh cycles

:``BLINK_X3``:
    blink interval is 3 vertical refresh cycles

:``BLINK_X4``:
    blink interval is 4 vertical refresh cycles


.. _`osd_blink_interval.description`:

Description
-----------

An enumeration of the DaVinci pixel blinking interval options.



.. _`osd_cursor_h_width`:

enum osd_cursor_h_width
=======================

.. c:type:: osd_cursor_h_width

    


.. _`osd_cursor_h_width.definition`:

Definition
----------

.. code-block:: c

    enum osd_cursor_h_width {
      H_WIDTH_1,
      H_WIDTH_4,
      H_WIDTH_8,
      H_WIDTH_12,
      H_WIDTH_16,
      H_WIDTH_20,
      H_WIDTH_24,
      H_WIDTH_28
    };


.. _`osd_cursor_h_width.constants`:

Constants
---------

:``H_WIDTH_1``:
    horizontal line width is 1 pixel

:``H_WIDTH_4``:
    horizontal line width is 4 pixels

:``H_WIDTH_8``:
    horizontal line width is 8 pixels

:``H_WIDTH_12``:
    horizontal line width is 12 pixels

:``H_WIDTH_16``:
    horizontal line width is 16 pixels

:``H_WIDTH_20``:
    horizontal line width is 20 pixels

:``H_WIDTH_24``:
    horizontal line width is 24 pixels

:``H_WIDTH_28``:
    horizontal line width is 28 pixels


.. _`osd_cursor_v_width`:

enum osd_cursor_v_width
=======================

.. c:type:: osd_cursor_v_width

    


.. _`osd_cursor_v_width.definition`:

Definition
----------

.. code-block:: c

    enum osd_cursor_v_width {
      V_WIDTH_1,
      V_WIDTH_2,
      V_WIDTH_4,
      V_WIDTH_6,
      V_WIDTH_8,
      V_WIDTH_10,
      V_WIDTH_12,
      V_WIDTH_14
    };


.. _`osd_cursor_v_width.constants`:

Constants
---------

:``V_WIDTH_1``:
    vertical line width is 1 line

:``V_WIDTH_2``:
    vertical line width is 2 lines

:``V_WIDTH_4``:
    vertical line width is 4 lines

:``V_WIDTH_6``:
    vertical line width is 6 lines

:``V_WIDTH_8``:
    vertical line width is 8 lines

:``V_WIDTH_10``:
    vertical line width is 10 lines

:``V_WIDTH_12``:
    vertical line width is 12 lines

:``V_WIDTH_14``:
    vertical line width is 14 lines


.. _`osd_cursor_config`:

struct osd_cursor_config
========================

.. c:type:: osd_cursor_config

    


.. _`osd_cursor_config.definition`:

Definition
----------

.. code-block:: c

  struct osd_cursor_config {
    unsigned xsize;
    unsigned ysize;
    unsigned xpos;
    unsigned ypos;
    int interlaced;
    enum osd_cursor_h_width h_width;
    enum osd_cursor_v_width v_width;
    enum osd_clut clut;
    unsigned char clut_index;
  };


.. _`osd_cursor_config.members`:

Members
-------

:``xsize``:
    horizontal size in pixels

:``ysize``:
    vertical size in lines

:``xpos``:
    horizontal offset in pixels from the left edge of the display

:``ypos``:
    vertical offset in lines from the top of the display

:``interlaced``:
    Non-zero if the display is interlaced, or zero otherwise

:``h_width``:
    horizontal line width

:``v_width``:
    vertical line width

:``clut``:
    the CLUT selector (ROM or RAM) for the cursor color

:``clut_index``:
    an index into the CLUT for the cursor color




.. _`osd_cursor_config.description`:

Description
-----------

A structure describing the configuration parameters of the hardware
rectangular cursor.



.. _`osd_layer_config`:

struct osd_layer_config
=======================

.. c:type:: osd_layer_config

    


.. _`osd_layer_config.definition`:

Definition
----------

.. code-block:: c

  struct osd_layer_config {
    enum osd_pix_format pixfmt;
    unsigned line_length;
    unsigned xsize;
    unsigned ysize;
    unsigned xpos;
    unsigned ypos;
    int interlaced;
  };


.. _`osd_layer_config.members`:

Members
-------

:``pixfmt``:
    pixel format

:``line_length``:
    offset in bytes between start of each line in memory

:``xsize``:
    number of horizontal pixels displayed per line

:``ysize``:
    number of lines displayed

:``xpos``:
    horizontal offset in pixels from the left edge of the display

:``ypos``:
    vertical offset in lines from the top of the display

:``interlaced``:
    Non-zero if the display is interlaced, or zero otherwise




.. _`osd_layer_config.description`:

Description
-----------

A structure describing the configuration parameters of an On-Screen Display
(OSD) or video layer related to how the image is stored in memory.
``line_length`` must be a multiple of the cache line size (32 bytes).

