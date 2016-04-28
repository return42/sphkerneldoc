.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-legacy-gamma-set:

==================================
drm_atomic_helper_legacy_gamma_set
==================================

*man drm_atomic_helper_legacy_gamma_set(9)*

*4.6.0-rc5*

set the legacy gamma correction table


Synopsis
========

.. c:function:: void drm_atomic_helper_legacy_gamma_set( struct drm_crtc * crtc, u16 * red, u16 * green, u16 * blue, uint32_t start, uint32_t size )

Arguments
=========

``crtc``
    CRTC object

``red``
    red correction table

``green``
    green correction table

``blue``
    green correction table

``start``
    -- undescribed --

``size``
    size of the tables


Description
===========

Implements support for legacy gamma correction table for drivers that
support color management through the DEGAMMA_LUT/GAMMA_LUT properties.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
