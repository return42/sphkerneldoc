.. -*- coding: utf-8; mode: rst -*-

====================
svga3d_surfacedefs.h
====================


.. _`svga3dsurface_get_pixel_offset`:

svga3dsurface_get_pixel_offset
==============================

.. c:function:: u32 svga3dsurface_get_pixel_offset (SVGA3dSurfaceFormat format, u32 width, u32 height, u32 x, u32 y, u32 z)

    Compute the offset (in bytes) to a pixel in an image (or volume).

    :param SVGA3dSurfaceFormat format:

        *undescribed*

    :param u32 width:
        The image width in pixels.

    :param u32 height:
        The image height in pixels

    :param u32 x:

        *undescribed*

    :param u32 y:

        *undescribed*

    :param u32 z:

        *undescribed*



.. _`svga3dsurface_is_gb_screen_target_format`:

svga3dsurface_is_gb_screen_target_format
========================================

.. c:function:: bool svga3dsurface_is_gb_screen_target_format (SVGA3dSurfaceFormat format)

    Is the specified format usable as a ScreenTarget? (with just the GBObjects cap-bit set)

    :param SVGA3dSurfaceFormat format:
        format to queried



.. _`svga3dsurface_is_gb_screen_target_format.returns`:

RETURNS
-------

true if queried format is valid for screen targets



.. _`svga3dsurface_is_dx_screen_target_format`:

svga3dsurface_is_dx_screen_target_format
========================================

.. c:function:: bool svga3dsurface_is_dx_screen_target_format (SVGA3dSurfaceFormat format)

    Is the specified format usable as a ScreenTarget? (with DX10 enabled)

    :param SVGA3dSurfaceFormat format:
        format to queried



.. _`svga3dsurface_is_dx_screen_target_format.results`:

Results
-------

true if queried format is valid for screen targets



.. _`svga3dsurface_is_screen_target_format`:

svga3dsurface_is_screen_target_format
=====================================

.. c:function:: bool svga3dsurface_is_screen_target_format (SVGA3dSurfaceFormat format)

    Is the specified format usable as a ScreenTarget? (for some combination of caps)

    :param SVGA3dSurfaceFormat format:
        format to queried



.. _`svga3dsurface_is_screen_target_format.results`:

Results
-------

true if queried format is valid for screen targets

