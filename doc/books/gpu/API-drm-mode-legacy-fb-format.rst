.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-legacy-fb-format:

=========================
drm_mode_legacy_fb_format
=========================

*man drm_mode_legacy_fb_format(9)*

*4.6.0-rc5*

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

Computes a drm fourcc pixel format code for the given ``bpp``/``depth``
values. Useful in fbdev emulation code, since that deals in those
values.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
