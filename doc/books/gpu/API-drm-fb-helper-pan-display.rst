.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-pan-display:

=========================
drm_fb_helper_pan_display
=========================

*man drm_fb_helper_pan_display(9)*

*4.6.0-rc5*

implementation for ->fb_pan_display


Synopsis
========

.. c:function:: int drm_fb_helper_pan_display( struct fb_var_screeninfo * var, struct fb_info * info )

Arguments
=========

``var``
    updated screen information

``info``
    fbdev registered by the helper


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
