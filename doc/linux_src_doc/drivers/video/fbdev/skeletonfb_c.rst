.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/skeletonfb.c

.. _`xxxfb_open`:

xxxfb_open
==========

.. c:function:: int xxxfb_open(struct fb_info *info, int user)

    Optional function. Called when the framebuffer is first accessed.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param int user:
        tell us if the userland (value=1) or the console is accessing
        the framebuffer.

.. _`xxxfb_open.description`:

Description
-----------

This function is the first function called in the framebuffer api.
Usually you don't need to provide this function. The case where it
is used is to change from a text mode hardware state to a graphics
mode state.

Returns negative errno on error, or zero on success.

.. _`xxxfb_release`:

xxxfb_release
=============

.. c:function:: int xxxfb_release(struct fb_info *info, int user)

    Optional function. Called when the framebuffer device is closed.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param int user:
        tell us if the userland (value=1) or the console is accessing
        the framebuffer.

.. _`xxxfb_release.description`:

Description
-----------

Thus function is called when we close /dev/fb or the framebuffer
console system is released. Usually you don't need this function.
The case where it is usually used is to go from a graphics state
to a text mode state.

Returns negative errno on error, or zero on success.

.. _`xxxfb_check_var`:

xxxfb_check_var
===============

.. c:function:: int xxxfb_check_var(struct fb_var_screeninfo *var, struct fb_info *info)

    Optional function. Validates a var passed in.

    :param struct fb_var_screeninfo \*var:
        frame buffer variable screen structure

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. _`xxxfb_check_var.description`:

Description
-----------

Checks to see if the hardware supports the state requested by
var passed in. This function does not alter the hardware state!!!
This means the data stored in struct fb_info and struct xxx_par do
not change. This includes the var inside of struct fb_info.
Do NOT change these. This function can be called on its own if we
intent to only test a mode and not actually set it. The stuff in
modedb.c is a example of this. If the var passed in is slightly
off by what the hardware can support then we alter the var PASSED in
to what we can do.

For values that are off, this function must round them \_up\_ to the
next value that is supported by the hardware.  If the value is
greater than the highest value supported by the hardware, then this
function must return -EINVAL.

.. _`xxxfb_check_var.exception-to-the-above-rule`:

Exception to the above rule
---------------------------

Some drivers have a fixed mode, ie,
the hardware is already set at boot up, and cannot be changed.  In
this case, it is more acceptable that this function just return
a copy of the currently working var (info->var). Better is to not
implement this function, as the upper layer will do the copying
of the current var for you.

.. _`xxxfb_check_var.note`:

Note
----

This is the only function where the contents of var can be
freely adjusted after the driver has been registered. If you find
that you have code outside of this function that alters the content
of var, then you are doing something wrong.  Note also that the
contents of info->var must be left untouched at all times after
driver registration.

Returns negative errno on error, or zero on success.

.. _`xxxfb_set_par`:

xxxfb_set_par
=============

.. c:function:: int xxxfb_set_par(struct fb_info *info)

    Optional function. Alters the hardware state.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. _`xxxfb_set_par.description`:

Description
-----------

Using the fb_var_screeninfo in fb_info we set the resolution of the
this particular framebuffer. This function alters the par AND the
fb_fix_screeninfo stored in fb_info. It doesn't not alter var in
fb_info since we are using that data. This means we depend on the
data in var inside fb_info to be supported by the hardware.

This function is also used to recover/restore the hardware to a
known working state.

xxxfb_check_var is always called before xxxfb_set_par to ensure that
the contents of var is always valid.

Again if you can't change the resolution you don't need this function.

However, even if your hardware does not support mode changing,
a set_par might be needed to at least initialize the hardware to
a known working state, especially if it came back from another
process that also modifies the same hardware, such as X.

If this is the case, a combination such as the following should work:

static int xxxfb_check_var(struct fb_var_screeninfo \*var,
struct fb_info \*info)
{
\*var = info->var;
return 0;
}

static int xxxfb_set_par(struct fb_info \*info)
{
init your hardware here
}

Returns negative errno on error, or zero on success.

.. _`xxxfb_setcolreg`:

xxxfb_setcolreg
===============

.. c:function:: int xxxfb_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

    Optional function. Sets a color register.

    :param unsigned regno:
        Which register in the CLUT we are programming

    :param unsigned red:
        The red value which can be up to 16 bits wide

    :param unsigned green:
        The green value which can be up to 16 bits wide

    :param unsigned blue:
        The blue value which can be up to 16 bits wide.

    :param unsigned transp:
        If supported, the alpha value which can be up to 16 bits wide.

    :param struct fb_info \*info:
        frame buffer info structure

.. _`xxxfb_setcolreg.description`:

Description
-----------

Set a single color register. The values supplied have a 16 bit
magnitude which needs to be scaled in this function for the hardware.
Things to take into consideration are how many color registers, if
any, are supported with the current color visual. With truecolor mode
no color palettes are supported. Here a pseudo palette is created
which we store the value in pseudo_palette in struct fb_info. For
pseudocolor mode we have a limited color palette. To deal with this
we can program what color is displayed for a particular pixel value.
DirectColor is similar in that we can program each color field. If
we have a static colormap we don't need to implement this function.

Returns negative errno on error, or zero on success.

.. _`xxxfb_pan_display`:

xxxfb_pan_display
=================

.. c:function:: int xxxfb_pan_display(struct fb_var_screeninfo *var, struct fb_info *info)

    NOT a required function. Pans the display.

    :param struct fb_var_screeninfo \*var:
        frame buffer variable screen structure

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. _`xxxfb_pan_display.description`:

Description
-----------

Pan (or wrap, depending on the \`vmode' field) the display using the
\`xoffset' and \`yoffset' fields of the \`var' structure.
If the values don't fit, return -EINVAL.

Returns negative errno on error, or zero on success.

.. _`xxxfb_blank`:

xxxfb_blank
===========

.. c:function:: int xxxfb_blank(int blank_mode, struct fb_info *info)

    NOT a required function. Blanks the display.

    :param int blank_mode:
        the blank mode we want.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. _`xxxfb_blank.description`:

Description
-----------

Blank the screen if blank_mode != FB_BLANK_UNBLANK, else unblank.
Return 0 if blanking succeeded, != 0 if un-/blanking failed due to
e.g. a video mode which doesn't support it.

Implements VESA suspend and powerdown modes on hardware that supports
disabling hsync/vsync:

FB_BLANK_NORMAL = display is blanked, syncs are on.
FB_BLANK_HSYNC_SUSPEND = hsync off
FB_BLANK_VSYNC_SUSPEND = vsync off
FB_BLANK_POWERDOWN =  hsync and vsync off

If implementing this function, at least support FB_BLANK_UNBLANK.
Return !0 for any modes that are unimplemented.

.. _`xxxfb_fillrect`:

xxxfb_fillrect
==============

.. c:function:: void xxxfb_fillrect(struct fb_info *p, const struct fb_fillrect *region)

    REQUIRED function. Can use generic routines if non acclerated hardware and packed pixel based. Draws a rectangle on the screen.

    :param struct fb_info \*p:
        *undescribed*

    :param const struct fb_fillrect \*region:
        The structure representing the rectangular region we
        wish to draw to.

.. _`xxxfb_fillrect.description`:

Description
-----------

This drawing operation places/removes a retangle on the screen
depending on the rastering operation with the value of color which
is in the current color depth format.

.. _`xxxfb_copyarea`:

xxxfb_copyarea
==============

.. c:function:: void xxxfb_copyarea(struct fb_info *p, const struct fb_copyarea *area)

    REQUIRED function. Can use generic routines if non acclerated hardware and packed pixel based. Copies one area of the screen to another area.

    :param struct fb_info \*p:
        *undescribed*

    :param const struct fb_copyarea \*area:
        Structure providing the data to copy the framebuffer contents
        from one region to another.

.. _`xxxfb_copyarea.description`:

Description
-----------

This drawing operation copies a rectangular area from one area of the
screen to another area.

.. _`xxxfb_imageblit`:

xxxfb_imageblit
===============

.. c:function:: void xxxfb_imageblit(struct fb_info *p, const struct fb_image *image)

    REQUIRED function. Can use generic routines if non acclerated hardware and packed pixel based. Copies a image from system memory to the screen.

    :param struct fb_info \*p:
        *undescribed*

    :param const struct fb_image \*image:
        structure defining the image.

.. _`xxxfb_imageblit.description`:

Description
-----------

This drawing operation draws a image on the screen. It can be a
mono image (needed for font handling) or a color image (needed for
tux).

.. _`xxxfb_cursor`:

xxxfb_cursor
============

.. c:function:: int xxxfb_cursor(struct fb_info *info, struct fb_cursor *cursor)

    OPTIONAL. If your hardware lacks support for a cursor, leave this field NULL.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

    :param struct fb_cursor \*cursor:
        structure defining the cursor to draw.

.. _`xxxfb_cursor.description`:

Description
-----------

This operation is used to set or alter the properities of the
cursor.

Returns negative errno on error, or zero on success.

.. _`xxxfb_sync`:

xxxfb_sync
==========

.. c:function:: int xxxfb_sync(struct fb_info *info)

    NOT a required function. Normally the accel engine for a graphics card take a specific amount of time. Often we have to wait for the accelerator to finish its operation before we can write to the framebuffer so we can have consistent display output.

    :param struct fb_info \*info:
        frame buffer structure that represents a single frame buffer

.. _`xxxfb_sync.description`:

Description
-----------

If the driver has implemented its own hardware-based drawing function,
implementing this function is highly recommended.

.. _`xxxfb_suspend`:

xxxfb_suspend
=============

.. c:function:: int xxxfb_suspend(struct pci_dev *dev, pm_message_t msg)

    Optional but recommended function. Suspend the device.

    :param struct pci_dev \*dev:
        PCI device

    :param pm_message_t msg:
        the suspend event code.

.. _`xxxfb_suspend.description`:

Description
-----------

See Documentation/power/devices.txt for more information

.. _`xxxfb_resume`:

xxxfb_resume
============

.. c:function:: int xxxfb_resume(struct pci_dev *dev)

    Optional but recommended function. Resume the device.

    :param struct pci_dev \*dev:
        PCI device

.. _`xxxfb_resume.description`:

Description
-----------

See Documentation/power/devices.txt for more information

.. _`xxxfb_suspend`:

xxxfb_suspend
=============

.. c:function:: int xxxfb_suspend(struct platform_device *dev, pm_message_t msg)

    Optional but recommended function. Suspend the device.

    :param struct platform_device \*dev:
        platform device

    :param pm_message_t msg:
        the suspend event code.

.. _`xxxfb_suspend.description`:

Description
-----------

See Documentation/power/devices.txt for more information

.. _`xxxfb_resume`:

xxxfb_resume
============

.. c:function:: int xxxfb_resume(struct platform_dev *dev)

    Optional but recommended function. Resume the device.

    :param struct platform_dev \*dev:
        platform device

.. _`xxxfb_resume.description`:

Description
-----------

See Documentation/power/devices.txt for more information

.. This file was automatic generated / don't edit.

