.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/drm_fourcc.c

.. _`drm_get_format_name`:

drm_get_format_name
===================

.. c:function:: const char *drm_get_format_name(uint32_t format)

    return a string for drm fourcc format

    :param uint32_t format:
        format to compute name of

.. _`drm_get_format_name.description`:

Description
-----------

Note that the buffer used by this function is globally shared and owned by
the function itself.

.. _`drm_get_format_name.fixme`:

FIXME
-----

This isn't really multithreading safe.

.. _`drm_fb_get_bpp_depth`:

drm_fb_get_bpp_depth
====================

.. c:function:: void drm_fb_get_bpp_depth(uint32_t format, unsigned int *depth, int *bpp)

    get the bpp/depth values for format

    :param uint32_t format:
        pixel format (DRM_FORMAT\_\*)

    :param unsigned int \*depth:
        storage for the depth value

    :param int \*bpp:
        storage for the bpp value

.. _`drm_fb_get_bpp_depth.description`:

Description
-----------

This only supports RGB formats here for compat with code that doesn't use
pixel formats directly yet.

.. _`drm_format_num_planes`:

drm_format_num_planes
=====================

.. c:function:: int drm_format_num_planes(uint32_t format)

    get the number of planes for format

    :param uint32_t format:
        pixel format (DRM_FORMAT\_\*)

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
        pixel format (DRM_FORMAT\_\*)

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
        pixel format (DRM_FORMAT\_\*)

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
        pixel format (DRM_FORMAT\_\*)

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

