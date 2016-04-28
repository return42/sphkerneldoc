.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-helper-crtc-enable-color-mgmt:

=================================
drm_helper_crtc_enable_color_mgmt
=================================

*man drm_helper_crtc_enable_color_mgmt(9)*

*4.6.0-rc5*

enable color management properties


Synopsis
========

.. c:function:: void drm_helper_crtc_enable_color_mgmt( struct drm_crtc * crtc, int degamma_lut_size, int gamma_lut_size )

Arguments
=========

``crtc``
    DRM CRTC

``degamma_lut_size``
    the size of the degamma lut (before CSC)

``gamma_lut_size``
    the size of the gamma lut (after CSC)


Description
===========

This function lets the driver enable the color correction properties on
a CRTC. This includes 3 degamma, csc and gamma properties that userspace
can set and 2 size properties to inform the userspace of the lut sizes.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
