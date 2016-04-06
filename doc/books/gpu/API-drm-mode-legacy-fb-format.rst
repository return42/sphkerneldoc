
.. _API-drm-mode-legacy-fb-format:

=========================
drm_mode_legacy_fb_format
=========================

*man drm_mode_legacy_fb_format(9)*

*4.6.0-rc1*

compute drm fourcc code from legacy description


Synopsis
========

.. c:function:: uint32_t drm_mode_legacy_fb_format( uint32_t bpp, uint32_t depth )

Arguments
=========

``bpp``
    bits per pixels

``depth``
    bit depth per pixel


Description
===========

Computes a drm fourcc pixel format code for the given ``bpp``/``depth`` values. Useful in fbdev emulation code, since that deals in those values.
