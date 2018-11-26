.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/tinydrm/core/tinydrm-helpers.c

.. _`tinydrm_merge_clips`:

tinydrm_merge_clips
===================

.. c:function:: bool tinydrm_merge_clips(struct drm_clip_rect *dst, struct drm_clip_rect *src, unsigned int num_clips, unsigned int flags, u32 max_width, u32 max_height)

    Merge clip rectangles

    :param dst:
        Destination clip rectangle
    :type dst: struct drm_clip_rect \*

    :param src:
        Source clip rectangle(s)
    :type src: struct drm_clip_rect \*

    :param num_clips:
        Number of \ ``src``\  clip rectangles
    :type num_clips: unsigned int

    :param flags:
        Dirty fb ioctl flags
    :type flags: unsigned int

    :param max_width:
        Maximum width of \ ``dst``\ 
    :type max_width: u32

    :param max_height:
        Maximum height of \ ``dst``\ 
    :type max_height: u32

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

    :param dst:
        Destination buffer
    :type dst: void \*

    :param vaddr:
        Source buffer
    :type vaddr: void \*

    :param fb:
        DRM framebuffer
    :type fb: struct drm_framebuffer \*

    :param clip:
        Clip rectangle area to copy
    :type clip: struct drm_clip_rect \*

.. _`tinydrm_swab16`:

tinydrm_swab16
==============

.. c:function:: void tinydrm_swab16(u16 *dst, void *vaddr, struct drm_framebuffer *fb, struct drm_clip_rect *clip)

    Swap bytes into clip buffer

    :param dst:
        RGB565 destination buffer
    :type dst: u16 \*

    :param vaddr:
        RGB565 source buffer
    :type vaddr: void \*

    :param fb:
        DRM framebuffer
    :type fb: struct drm_framebuffer \*

    :param clip:
        Clip rectangle area to copy
    :type clip: struct drm_clip_rect \*

.. _`tinydrm_xrgb8888_to_rgb565`:

tinydrm_xrgb8888_to_rgb565
==========================

.. c:function:: void tinydrm_xrgb8888_to_rgb565(u16 *dst, void *vaddr, struct drm_framebuffer *fb, struct drm_clip_rect *clip, bool swap)

    Convert XRGB8888 to RGB565 clip buffer

    :param dst:
        RGB565 destination buffer
    :type dst: u16 \*

    :param vaddr:
        XRGB8888 source buffer
    :type vaddr: void \*

    :param fb:
        DRM framebuffer
    :type fb: struct drm_framebuffer \*

    :param clip:
        Clip rectangle area to copy
    :type clip: struct drm_clip_rect \*

    :param swap:
        Swap bytes
    :type swap: bool

.. _`tinydrm_xrgb8888_to_rgb565.description`:

Description
-----------

Drivers can use this function for RGB565 devices that don't natively
support XRGB8888.

.. _`tinydrm_xrgb8888_to_gray8`:

tinydrm_xrgb8888_to_gray8
=========================

.. c:function:: void tinydrm_xrgb8888_to_gray8(u8 *dst, void *vaddr, struct drm_framebuffer *fb, struct drm_clip_rect *clip)

    Convert XRGB8888 to grayscale

    :param dst:
        8-bit grayscale destination buffer
    :type dst: u8 \*

    :param vaddr:
        XRGB8888 source buffer
    :type vaddr: void \*

    :param fb:
        DRM framebuffer
    :type fb: struct drm_framebuffer \*

    :param clip:
        Clip rectangle area to copy
    :type clip: struct drm_clip_rect \*

.. _`tinydrm_xrgb8888_to_gray8.description`:

Description
-----------

Drm doesn't have native monochrome or grayscale support.
Such drivers can announce the commonly supported XR24 format to userspace
and use this function to convert to the native format.

Monochrome drivers will use the most significant bit,
where 1 means foreground color and 0 background color.

ITU BT.601 is used for the RGB -> luma (brightness) conversion.

.. _`tinydrm_spi_max_transfer_size`:

tinydrm_spi_max_transfer_size
=============================

.. c:function:: size_t tinydrm_spi_max_transfer_size(struct spi_device *spi, size_t max_len)

    Determine max SPI transfer size

    :param spi:
        SPI device
    :type spi: struct spi_device \*

    :param max_len:
        Maximum buffer size needed (optional)
    :type max_len: size_t

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

    :param spi:
        SPI device
    :type spi: struct spi_device \*

    :param bpw:
        Bits per word
    :type bpw: u8

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

    :param spi:
        SPI device
    :type spi: struct spi_device \*

    :param speed_hz:
        Override speed (optional)
    :type speed_hz: u32

    :param header:
        Optional header transfer
    :type header: struct spi_transfer \*

    :param bpw:
        Bits per word
    :type bpw: u8

    :param buf:
        Buffer to transfer
    :type buf: const void \*

    :param len:
        Buffer length
    :type len: size_t

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

