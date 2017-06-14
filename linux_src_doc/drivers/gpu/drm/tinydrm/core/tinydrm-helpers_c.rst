.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/tinydrm/core/tinydrm-helpers.c

.. _`tinydrm_merge_clips`:

tinydrm_merge_clips
===================

.. c:function:: bool tinydrm_merge_clips(struct drm_clip_rect *dst, struct drm_clip_rect *src, unsigned int num_clips, unsigned int flags, u32 max_width, u32 max_height)

    Merge clip rectangles

    :param struct drm_clip_rect \*dst:
        Destination clip rectangle

    :param struct drm_clip_rect \*src:
        Source clip rectangle(s)

    :param unsigned int num_clips:
        Number of \ ``src``\  clip rectangles

    :param unsigned int flags:
        Dirty fb ioctl flags

    :param u32 max_width:
        Maximum width of \ ``dst``\ 

    :param u32 max_height:
        Maximum height of \ ``dst``\ 

.. _`tinydrm_merge_clips.description`:

Description
-----------

This function merges \ ``src``\  clip rectangle(s) into \ ``dst``\ . If \ ``src``\  is NULL,
\ ``max_width``\  and \ ``min_width``\  is used to set a full \ ``dst``\  clip rectangle.

.. _`tinydrm_merge_clips.return`:

Return
------

true if it's a full clip, false otherwise

.. _`tinydrm_memcpy`:

tinydrm_memcpy
==============

.. c:function:: void tinydrm_memcpy(void *dst, void *vaddr, struct drm_framebuffer *fb, struct drm_clip_rect *clip)

    Copy clip buffer

    :param void \*dst:
        Destination buffer

    :param void \*vaddr:
        Source buffer

    :param struct drm_framebuffer \*fb:
        DRM framebuffer

    :param struct drm_clip_rect \*clip:
        Clip rectangle area to copy

.. _`tinydrm_swab16`:

tinydrm_swab16
==============

.. c:function:: void tinydrm_swab16(u16 *dst, void *vaddr, struct drm_framebuffer *fb, struct drm_clip_rect *clip)

    Swap bytes into clip buffer

    :param u16 \*dst:
        RGB565 destination buffer

    :param void \*vaddr:
        RGB565 source buffer

    :param struct drm_framebuffer \*fb:
        DRM framebuffer

    :param struct drm_clip_rect \*clip:
        Clip rectangle area to copy

.. _`tinydrm_xrgb8888_to_rgb565`:

tinydrm_xrgb8888_to_rgb565
==========================

.. c:function:: void tinydrm_xrgb8888_to_rgb565(u16 *dst, void *vaddr, struct drm_framebuffer *fb, struct drm_clip_rect *clip, bool swap)

    Convert XRGB8888 to RGB565 clip buffer

    :param u16 \*dst:
        RGB565 destination buffer

    :param void \*vaddr:
        XRGB8888 source buffer

    :param struct drm_framebuffer \*fb:
        DRM framebuffer

    :param struct drm_clip_rect \*clip:
        Clip rectangle area to copy

    :param bool swap:
        Swap bytes

.. _`tinydrm_xrgb8888_to_rgb565.description`:

Description
-----------

Drivers can use this function for RGB565 devices that don't natively
support XRGB8888.

.. _`tinydrm_of_find_backlight`:

tinydrm_of_find_backlight
=========================

.. c:function:: struct backlight_device *tinydrm_of_find_backlight(struct device *dev)

    Find backlight device in device-tree

    :param struct device \*dev:
        Device

.. _`tinydrm_of_find_backlight.description`:

Description
-----------

This function looks for a DT node pointed to by a property named 'backlight'
and uses \ :c:func:`of_find_backlight_by_node`\  to get the backlight device.
Additionally if the brightness property is zero, it is set to
max_brightness.

.. _`tinydrm_of_find_backlight.return`:

Return
------

NULL if there's no backlight property.
Error pointer -EPROBE_DEFER if the DT node is found, but no backlight device
is found.
If the backlight device is found, a pointer to the structure is returned.

.. _`tinydrm_enable_backlight`:

tinydrm_enable_backlight
========================

.. c:function:: int tinydrm_enable_backlight(struct backlight_device *backlight)

    Enable backlight helper

    :param struct backlight_device \*backlight:
        Backlight device

.. _`tinydrm_enable_backlight.return`:

Return
------

Zero on success, negative error code on failure.

.. _`tinydrm_disable_backlight`:

tinydrm_disable_backlight
=========================

.. c:function:: int tinydrm_disable_backlight(struct backlight_device *backlight)

    Disable backlight helper

    :param struct backlight_device \*backlight:
        Backlight device

.. _`tinydrm_disable_backlight.return`:

Return
------

Zero on success, negative error code on failure.

.. _`tinydrm_spi_max_transfer_size`:

tinydrm_spi_max_transfer_size
=============================

.. c:function:: size_t tinydrm_spi_max_transfer_size(struct spi_device *spi, size_t max_len)

    Determine max SPI transfer size

    :param struct spi_device \*spi:
        SPI device

    :param size_t max_len:
        Maximum buffer size needed (optional)

.. _`tinydrm_spi_max_transfer_size.description`:

Description
-----------

This function returns the maximum size to use for SPI transfers. It checks
the SPI master, the optional \ ``max_len``\  and the module parameter spi_max and
returns the smallest.

.. _`tinydrm_spi_max_transfer_size.return`:

Return
------

Maximum size for SPI transfers

.. _`tinydrm_spi_bpw_supported`:

tinydrm_spi_bpw_supported
=========================

.. c:function:: bool tinydrm_spi_bpw_supported(struct spi_device *spi, u8 bpw)

    Check if bits per word is supported

    :param struct spi_device \*spi:
        SPI device

    :param u8 bpw:
        Bits per word

.. _`tinydrm_spi_bpw_supported.description`:

Description
-----------

This function checks to see if the SPI master driver supports \ ``bpw``\ .

.. _`tinydrm_spi_bpw_supported.return`:

Return
------

True if \ ``bpw``\  is supported, false otherwise.

.. _`tinydrm_spi_transfer`:

tinydrm_spi_transfer
====================

.. c:function:: int tinydrm_spi_transfer(struct spi_device *spi, u32 speed_hz, struct spi_transfer *header, u8 bpw, const void *buf, size_t len)

    SPI transfer helper

    :param struct spi_device \*spi:
        SPI device

    :param u32 speed_hz:
        Override speed (optional)

    :param struct spi_transfer \*header:
        Optional header transfer

    :param u8 bpw:
        Bits per word

    :param const void \*buf:
        Buffer to transfer

    :param size_t len:
        Buffer length

.. _`tinydrm_spi_transfer.description`:

Description
-----------

This SPI transfer helper breaks up the transfer of \ ``buf``\  into chunks which
the SPI master driver can handle. If the machine is Little Endian and the
SPI master driver doesn't support 16 bits per word, it swaps the bytes and
does a 8-bit transfer.
If \ ``header``\  is set, it is prepended to each SPI message.

.. _`tinydrm_spi_transfer.return`:

Return
------

Zero on success, negative error code on failure.

.. This file was automatic generated / don't edit.
