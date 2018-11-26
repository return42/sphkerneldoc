.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_fourcc.c

.. _`drm_mode_legacy_fb_format`:

drm_mode_legacy_fb_format
=========================

.. c:function:: uint32_t drm_mode_legacy_fb_format(uint32_t bpp, uint32_t depth)

    compute drm fourcc code from legacy description

    :param bpp:
        bits per pixels
    :type bpp: uint32_t

    :param depth:
        bit depth per pixel
    :type depth: uint32_t

.. _`drm_mode_legacy_fb_format.description`:

Description
-----------

Computes a drm fourcc pixel format code for the given \ ``bpp``\ /@depth values.
Useful in fbdev emulation code, since that deals in those values.

.. _`drm_driver_legacy_fb_format`:

drm_driver_legacy_fb_format
===========================

.. c:function:: uint32_t drm_driver_legacy_fb_format(struct drm_device *dev, uint32_t bpp, uint32_t depth)

    compute drm fourcc code from legacy description

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param bpp:
        bits per pixels
    :type bpp: uint32_t

    :param depth:
        bit depth per pixel
    :type depth: uint32_t

.. _`drm_driver_legacy_fb_format.description`:

Description
-----------

Computes a drm fourcc pixel format code for the given \ ``bpp``\ /@depth values.
Unlike \ :c:func:`drm_mode_legacy_fb_format`\  this looks at the drivers mode_config,
and depending on the quirk_addfb_prefer_host_byte_order flag it returns
little endian byte order or host byte order framebuffer formats.

.. _`drm_get_format_name`:

drm_get_format_name
===================

.. c:function:: const char *drm_get_format_name(uint32_t format, struct drm_format_name_buf *buf)

    fill a string with a drm fourcc format's name

    :param format:
        format to compute name of
    :type format: uint32_t

    :param buf:
        caller-supplied buffer
    :type buf: struct drm_format_name_buf \*

.. _`drm_format_info`:

drm_format_info
===============

.. c:function:: const struct drm_format_info *drm_format_info(u32 format)

    query information for a given format

    :param format:
        pixel format (DRM_FORMAT_*)
    :type format: u32

.. _`drm_format_info.description`:

Description
-----------

The caller should only pass a supported pixel format to this function.
Unsupported pixel formats will generate a warning in the kernel log.

.. _`drm_format_info.return`:

Return
------

The instance of struct drm_format_info that describes the pixel format, or
NULL if the format is unsupported.

.. _`drm_get_format_info`:

drm_get_format_info
===================

.. c:function:: const struct drm_format_info *drm_get_format_info(struct drm_device *dev, const struct drm_mode_fb_cmd2 *mode_cmd)

    query information for a given framebuffer configuration

    :param dev:
        DRM device
    :type dev: struct drm_device \*

    :param mode_cmd:
        metadata from the userspace fb creation request
    :type mode_cmd: const struct drm_mode_fb_cmd2 \*

.. _`drm_get_format_info.return`:

Return
------

The instance of struct drm_format_info that describes the pixel format, or
NULL if the format is unsupported.

.. _`drm_format_num_planes`:

drm_format_num_planes
=====================

.. c:function:: int drm_format_num_planes(uint32_t format)

    get the number of planes for format

    :param format:
        pixel format (DRM_FORMAT_*)
    :type format: uint32_t

.. _`drm_format_num_planes.return`:

Return
------

The number of planes used by the specified pixel format.

.. _`drm_format_plane_cpp`:

drm_format_plane_cpp
====================

.. c:function:: int drm_format_plane_cpp(uint32_t format, int plane)

    determine the bytes per pixel value

    :param format:
        pixel format (DRM_FORMAT_*)
    :type format: uint32_t

    :param plane:
        plane index
    :type plane: int

.. _`drm_format_plane_cpp.return`:

Return
------

The bytes per pixel value for the specified plane.

.. _`drm_format_horz_chroma_subsampling`:

drm_format_horz_chroma_subsampling
==================================

.. c:function:: int drm_format_horz_chroma_subsampling(uint32_t format)

    get the horizontal chroma subsampling factor

    :param format:
        pixel format (DRM_FORMAT_*)
    :type format: uint32_t

.. _`drm_format_horz_chroma_subsampling.return`:

Return
------

The horizontal chroma subsampling factor for the
specified pixel format.

.. _`drm_format_vert_chroma_subsampling`:

drm_format_vert_chroma_subsampling
==================================

.. c:function:: int drm_format_vert_chroma_subsampling(uint32_t format)

    get the vertical chroma subsampling factor

    :param format:
        pixel format (DRM_FORMAT_*)
    :type format: uint32_t

.. _`drm_format_vert_chroma_subsampling.return`:

Return
------

The vertical chroma subsampling factor for the
specified pixel format.

.. _`drm_format_plane_width`:

drm_format_plane_width
======================

.. c:function:: int drm_format_plane_width(int width, uint32_t format, int plane)

    width of the plane given the first plane

    :param width:
        width of the first plane
    :type width: int

    :param format:
        pixel format
    :type format: uint32_t

    :param plane:
        plane index
    :type plane: int

.. _`drm_format_plane_width.return`:

Return
------

The width of \ ``plane``\ , given that the width of the first plane is \ ``width``\ .

.. _`drm_format_plane_height`:

drm_format_plane_height
=======================

.. c:function:: int drm_format_plane_height(int height, uint32_t format, int plane)

    height of the plane given the first plane

    :param height:
        height of the first plane
    :type height: int

    :param format:
        pixel format
    :type format: uint32_t

    :param plane:
        plane index
    :type plane: int

.. _`drm_format_plane_height.return`:

Return
------

The height of \ ``plane``\ , given that the height of the first plane is \ ``height``\ .

.. This file was automatic generated / don't edit.

