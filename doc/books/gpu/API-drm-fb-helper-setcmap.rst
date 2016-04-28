.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-setcmap:

=====================
drm_fb_helper_setcmap
=====================

*man drm_fb_helper_setcmap(9)*

*4.6.0-rc5*

implementation for ->fb_setcmap


Synopsis
========

.. c:function:: int drm_fb_helper_setcmap( struct fb_cmap * cmap, struct fb_info * info )

Arguments
=========

``cmap``
    cmap to set

``info``
    fbdev registered by the helper


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
