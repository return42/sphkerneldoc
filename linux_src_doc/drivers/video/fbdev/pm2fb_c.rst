.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/video/fbdev/pm2fb.c

.. _`pm2fb_set_par`:

pm2fb_set_par
=============

.. c:function:: int pm2fb_set_par(struct fb_info *info)

    Alters the hardware state.

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. _`pm2fb_set_par.description`:

Description
-----------

Using the fb_var_screeninfo in fb_info we set the resolution of the
this particular framebuffer.

.. _`pm2fb_setcolreg`:

pm2fb_setcolreg
===============

.. c:function:: int pm2fb_setcolreg(unsigned regno, unsigned red, unsigned green, unsigned blue, unsigned transp, struct fb_info *info)

    Sets a color register.

    :param regno:
        boolean, 0 copy local, 1 \ :c:func:`get_user`\  function
    :type regno: unsigned

    :param red:
        frame buffer colormap structure
    :type red: unsigned

    :param green:
        The green value which can be up to 16 bits wide
    :type green: unsigned

    :param blue:
        The blue value which can be up to 16 bits wide.
    :type blue: unsigned

    :param transp:
        If supported the alpha value which can be up to 16 bits wide.
    :type transp: unsigned

    :param info:
        frame buffer info structure
    :type info: struct fb_info \*

.. _`pm2fb_setcolreg.description`:

Description
-----------

Set a single color register. The values supplied have a 16 bit
magnitude which needs to be scaled in this function for the hardware.
Pretty much a direct lift from tdfxfb.c.

Returns negative errno on error, or zero on success.

.. _`pm2fb_pan_display`:

pm2fb_pan_display
=================

.. c:function:: int pm2fb_pan_display(struct fb_var_screeninfo *var, struct fb_info *info)

    Pans the display.

    :param var:
        frame buffer variable screen structure
    :type var: struct fb_var_screeninfo \*

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. _`pm2fb_pan_display.description`:

Description
-----------

Pan (or wrap, depending on the \`vmode' field) the display using the
\`xoffset' and \`yoffset' fields of the \`var' structure.
If the values don't fit, return -EINVAL.

Returns negative errno on error, or zero on success.

.. _`pm2fb_blank`:

pm2fb_blank
===========

.. c:function:: int pm2fb_blank(int blank_mode, struct fb_info *info)

    Blanks the display.

    :param blank_mode:
        the blank mode we want.
    :type blank_mode: int

    :param info:
        frame buffer structure that represents a single frame buffer
    :type info: struct fb_info \*

.. _`pm2fb_blank.description`:

Description
-----------

Blank the screen if blank_mode != 0, else unblank. Return 0 if
blanking succeeded, != 0 if un-/blanking failed due to e.g. a
video mode which doesn't support it. Implements VESA suspend
and powerdown modes on hardware that supports disabling hsync/vsync:
blank_mode == 2: suspend vsync
blank_mode == 3: suspend hsync
blank_mode == 4: powerdown

Returns negative errno on error, or zero on success.

.. _`pm2fb_probe`:

pm2fb_probe
===========

.. c:function:: int pm2fb_probe(struct pci_dev *pdev, const struct pci_device_id *id)

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

    :param id:
        *undescribed*
    :type id: const struct pci_device_id \*

.. _`pm2fb_probe.description`:

Description
-----------

Initialise and allocate resource for PCI device.

\ ``param``\        pdev    PCI device.
\ ``param``\        id      PCI device ID.

.. _`pm2fb_remove`:

pm2fb_remove
============

.. c:function:: void pm2fb_remove(struct pci_dev *pdev)

    :param pdev:
        *undescribed*
    :type pdev: struct pci_dev \*

.. _`pm2fb_remove.description`:

Description
-----------

Release all device resources.

\ ``param``\        pdev    PCI device to clean up.

.. _`pm2fb_setup`:

pm2fb_setup
===========

.. c:function:: int pm2fb_setup(char *options)

    :param options:
        *undescribed*
    :type options: char \*

.. _`pm2fb_setup.description`:

Description
-----------

This is, comma-separated options following \`video=pm2fb:'.

.. This file was automatic generated / don't edit.

