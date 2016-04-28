.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-set-mode-prop-for-crtc:

=================================
drm_atomic_set_mode_prop_for_crtc
=================================

*man drm_atomic_set_mode_prop_for_crtc(9)*

*4.6.0-rc5*

set mode for CRTC


Synopsis
========

.. c:function:: int drm_atomic_set_mode_prop_for_crtc( struct drm_crtc_state * state, struct drm_property_blob * blob )

Arguments
=========

``state``
    the CRTC whose incoming state to update

``blob``
    pointer to blob property to use for mode


Description
===========

Set a mode (originating from a blob property) on the desired CRTC state.
This function will take a reference on the blob property for the CRTC
state, and release the reference held on the state's existing mode
property, if any was set.


RETURNS
=======

Zero on success, error code on failure. Cannot return -EDEADLK.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
