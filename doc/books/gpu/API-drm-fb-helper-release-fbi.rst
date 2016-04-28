.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-fb-helper-release-fbi:

=========================
drm_fb_helper_release_fbi
=========================

*man drm_fb_helper_release_fbi(9)*

*4.6.0-rc5*

dealloc fb_info and its members


Synopsis
========

.. c:function:: void drm_fb_helper_release_fbi( struct drm_fb_helper * fb_helper )

Arguments
=========

``fb_helper``
    driver-allocated fbdev helper


Description
===========

A helper to free memory taken by fb_info and the members cmap and
apertures


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
