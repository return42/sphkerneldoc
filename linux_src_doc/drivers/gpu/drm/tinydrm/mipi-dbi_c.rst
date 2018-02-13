.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/tinydrm/mipi-dbi.c

.. _`overview`:

overview
========

This library provides helpers for MIPI Display Bus Interface (DBI)
compatible display controllers.

Many controllers for tiny lcd displays are MIPI compliant and can use this
library. If a controller uses registers 0x2A and 0x2B to set the area to
update and uses register 0x2C to write to frame memory, it is most likely
MIPI compliant.

Only MIPI Type 1 displays are supported since a full frame memory is needed.

There are 3 MIPI DBI implementation types:

A. Motorola 6800 type parallel bus

B. Intel 8080 type parallel bus

C. SPI type with 3 options:

   1. 9-bit with the Data/Command signal as the ninth bit
   2. Same as above except it's sent as 16 bits
   3. 8-bit with the Data/Command signal as a separate D/CX pin

Currently mipi_dbi only supports Type C options 1 and 3 with
\ :c:func:`mipi_dbi_spi_init`\ .

.. _`mipi_dbi_command_read`:

mipi_dbi_command_read
=====================

.. c:function:: int mipi_dbi_command_read(struct mipi_dbi *mipi, u8 cmd, u8 *val)

    MIPI DCS read command

    :param struct mipi_dbi \*mipi:
        MIPI structure

    :param u8 cmd:
        Command

    :param u8 \*val:
        Value read

.. _`mipi_dbi_command_read.description`:

Description
-----------

Send MIPI DCS read command to the controller.

.. _`mipi_dbi_command_read.return`:

Return
------

Zero on success, negative error code on failure.

.. _`mipi_dbi_command_buf`:

mipi_dbi_command_buf
====================

.. c:function:: int mipi_dbi_command_buf(struct mipi_dbi *mipi, u8 cmd, u8 *data, size_t len)

    MIPI DCS command with parameter(s) in an array

    :param struct mipi_dbi \*mipi:
        MIPI structure

    :param u8 cmd:
        Command

    :param u8 \*data:
        Parameter buffer

    :param size_t len:
        Buffer length

.. _`mipi_dbi_command_buf.return`:

Return
------

Zero on success, negative error code on failure.

.. _`mipi_dbi_buf_copy`:

mipi_dbi_buf_copy
=================

.. c:function:: int mipi_dbi_buf_copy(void *dst, struct drm_framebuffer *fb, struct drm_clip_rect *clip, bool swap)

    Copy a framebuffer, transforming it if necessary

    :param void \*dst:
        The destination buffer

    :param struct drm_framebuffer \*fb:
        The source framebuffer

    :param struct drm_clip_rect \*clip:
        Clipping rectangle of the area to be copied

    :param bool swap:
        When true, swap MSB/LSB of 16-bit values

.. _`mipi_dbi_buf_copy.return`:

Return
------

Zero on success, negative error code on failure.

.. _`mipi_dbi_pipe_enable`:

mipi_dbi_pipe_enable
====================

.. c:function:: void mipi_dbi_pipe_enable(struct drm_simple_display_pipe *pipe, struct drm_crtc_state *crtc_state)

    MIPI DBI pipe enable helper

    :param struct drm_simple_display_pipe \*pipe:
        Display pipe

    :param struct drm_crtc_state \*crtc_state:
        CRTC state

.. _`mipi_dbi_pipe_enable.description`:

Description
-----------

This function enables backlight. Drivers can use this as their
\ :c:type:`drm_simple_display_pipe_funcs->enable <drm_simple_display_pipe_funcs>`\  callback.

.. _`mipi_dbi_pipe_disable`:

mipi_dbi_pipe_disable
=====================

.. c:function:: void mipi_dbi_pipe_disable(struct drm_simple_display_pipe *pipe)

    MIPI DBI pipe disable helper

    :param struct drm_simple_display_pipe \*pipe:
        Display pipe

.. _`mipi_dbi_pipe_disable.description`:

Description
-----------

This function disables backlight if present or if not the
display memory is blanked. Drivers can use this as their
\ :c:type:`drm_simple_display_pipe_funcs->disable <drm_simple_display_pipe_funcs>`\  callback.

.. _`mipi_dbi_init`:

mipi_dbi_init
=============

.. c:function:: int mipi_dbi_init(struct device *dev, struct mipi_dbi *mipi, const struct drm_simple_display_pipe_funcs *pipe_funcs, struct drm_driver *driver, const struct drm_display_mode *mode, unsigned int rotation)

    MIPI DBI initialization

    :param struct device \*dev:
        Parent device

    :param struct mipi_dbi \*mipi:
        &mipi_dbi structure to initialize

    :param const struct drm_simple_display_pipe_funcs \*pipe_funcs:
        Display pipe functions

    :param struct drm_driver \*driver:
        DRM driver

    :param const struct drm_display_mode \*mode:
        Display mode

    :param unsigned int rotation:
        Initial rotation in degrees Counter Clock Wise

.. _`mipi_dbi_init.description`:

Description
-----------

This function initializes a \ :c:type:`struct mipi_dbi <mipi_dbi>`\  structure and it's underlying
\ ``tinydrm_device``\ . It also sets up the display pipeline.

Supported formats: Native RGB565 and emulated XRGB8888.

Objects created by this function will be automatically freed on driver
detach (devres).

.. _`mipi_dbi_init.return`:

Return
------

Zero on success, negative error code on failure.

.. _`mipi_dbi_hw_reset`:

mipi_dbi_hw_reset
=================

.. c:function:: void mipi_dbi_hw_reset(struct mipi_dbi *mipi)

    Hardware reset of controller

    :param struct mipi_dbi \*mipi:
        MIPI DBI structure

.. _`mipi_dbi_hw_reset.description`:

Description
-----------

Reset controller if the \ :c:type:`mipi_dbi->reset <mipi_dbi>`\  gpio is set.

.. _`mipi_dbi_display_is_on`:

mipi_dbi_display_is_on
======================

.. c:function:: bool mipi_dbi_display_is_on(struct mipi_dbi *mipi)

    Check if display is on

    :param struct mipi_dbi \*mipi:
        MIPI DBI structure

.. _`mipi_dbi_display_is_on.description`:

Description
-----------

This function checks the Power Mode register (if readable) to see if
display output is turned on. This can be used to see if the bootloader
has already turned on the display avoiding flicker when the pipeline is
enabled.

.. _`mipi_dbi_display_is_on.return`:

Return
------

true if the display can be verified to be on, false otherwise.

.. _`mipi_dbi_spi_cmd_max_speed`:

mipi_dbi_spi_cmd_max_speed
==========================

.. c:function:: u32 mipi_dbi_spi_cmd_max_speed(struct spi_device *spi, size_t len)

    get the maximum SPI bus speed

    :param struct spi_device \*spi:
        SPI device

    :param size_t len:
        The transfer buffer length.

.. _`mipi_dbi_spi_cmd_max_speed.description`:

Description
-----------

Many controllers have a max speed of 10MHz, but can be pushed way beyond
that. Increase reliability by running pixel data at max speed and the rest
at 10MHz, preventing transfer glitches from messing up the init settings.

.. _`mipi_dbi_spi_init`:

mipi_dbi_spi_init
=================

.. c:function:: int mipi_dbi_spi_init(struct spi_device *spi, struct mipi_dbi *mipi, struct gpio_desc *dc)

    Initialize MIPI DBI SPI interfaced controller

    :param struct spi_device \*spi:
        SPI device

    :param struct mipi_dbi \*mipi:
        &mipi_dbi structure to initialize

    :param struct gpio_desc \*dc:
        D/C gpio (optional)

.. _`mipi_dbi_spi_init.description`:

Description
-----------

This function sets \ :c:type:`mipi_dbi->command <mipi_dbi>`\ , enables \ :c:type:`mipi->read_commands <mipi>`\  for the
usual read commands. It should be followed by a call to \ :c:func:`mipi_dbi_init`\  or
a driver-specific init.

If \ ``dc``\  is set, a Type C Option 3 interface is assumed, if not
Type C Option 1.

If the SPI master driver doesn't support the necessary bits per word,

.. _`mipi_dbi_spi_init.the-following-transformation-is-used`:

the following transformation is used
------------------------------------


- 9-bit: reorder buffer as 9x 8-bit words, padded with no-op command.
- 16-bit: if big endian send as 8-bit, if little endian swap bytes

.. _`mipi_dbi_spi_init.return`:

Return
------

Zero on success, negative error code on failure.

.. _`mipi_dbi_debugfs_init`:

mipi_dbi_debugfs_init
=====================

.. c:function:: int mipi_dbi_debugfs_init(struct drm_minor *minor)

    Create debugfs entries

    :param struct drm_minor \*minor:
        DRM minor

.. _`mipi_dbi_debugfs_init.description`:

Description
-----------

This function creates a 'command' debugfs file for sending commands to the
controller or getting the read command values.
Drivers can use this as their \ :c:type:`drm_driver->debugfs_init <drm_driver>`\  callback.

.. _`mipi_dbi_debugfs_init.return`:

Return
------

Zero on success, negative error code on failure.

.. This file was automatic generated / don't edit.

