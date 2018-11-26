.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/staging/fbtft/fbtft-core.c

.. _`fbtft_framebuffer_alloc`:

fbtft_framebuffer_alloc
=======================

.. c:function:: struct fb_info *fbtft_framebuffer_alloc(struct fbtft_display *display, struct device *dev, struct fbtft_platform_data *pdata)

    creates a new frame buffer info structure

    :param display:
        pointer to structure describing the display
    :type display: struct fbtft_display \*

    :param dev:
        pointer to the device for this fb, this can be NULL
    :type dev: struct device \*

    :param pdata:
        *undescribed*
    :type pdata: struct fbtft_platform_data \*

.. _`fbtft_framebuffer_alloc.description`:

Description
-----------

Creates a new frame buffer info structure.

.. _`fbtft_framebuffer_alloc.also-creates-and-populates-the-following-structures`:

Also creates and populates the following structures
---------------------------------------------------

info->fbops
info->fbdefio
info->pseudo_palette
par->fbtftops
par->txbuf

Returns the new structure, or NULL if an error occurred.

.. _`fbtft_framebuffer_release`:

fbtft_framebuffer_release
=========================

.. c:function:: void fbtft_framebuffer_release(struct fb_info *info)

    frees up all memory used by the framebuffer

    :param info:
        frame buffer info structure
    :type info: struct fb_info \*

.. _`fbtft_register_framebuffer`:

fbtft_register_framebuffer
==========================

.. c:function:: int fbtft_register_framebuffer(struct fb_info *fb_info)

    registers a tft frame buffer device

    :param fb_info:
        frame buffer info structure
    :type fb_info: struct fb_info \*

.. _`fbtft_register_framebuffer.description`:

Description
-----------

Sets SPI driverdata if needed
Requests needed gpios.
Initializes display
Updates display.
Registers a frame buffer device \ ``fb_info``\ .

Returns negative errno on error, or zero for success.

.. _`fbtft_unregister_framebuffer`:

fbtft_unregister_framebuffer
============================

.. c:function:: int fbtft_unregister_framebuffer(struct fb_info *fb_info)

    releases a tft frame buffer device

    :param fb_info:
        frame buffer info structure
    :type fb_info: struct fb_info \*

.. _`fbtft_unregister_framebuffer.description`:

Description
-----------

Frees SPI driverdata if needed
Frees gpios.
Unregisters frame buffer device.

.. _`fbtft_init_display_dt`:

fbtft_init_display_dt
=====================

.. c:function:: int fbtft_init_display_dt(struct fbtft_par *par)

    Device Tree \ :c:func:`init_display`\  function

    :param par:
        Driver data
    :type par: struct fbtft_par \*

.. _`fbtft_init_display_dt.return`:

Return
------

0 if successful, negative if error

.. _`fbtft_init_display`:

fbtft_init_display
==================

.. c:function:: int fbtft_init_display(struct fbtft_par *par)

    Generic \ :c:func:`init_display`\  function

    :param par:
        Driver data
    :type par: struct fbtft_par \*

.. _`fbtft_init_display.description`:

Description
-----------

Uses par->init_sequence to do the initialization

.. _`fbtft_init_display.return`:

Return
------

0 if successful, negative if error

.. _`fbtft_verify_gpios`:

fbtft_verify_gpios
==================

.. c:function:: int fbtft_verify_gpios(struct fbtft_par *par)

    Generic \ :c:func:`verify_gpios`\  function

    :param par:
        Driver data
    :type par: struct fbtft_par \*

.. _`fbtft_verify_gpios.description`:

Description
-----------

Uses \ ``spi``\ , \ ``pdev``\  and \ ``buswidth``\  to determine which GPIOs is needed

.. _`fbtft_verify_gpios.return`:

Return
------

0 if successful, negative if error

.. _`fbtft_probe_common`:

fbtft_probe_common
==================

.. c:function:: int fbtft_probe_common(struct fbtft_display *display, struct spi_device *sdev, struct platform_device *pdev)

    Generic device \ :c:func:`probe`\  helper function

    :param display:
        Display properties
    :type display: struct fbtft_display \*

    :param sdev:
        SPI device
    :type sdev: struct spi_device \*

    :param pdev:
        Platform device
    :type pdev: struct platform_device \*

.. _`fbtft_probe_common.description`:

Description
-----------

Allocates, initializes and registers a framebuffer

Either \ ``sdev``\  or \ ``pdev``\  should be NULL

.. _`fbtft_probe_common.return`:

Return
------

0 if successful, negative if error

.. _`fbtft_remove_common`:

fbtft_remove_common
===================

.. c:function:: int fbtft_remove_common(struct device *dev, struct fb_info *info)

    Generic device \ :c:func:`remove`\  helper function

    :param dev:
        Device
    :type dev: struct device \*

    :param info:
        Framebuffer
    :type info: struct fb_info \*

.. _`fbtft_remove_common.description`:

Description
-----------

Unregisters and releases the framebuffer

.. _`fbtft_remove_common.return`:

Return
------

0 if successful, negative if error

.. This file was automatic generated / don't edit.

