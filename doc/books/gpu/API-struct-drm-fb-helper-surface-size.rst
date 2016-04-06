
.. _API-struct-drm-fb-helper-surface-size:

=================================
struct drm_fb_helper_surface_size
=================================

*man struct drm_fb_helper_surface_size(9)*

*4.6.0-rc1*

describes fbdev size and scanout surface size


Synopsis
========

.. code-block:: c

    struct drm_fb_helper_surface_size {
      u32 fb_width;
      u32 fb_height;
      u32 surface_width;
      u32 surface_height;
      u32 surface_bpp;
      u32 surface_depth;
    };


Members
=======

fb_width
    fbdev width

fb_height
    fbdev height

surface_width
    scanout buffer width

surface_height
    scanout buffer height

surface_bpp
    scanout buffer bpp

surface_depth
    scanout buffer depth


Description
===========

Note that the scanout surface width/height may be larger than the fbdev width/height. In case of multiple displays, the scanout surface is sized according to the largest
width/height (so it is large enough for all CRTCs to scanout). But the fbdev width/height is sized to the minimum width/ height of all the displays. This ensures that fbcon fits on
the smallest of the attached displays.

So what is passed to ``drm_fb_helper_fill_var`` should be fb_width/fb_height, rather than the surface size.
