.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_fourcc.c

.. _`drm_mode_legacy_fb_format`:

drm_mode_legacy_fb_format
=========================

.. c:function:: uint32_t drm_mode_legacy_fb_format(uint32_t bpp, uint32_t depth)

    compute drm fourcc code from legacy description

    :param uint32_t bpp:
        bits per pixels

    :param uint32_t depth:
        bit depth per pixel

.. _`drm_mode_legacy_fb_format.description`:

Description
-----------

Computes a drm fourcc pixel format code for the given \ ``bpp``\ /@depth values.
Useful in fbdev emulation code, since that deals in those values.

.. _`drm_get_format_name`:

drm_get_format_name
===================

.. c:function:: const char *drm_get_format_name(uint32_t format, struct drm_format_name_buf *buf)

    fill a string with a drm fourcc format's name

    :param uint32_t format:
        format to compute name of

    :param struct drm_format_name_buf \*buf:
        caller-supplied buffer

.. _`drm_format_info`:

drm_format_info
===============

.. c:function:: const struct drm_format_info *drm_format_info(u32 format)

    query information for a given format

    :param u32 format:
        pixel format (DRM_FORMAT_*)

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

    :param struct drm_device \*dev:
        DRM device

    :param const struct drm_mode_fb_cmd2 \*mode_cmd:
        metadata from the userspace fb creation request

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

    :param uint32_t format:
        pixel format (DRM_FORMAT_*)

.. _`drm_format_num_planes.return`:

Return
------

The number of planes used by the specified pixel format.

.. _`drm_format_plane_cpp`:

drm_format_plane_cpp
====================

.. c:function:: int drm_format_plane_cpp(uint32_t format, int plane)

    determine the bytes per pixel value

    :param uint32_t format:
        pixel format (DRM_FORMAT_*)

    :param int plane:
        plane index

.. _`drm_format_plane_cpp.return`:

Return
------

The bytes per pixel value for the specified plane.

.. _`drm_format_horz_chroma_subsampling`:

drm_format_horz_chroma_subsampling
==================================

.. c:function:: int drm_format_horz_chroma_subsampling(uint32_t format)

    get the horizontal chroma subsampling factor

    :param uint32_t format:
        pixel format (DRM_FORMAT_*)

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

    :param uint32_t format:
        pixel format (DRM_FORMAT_*)

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

    :param int width:
        width of the first plane

    :param uint32_t format:
        pixel format

    :param int plane:
        plane index

.. _`drm_format_plane_width.return`:

Return
------

The width of \ ``plane``\ , given that the width of the first plane is \ ``width``\ .

.. _`drm_format_plane_height`:

drm_format_plane_height
=======================

.. c:function:: int drm_format_plane_height(int height, uint32_t format, int plane)

    height of the plane given the first plane

    :param int height:
        height of the first plane

    :param uint32_t format:
        pixel format

    :param int plane:
        plane index

.. _`drm_format_plane_height.return`:

Return
------

The height of \ ``plane``\ , given that the height of the first plane is \ ``height``\ .

.. This file was automatic generated / don't edit.

