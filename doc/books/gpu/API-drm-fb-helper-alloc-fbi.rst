.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-alloc-fbi:

=======================
drm_fb_helper_alloc_fbi
=======================

*man drm_fb_helper_alloc_fbi(9)*

*4.6.0-rc5*

allocate fb_info and some of its members


Synopsis
========

.. c:function:: struct fb_info * drm_fb_helper_alloc_fbi( struct drm_fb_helper * fb_helper )

Arguments
=========

``fb_helper``
    driver-allocated fbdev helper


Description
===========

A helper to alloc fb_info and the members cmap and apertures. Called by
the driver within the fb_probe fb_helper callback function.


RETURNS
=======

fb_info pointer if things went okay, pointer containing error code
otherwise


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
