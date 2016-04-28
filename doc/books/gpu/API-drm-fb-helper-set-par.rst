.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-set-par:

=====================
drm_fb_helper_set_par
=====================

*man drm_fb_helper_set_par(9)*

*4.6.0-rc5*

implementation for ->fb_set_par


Synopsis
========

.. c:function:: int drm_fb_helper_set_par( struct fb_info * info )

Arguments
=========

``info``
    fbdev registered by the helper


Description
===========

This will let fbcon do the mode init and is called at initialization
time by the fbdev core when registering the driver, and later on through
the hotplug callback.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
