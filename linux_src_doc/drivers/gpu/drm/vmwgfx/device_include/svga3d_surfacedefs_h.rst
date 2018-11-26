.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vmwgfx/device_include/svga3d_surfacedefs.h

.. _`svga3dsurface_get_desc`:

svga3dsurface_get_desc
======================

.. c:function:: const struct svga3d_surface_desc *svga3dsurface_get_desc(SVGA3dSurfaceFormat format)

    Look up the appropriate SVGA3dSurfaceDesc for the given format.

    :param format:
        *undescribed*
    :type format: SVGA3dSurfaceFormat

.. _`svga3dsurface_get_mip_size`:

svga3dsurface_get_mip_size
==========================

.. c:function:: surf_size_struct svga3dsurface_get_mip_size(surf_size_struct base_level, u32 mip_level)

    Given a base level size and the mip level, compute the size of the mip level.

    :param base_level:
        *undescribed*
    :type base_level: surf_size_struct

    :param mip_level:
        *undescribed*
    :type mip_level: u32

.. _`svga3dsurface_get_image_buffer_size`:

svga3dsurface_get_image_buffer_size
===================================

.. c:function:: u32 svga3dsurface_get_image_buffer_size(const struct svga3d_surface_desc *desc, const surf_size_struct *size, u32 pitch)

    Calculates image buffer size.

    :param desc:
        *undescribed*
    :type desc: const struct svga3d_surface_desc \*

    :param size:
        *undescribed*
    :type size: const surf_size_struct \*

    :param pitch:
        *undescribed*
    :type pitch: u32

.. _`svga3dsurface_get_image_buffer_size.description`:

Description
-----------

Return the number of bytes of buffer space required to store one image of a
surface, optionally using the specified pitch.

If pitch is zero, it is assumed that rows are tightly packed.

This function is overflow-safe. If the result would have overflowed, instead
we return MAX_UINT32.

.. _`svga3dsurface_get_serialized_size`:

svga3dsurface_get_serialized_size
=================================

.. c:function:: u32 svga3dsurface_get_serialized_size(SVGA3dSurfaceFormat format, surf_size_struct base_level_size, u32 num_mip_levels, u32 num_layers)

    Get the serialized size for the image.

    :param format:
        *undescribed*
    :type format: SVGA3dSurfaceFormat

    :param base_level_size:
        *undescribed*
    :type base_level_size: surf_size_struct

    :param num_mip_levels:
        *undescribed*
    :type num_mip_levels: u32

    :param num_layers:
        *undescribed*
    :type num_layers: u32

.. _`svga3dsurface_get_serialized_size_extended`:

svga3dsurface_get_serialized_size_extended
==========================================

.. c:function:: u32 svga3dsurface_get_serialized_size_extended(SVGA3dSurfaceFormat format, surf_size_struct base_level_size, u32 num_mip_levels, u32 num_layers, u32 num_samples)

    Returns the number of bytes required for a surface with given parameters. Support for sample count.

    :param format:
        *undescribed*
    :type format: SVGA3dSurfaceFormat

    :param base_level_size:
        *undescribed*
    :type base_level_size: surf_size_struct

    :param num_mip_levels:
        *undescribed*
    :type num_mip_levels: u32

    :param num_layers:
        *undescribed*
    :type num_layers: u32

    :param num_samples:
        *undescribed*
    :type num_samples: u32

.. _`svga3dsurface_get_pixel_offset`:

svga3dsurface_get_pixel_offset
==============================

.. c:function:: u32 svga3dsurface_get_pixel_offset(SVGA3dSurfaceFormat format, u32 width, u32 height, u32 x, u32 y, u32 z)

    Compute the offset (in bytes) to a pixel in an image (or volume).

    :param format:
        *undescribed*
    :type format: SVGA3dSurfaceFormat

    :param width:
        The image width in pixels.
    :type width: u32

    :param height:
        The image height in pixels
    :type height: u32

    :param x:
        *undescribed*
    :type x: u32

    :param y:
        *undescribed*
    :type y: u32

    :param z:
        *undescribed*
    :type z: u32

.. _`svga3dsurface_is_gb_screen_target_format`:

svga3dsurface_is_gb_screen_target_format
========================================

.. c:function:: bool svga3dsurface_is_gb_screen_target_format(SVGA3dSurfaceFormat format)

    Is the specified format usable as a ScreenTarget? (with just the GBObjects cap-bit set)

    :param format:
        format to queried
    :type format: SVGA3dSurfaceFormat

.. _`svga3dsurface_is_gb_screen_target_format.return`:

Return
------

true if queried format is valid for screen targets

.. _`svga3dsurface_is_dx_screen_target_format`:

svga3dsurface_is_dx_screen_target_format
========================================

.. c:function:: bool svga3dsurface_is_dx_screen_target_format(SVGA3dSurfaceFormat format)

    Is the specified format usable as a ScreenTarget? (with DX10 enabled)

    :param format:
        format to queried
    :type format: SVGA3dSurfaceFormat

.. _`svga3dsurface_is_dx_screen_target_format.results`:

Results
-------

true if queried format is valid for screen targets

.. _`svga3dsurface_is_screen_target_format`:

svga3dsurface_is_screen_target_format
=====================================

.. c:function:: bool svga3dsurface_is_screen_target_format(SVGA3dSurfaceFormat format)

    Is the specified format usable as a ScreenTarget? (for some combination of caps)

    :param format:
        format to queried
    :type format: SVGA3dSurfaceFormat

.. _`svga3dsurface_is_screen_target_format.results`:

Results
-------

true if queried format is valid for screen targets

.. This file was automatic generated / don't edit.

