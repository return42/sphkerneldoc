.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/s3c-fb.c

.. _`s3c_fb_variant`:

struct s3c_fb_variant
=====================

.. c:type:: struct s3c_fb_variant

    fb variant information

.. _`s3c_fb_variant.definition`:

Definition
----------

.. code-block:: c

    struct s3c_fb_variant {
        unsigned int is_2443:1;
        unsigned short nr_windows;
        unsigned int vidtcon;
        unsigned short wincon;
        unsigned short winmap;
        unsigned short keycon;
        unsigned short buf_start;
        unsigned short buf_end;
        unsigned short buf_size;
        unsigned short osd;
        unsigned short osd_stride;
        unsigned short palette[S3C_FB_MAX_WIN];
        unsigned int has_prtcon:1;
        unsigned int has_shadowcon:1;
        unsigned int has_blendcon:1;
        unsigned int has_clksel:1;
        unsigned int has_fixvclk:1;
    }

.. _`s3c_fb_variant.members`:

Members
-------

is_2443
    Set if S3C2443/S3C2416 style hardware.

nr_windows
    The number of windows.

vidtcon
    The base for the VIDTCONx registers

wincon
    The base for the WINxCON registers.

winmap
    The base for the WINxMAP registers.

keycon
    The abse for the WxKEYCON registers.

buf_start
    Offset of buffer start registers.

buf_end
    Offset of buffer end registers.

buf_size
    Offset of buffer size registers.

osd
    The base for the OSD registers.

osd_stride
    *undescribed*

palette
    Address of palette memory, or 0 if none.

has_prtcon
    Set if has PRTCON register.

has_shadowcon
    Set if has SHADOWCON register.

has_blendcon
    Set if has BLENDCON register.

has_clksel
    Set if VIDCON0 register has CLKSEL bit.

has_fixvclk
    Set if VIDCON1 register has FIXVCLK bits.

.. _`s3c_fb_win_variant`:

struct s3c_fb_win_variant
=========================

.. c:type:: struct s3c_fb_win_variant


.. _`s3c_fb_win_variant.definition`:

Definition
----------

.. code-block:: c

    struct s3c_fb_win_variant {
        unsigned int has_osd_c:1;
        unsigned int has_osd_d:1;
        unsigned int has_osd_alpha:1;
        unsigned int palette_16bpp:1;
        unsigned short osd_size_off;
        unsigned short palette_sz;
        u32 valid_bpp;
    }

.. _`s3c_fb_win_variant.members`:

Members
-------

has_osd_c
    Set if has OSD C register.

has_osd_d
    Set if has OSD D register.

has_osd_alpha
    Set if can change alpha transparency for a window.

palette_16bpp
    Set if palette is 16bits wide.

osd_size_off
    If != 0, supports setting up OSD for a window; the appropriate
    register is located at the given offset from OSD_BASE.

palette_sz
    Size of palette in entries.

valid_bpp
    1 bit per BPP setting to show valid bits-per-pixel.

.. _`s3c_fb_win_variant.description`:

Description
-----------

valid_bpp bit x is set if (x+1)BPP is supported.

.. _`s3c_fb_driverdata`:

struct s3c_fb_driverdata
========================

.. c:type:: struct s3c_fb_driverdata

    per-device type driver data for init time.

.. _`s3c_fb_driverdata.definition`:

Definition
----------

.. code-block:: c

    struct s3c_fb_driverdata {
        struct s3c_fb_variant variant;
        struct s3c_fb_win_variant  *win[S3C_FB_MAX_WIN];
    }

.. _`s3c_fb_driverdata.members`:

Members
-------

variant
    The variant information for this driver.

win
    The window information for each window.

.. _`s3c_fb_palette`:

struct s3c_fb_palette
=====================

.. c:type:: struct s3c_fb_palette

    palette information

.. _`s3c_fb_palette.definition`:

Definition
----------

.. code-block:: c

    struct s3c_fb_palette {
        struct fb_bitfield r;
        struct fb_bitfield g;
        struct fb_bitfield b;
        struct fb_bitfield a;
    }

.. _`s3c_fb_palette.members`:

Members
-------

r
    Red bitfield.

g
    Green bitfield.

b
    Blue bitfield.

a
    Alpha bitfield.

.. _`s3c_fb_win`:

struct s3c_fb_win
=================

.. c:type:: struct s3c_fb_win

    per window private data for each framebuffer.

.. _`s3c_fb_win.definition`:

Definition
----------

.. code-block:: c

    struct s3c_fb_win {
        struct s3c_fb_pd_win *windata;
        struct s3c_fb *parent;
        struct fb_info *fbinfo;
        struct s3c_fb_palette palette;
        struct s3c_fb_win_variant variant;
        u32 *palette_buffer;
        u32 pseudo_palette[16];
        unsigned int index;
    }

.. _`s3c_fb_win.members`:

Members
-------

windata
    The platform data supplied for the window configuration.

parent
    The hardware that this window is part of.

fbinfo
    Pointer pack to the framebuffer info for this window.

palette
    The bitfields for changing r/g/b into a hardware palette entry.

variant
    *undescribed*

palette_buffer
    Buffer/cache to hold palette entries.

pseudo_palette
    For use in TRUECOLOUR modes for entries 0..15/

index
    The window number of this window.

.. _`s3c_fb_vsync`:

struct s3c_fb_vsync
===================

.. c:type:: struct s3c_fb_vsync

    vsync information

.. _`s3c_fb_vsync.definition`:

Definition
----------

.. code-block:: c

    struct s3c_fb_vsync {
        wait_queue_head_t wait;
        unsigned int count;
    }

.. _`s3c_fb_vsync.members`:

Members
-------

wait
    a queue for processes waiting for vsync

count
    vsync interrupt count

.. _`s3c_fb`:

struct s3c_fb
=============

.. c:type:: struct s3c_fb

    overall hardware state of the hardware

.. _`s3c_fb.definition`:

Definition
----------

.. code-block:: c

    struct s3c_fb {
        spinlock_t slock;
        struct device *dev;
        struct clk *bus_clk;
        struct clk *lcd_clk;
        void __iomem *regs;
        struct s3c_fb_variant variant;
        unsigned char enabled;
        bool output_on;
        struct s3c_fb_platdata *pdata;
        struct s3c_fb_win  *windows[S3C_FB_MAX_WIN];
        int irq_no;
        unsigned long irq_flags;
        struct s3c_fb_vsync vsync_info;
    }

.. _`s3c_fb.members`:

Members
-------

slock
    The spinlock protection for this data structure.

dev
    The device that we bound to, for printing, etc.

bus_clk
    The clk (hclk) feeding our interface and possibly pixclk.

lcd_clk
    The clk (sclk) feeding pixclk.

regs
    The mapped hardware registers.

variant
    Variant information for this hardware.

enabled
    A bitmask of enabled hardware windows.

output_on
    Flag if the physical output is enabled.

pdata
    The platform configuration data passed with the device.

windows
    The hardware windows that have been claimed.

irq_no
    IRQ line number

irq_flags
    irq flags

vsync_info
    VSYNC-related information (count, queues...)

.. _`s3c_fb_validate_win_bpp`:

s3c_fb_validate_win_bpp
=======================

.. c:function:: bool s3c_fb_validate_win_bpp(struct s3c_fb_win *win, unsigned int bpp)

    validate the bits-per-pixel for this mode.

    :param struct s3c_fb_win \*win:
        The device window.

    :param unsigned int bpp:
        The bit depth.

.. _`s3c_fb_check_var`:

s3c_fb_check_var
================

.. c:function:: int s3c_fb_check_var(struct fb_var_screeninfo *var, struct fb_info *info)

    framebuffer layer request to verify a given mode.

    :param struct fb_var_screeninfo \*var:
        The screen information to verify.

    :param struct fb_info \*info:
        The framebuffer device.

.. _`s3c_fb_check_var.description`:

Description
-----------

Framebuffer layer call to verify the given information and allow us to
update various information depending on the hardware capabilities.

.. _`s3c_fb_calc_pixclk`:

s3c_fb_calc_pixclk
==================

.. c:function:: int s3c_fb_calc_pixclk(struct s3c_fb *sfb, unsigned int pixclk)

    calculate the divider to create the pixel clock.

    :param struct s3c_fb \*sfb:
        The hardware state.

    :param unsigned int pixclk:
        *undescribed*

.. _`s3c_fb_calc_pixclk.description`:

Description
-----------

Given the specified pixel clock, work out the necessary divider to get
close to the output frequency.

.. _`s3c_fb_align_word`:

s3c_fb_align_word
=================

.. c:function:: int s3c_fb_align_word(unsigned int bpp, unsigned int pix)

    align pixel count to word boundary

    :param unsigned int bpp:
        The number of bits per pixel

    :param unsigned int pix:
        The value to be aligned.

.. _`s3c_fb_align_word.description`:

Description
-----------

Align the given pixel count so that it will start on an 32bit word
boundary.

.. _`vidosd_set_size`:

vidosd_set_size
===============

.. c:function:: void vidosd_set_size(struct s3c_fb_win *win, u32 size)

    set OSD size for a window

    :param struct s3c_fb_win \*win:
        the window to set OSD size for

    :param u32 size:
        OSD size register value

.. _`vidosd_set_alpha`:

vidosd_set_alpha
================

.. c:function:: void vidosd_set_alpha(struct s3c_fb_win *win, u32 alpha)

    set alpha transparency for a window

    :param struct s3c_fb_win \*win:
        the window to set OSD size for

    :param u32 alpha:
        alpha register value

.. _`shadow_protect_win`:

shadow_protect_win
==================

.. c:function:: void shadow_protect_win(struct s3c_fb_win *win, bool protect)

    disable updating values from shadow registers at vsync

    :param struct s3c_fb_win \*win:
        window to protect registers for

    :param bool protect:
        1 to protect (disable updates)

.. _`s3c_fb_enable`:

s3c_fb_enable
=============

.. c:function:: void s3c_fb_enable(struct s3c_fb *sfb, int enable)

    Set the state of the main LCD output

    :param struct s3c_fb \*sfb:
        The main framebuffer state.

    :param int enable:
        The state to set.

.. _`s3c_fb_set_par`:

s3c_fb_set_par
==============

.. c:function:: int s3c_fb_set_par(struct fb_info *info)

    framebuffer request to set new framebuffer state.

    :param struct fb_info \*info:
        The framebuffer to change.

.. _`s3c_fb_set_par.description`:

Description
-----------

Framebuffer layer request to set a new mode for the specified framebuffer

.. _`s3c_fb_update_palette`:

s3c_fb_update_palette
=====================

.. c:function:: void s3c_fb_update_palette(struct s3c_fb *sfb, struct s3c_fb_win *win, unsigned int reg, u32 value)

    set or schedule a palette update.

    :param struct s3c_fb \*sfb:
        The hardware information.

    :param struct s3c_fb_win \*win:
        The window being updated.

    :param unsigned int reg:
        The palette index being changed.

    :param u32 value:
        The computed palette value.

.. _`s3c_fb_update_palette.description`:

Description
-----------

Change the value of a palette register, either by directly writing to
the palette (this requires the palette RAM to be disconnected from the
hardware whilst this is in progress) or schedule the update for later.

At the moment, since we have no VSYNC interrupt support, we simply set
the palette entry directly.

.. _`s3c_fb_setcolreg`:

s3c_fb_setcolreg
================

.. c:function:: int s3c_fb_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

    framebuffer layer request to change palette.

    :param unsigned regno:
        The palette index to change.

    :param unsigned red:
        The red field for the palette data.

    :param unsigned green:
        The green field for the palette data.

    :param unsigned blue:
        The blue field for the palette data.

    :param unsigned transp:
        *undescribed*

    :param struct fb_info \*info:
        The framebuffer being changed.

.. _`s3c_fb_blank`:

s3c_fb_blank
============

.. c:function:: int s3c_fb_blank(int blank_mode, struct fb_info *info)

    blank or unblank the given window

    :param int blank_mode:
        The blank state from FB_BLANK\_\*

    :param struct fb_info \*info:
        The framebuffer to blank.

.. _`s3c_fb_blank.description`:

Description
-----------

Framebuffer layer request to change the power state.

.. _`s3c_fb_pan_display`:

s3c_fb_pan_display
==================

.. c:function:: int s3c_fb_pan_display(struct fb_var_screeninfo *var, struct fb_info *info)

    Pan the display.

    :param struct fb_var_screeninfo \*var:
        The screen information to verify.

    :param struct fb_info \*info:
        The framebuffer device.

.. _`s3c_fb_pan_display.description`:

Description
-----------

Note that the offsets can be written to the device at any time, as their
values are latched at each vsync automatically. This also means that only
the last call to this function will have any effect on next vsync, but
there is no need to sleep waiting for it to prevent tearing.

.. _`s3c_fb_enable_irq`:

s3c_fb_enable_irq
=================

.. c:function:: void s3c_fb_enable_irq(struct s3c_fb *sfb)

    enable framebuffer interrupts

    :param struct s3c_fb \*sfb:
        main hardware state

.. _`s3c_fb_disable_irq`:

s3c_fb_disable_irq
==================

.. c:function:: void s3c_fb_disable_irq(struct s3c_fb *sfb)

    disable framebuffer interrupts

    :param struct s3c_fb \*sfb:
        main hardware state

.. _`s3c_fb_wait_for_vsync`:

s3c_fb_wait_for_vsync
=====================

.. c:function:: int s3c_fb_wait_for_vsync(struct s3c_fb *sfb, u32 crtc)

    sleep until next VSYNC interrupt or timeout

    :param struct s3c_fb \*sfb:
        main hardware state

    :param u32 crtc:
        head index.

.. _`s3c_fb_missing_pixclock`:

s3c_fb_missing_pixclock
=======================

.. c:function:: void s3c_fb_missing_pixclock(struct fb_videomode *mode)

    calculates pixel clock

    :param struct fb_videomode \*mode:
        The video mode to change.

.. _`s3c_fb_missing_pixclock.description`:

Description
-----------

Calculate the pixel clock when none has been given through platform data.

.. _`s3c_fb_alloc_memory`:

s3c_fb_alloc_memory
===================

.. c:function:: int s3c_fb_alloc_memory(struct s3c_fb *sfb, struct s3c_fb_win *win)

    allocate display memory for framebuffer window

    :param struct s3c_fb \*sfb:
        The base resources for the hardware.

    :param struct s3c_fb_win \*win:
        The window to initialise memory for.

.. _`s3c_fb_alloc_memory.description`:

Description
-----------

Allocate memory for the given framebuffer.

.. _`s3c_fb_free_memory`:

s3c_fb_free_memory
==================

.. c:function:: void s3c_fb_free_memory(struct s3c_fb *sfb, struct s3c_fb_win *win)

    free the display memory for the given window

    :param struct s3c_fb \*sfb:
        The base resources for the hardware.

    :param struct s3c_fb_win \*win:
        The window to free the display memory for.

.. _`s3c_fb_free_memory.description`:

Description
-----------

Free the display memory allocated by \ :c:func:`s3c_fb_alloc_memory`\ .

.. _`s3c_fb_release_win`:

s3c_fb_release_win
==================

.. c:function:: void s3c_fb_release_win(struct s3c_fb *sfb, struct s3c_fb_win *win)

    release resources for a framebuffer window.

    :param struct s3c_fb \*sfb:
        *undescribed*

    :param struct s3c_fb_win \*win:
        The window to cleanup the resources for.

.. _`s3c_fb_release_win.description`:

Description
-----------

Release the resources that where claimed for the hardware window,
such as the framebuffer instance and any memory claimed for it.

.. _`s3c_fb_probe_win`:

s3c_fb_probe_win
================

.. c:function:: int s3c_fb_probe_win(struct s3c_fb *sfb, unsigned int win_no, struct s3c_fb_win_variant *variant, struct s3c_fb_win **res)

    register an hardware window

    :param struct s3c_fb \*sfb:
        The base resources for the hardware

    :param unsigned int win_no:
        *undescribed*

    :param struct s3c_fb_win_variant \*variant:
        The variant information for this window.

    :param struct s3c_fb_win \*\*res:
        Pointer to where to place the resultant window.

.. _`s3c_fb_probe_win.description`:

Description
-----------

Allocate and do the basic initialisation for one of the hardware's graphics
windows.

.. _`s3c_fb_set_rgb_timing`:

s3c_fb_set_rgb_timing
=====================

.. c:function:: void s3c_fb_set_rgb_timing(struct s3c_fb *sfb)

    set video timing for rgb interface.

    :param struct s3c_fb \*sfb:
        The base resources for the hardware.

.. _`s3c_fb_set_rgb_timing.description`:

Description
-----------

Set horizontal and vertical lcd rgb interface timing.

.. _`s3c_fb_clear_win`:

s3c_fb_clear_win
================

.. c:function:: void s3c_fb_clear_win(struct s3c_fb *sfb, int win)

    clear hardware window registers.

    :param struct s3c_fb \*sfb:
        The base resources for the hardware.

    :param int win:
        The window to process.

.. _`s3c_fb_clear_win.description`:

Description
-----------

Reset the specific window registers to a known state.

.. _`s3c_fb_remove`:

s3c_fb_remove
=============

.. c:function:: int s3c_fb_remove(struct platform_device *pdev)

    Cleanup on module finalisation

    :param struct platform_device \*pdev:
        The platform device we are bound to.

.. _`s3c_fb_remove.description`:

Description
-----------

Shutdown and then release all the resources that the driver allocated
on initialisation.

.. This file was automatic generated / don't edit.

