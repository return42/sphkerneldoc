.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/mx3fb.c

.. _`sdc_set_window_pos`:

sdc_set_window_pos
==================

.. c:function:: int sdc_set_window_pos(struct mx3fb_data *mx3fb, enum ipu_channel channel, int16_t x_pos, int16_t y_pos)

    set window position of the respective plane.

    :param mx3fb:
        mx3fb context.
    :type mx3fb: struct mx3fb_data \*

    :param channel:
        IPU DMAC channel ID.
    :type channel: enum ipu_channel

    :param x_pos:
        X coordinate relative to the top left corner to place window at.
    :type x_pos: int16_t

    :param y_pos:
        Y coordinate relative to the top left corner to place window at.
    :type y_pos: int16_t

.. _`sdc_init_panel`:

sdc_init_panel
==============

.. c:function:: int sdc_init_panel(struct mx3fb_data *mx3fb, enum ipu_panel panel, uint32_t pixel_clk, uint16_t width, uint16_t height, uint16_t h_start_width, uint16_t h_sync_width, uint16_t h_end_width, uint16_t v_start_width, uint16_t v_sync_width, uint16_t v_end_width, struct ipu_di_signal_cfg sig)

    initialize a synchronous LCD panel.

    :param mx3fb:
        mx3fb context.
    :type mx3fb: struct mx3fb_data \*

    :param panel:
        panel type.
    :type panel: enum ipu_panel

    :param pixel_clk:
        desired pixel clock frequency in Hz.
    :type pixel_clk: uint32_t

    :param width:
        width of panel in pixels.
    :type width: uint16_t

    :param height:
        height of panel in pixels.
    :type height: uint16_t

    :param h_start_width:
        number of pixel clocks between the HSYNC signal pulse
        and the start of valid data.
    :type h_start_width: uint16_t

    :param h_sync_width:
        width of the HSYNC signal in units of pixel clocks.
    :type h_sync_width: uint16_t

    :param h_end_width:
        number of pixel clocks between the end of valid data
        and the HSYNC signal for next line.
    :type h_end_width: uint16_t

    :param v_start_width:
        number of lines between the VSYNC signal pulse and the
        start of valid data.
    :type v_start_width: uint16_t

    :param v_sync_width:
        width of the VSYNC signal in units of lines
    :type v_sync_width: uint16_t

    :param v_end_width:
        number of lines between the end of valid data and the
        VSYNC signal for next frame.
    :type v_end_width: uint16_t

    :param sig:
        bitfield of signal polarities for LCD interface.
    :type sig: struct ipu_di_signal_cfg

.. _`sdc_set_color_key`:

sdc_set_color_key
=================

.. c:function:: int sdc_set_color_key(struct mx3fb_data *mx3fb, enum ipu_channel channel, bool enable, uint32_t color_key)

    set the transparent color key for SDC graphic plane.

    :param mx3fb:
        mx3fb context.
    :type mx3fb: struct mx3fb_data \*

    :param channel:
        IPU DMAC channel ID.
    :type channel: enum ipu_channel

    :param enable:
        boolean to enable or disable color keyl.
    :type enable: bool

    :param color_key:
        24-bit RGB color to use as transparent color key.
    :type color_key: uint32_t

.. _`sdc_set_global_alpha`:

sdc_set_global_alpha
====================

.. c:function:: int sdc_set_global_alpha(struct mx3fb_data *mx3fb, bool enable, uint8_t alpha)

    set global alpha blending modes.

    :param mx3fb:
        mx3fb context.
    :type mx3fb: struct mx3fb_data \*

    :param enable:
        boolean to enable or disable global alpha blending. If disabled,
        per pixel blending is used.
    :type enable: bool

    :param alpha:
        global alpha value.
    :type alpha: uint8_t

.. _`mx3fb_set_fix`:

mx3fb_set_fix
=============

.. c:function:: int mx3fb_set_fix(struct fb_info *fbi)

    set fixed framebuffer parameters from variable settings.

    :param fbi:
        *undescribed*
    :type fbi: struct fb_info \*

.. _`mx3fb_set_par`:

mx3fb_set_par
=============

.. c:function:: int mx3fb_set_par(struct fb_info *fbi)

    set framebuffer parameters and change the operating mode.

    :param fbi:
        framebuffer information pointer.
    :type fbi: struct fb_info \*

.. _`mx3fb_check_var`:

mx3fb_check_var
===============

.. c:function:: int mx3fb_check_var(struct fb_var_screeninfo *var, struct fb_info *fbi)

    check and adjust framebuffer variable parameters.

    :param var:
        framebuffer variable parameters
    :type var: struct fb_var_screeninfo \*

    :param fbi:
        framebuffer information pointer
    :type fbi: struct fb_info \*

.. _`mx3fb_blank`:

mx3fb_blank
===========

.. c:function:: int mx3fb_blank(int blank, struct fb_info *fbi)

    blank the display.

    :param blank:
        *undescribed*
    :type blank: int

    :param fbi:
        *undescribed*
    :type fbi: struct fb_info \*

.. _`mx3fb_pan_display`:

mx3fb_pan_display
=================

.. c:function:: int mx3fb_pan_display(struct fb_var_screeninfo *var, struct fb_info *fbi)

    pan or wrap the display

    :param var:
        variable screen buffer information.
    :type var: struct fb_var_screeninfo \*

    :param fbi:
        *undescribed*
    :type fbi: struct fb_info \*

.. _`mx3fb_pan_display.description`:

Description
-----------

We look only at xoffset, yoffset and the FB_VMODE_YWRAP flag

.. _`mx3fb_map_video_memory`:

mx3fb_map_video_memory
======================

.. c:function:: int mx3fb_map_video_memory(struct fb_info *fbi, unsigned int mem_len, bool lock)

    allocates the DRAM memory for the frame buffer.

    :param fbi:
        framebuffer information pointer
    :type fbi: struct fb_info \*

    :param mem_len:
        length of mapped memory
    :type mem_len: unsigned int

    :param lock:
        do not lock during initialisation
    :type lock: bool

.. _`mx3fb_map_video_memory.description`:

Description
-----------

This buffer is remapped into a non-cached, non-buffered, memory region to
allow palette and pixel writes to occur without flushing the cache. Once this
area is remapped, all virtual memory access to the video memory should occur
at the new region.

.. _`mx3fb_unmap_video_memory`:

mx3fb_unmap_video_memory
========================

.. c:function:: int mx3fb_unmap_video_memory(struct fb_info *fbi)

    de-allocate frame buffer memory.

    :param fbi:
        framebuffer information pointer
    :type fbi: struct fb_info \*

.. _`mx3fb_init_fbinfo`:

mx3fb_init_fbinfo
=================

.. c:function:: struct fb_info *mx3fb_init_fbinfo(struct device *dev, struct fb_ops *ops)

    initialize framebuffer information object.

    :param dev:
        *undescribed*
    :type dev: struct device \*

    :param ops:
        *undescribed*
    :type ops: struct fb_ops \*

.. This file was automatic generated / don't edit.

