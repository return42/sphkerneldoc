.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-mask:

=============
drm_crtc_mask
=============

*man drm_crtc_mask(9)*

*4.6.0-rc5*

find the mask of a registered CRTC


Synopsis
========

.. c:function:: uint32_t drm_crtc_mask( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    CRTC to find mask for


Description
===========

Given a registered CRTC, return the mask bit of that CRTC for an
encoder's possible_crtcs field.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
