.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-blank:

===================
drm_fb_helper_blank
===================

*man drm_fb_helper_blank(9)*

*4.6.0-rc5*

implementation for ->fb_blank


Synopsis
========

.. c:function:: int drm_fb_helper_blank( int blank, struct fb_info * info )

Arguments
=========

``blank``
    desired blanking state

``info``
    fbdev registered by the helper


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
