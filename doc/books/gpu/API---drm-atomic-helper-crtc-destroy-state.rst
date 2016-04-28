.. -*- coding: utf-8; mode: rst -*-

.. _API---drm-atomic-helper-crtc-destroy-state:

======================================
__drm_atomic_helper_crtc_destroy_state
======================================

*man __drm_atomic_helper_crtc_destroy_state(9)*

*4.6.0-rc5*

release CRTC state


Synopsis
========

.. c:function:: void __drm_atomic_helper_crtc_destroy_state( struct drm_crtc * crtc, struct drm_crtc_state * state )

Arguments
=========

``crtc``
    CRTC object

``state``
    CRTC state object to release


Description
===========

Releases all resources stored in the CRTC state without actually freeing
the memory of the CRTC state. This is useful for drivers that subclass
the CRTC state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
