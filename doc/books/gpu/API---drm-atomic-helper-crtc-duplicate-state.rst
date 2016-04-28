.. -*- coding: utf-8; mode: rst -*-

.. _API---drm-atomic-helper-crtc-duplicate-state:

========================================
__drm_atomic_helper_crtc_duplicate_state
========================================

*man __drm_atomic_helper_crtc_duplicate_state(9)*

*4.6.0-rc5*

copy atomic CRTC state


Synopsis
========

.. c:function:: void __drm_atomic_helper_crtc_duplicate_state( struct drm_crtc * crtc, struct drm_crtc_state * state )

Arguments
=========

``crtc``
    CRTC object

``state``
    atomic CRTC state


Description
===========

Copies atomic state from a CRTC's current state and resets inferred
values. This is useful for drivers that subclass the CRTC state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
