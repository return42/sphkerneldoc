.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-crtc-check:

=====================
drm_atomic_crtc_check
=====================

*man drm_atomic_crtc_check(9)*

*4.6.0-rc5*

check crtc state


Synopsis
========

.. c:function:: int drm_atomic_crtc_check( struct drm_crtc * crtc, struct drm_crtc_state * state )

Arguments
=========

``crtc``
    crtc to check

``state``
    crtc state to check


Description
===========

Provides core sanity checks for crtc state.


RETURNS
=======

Zero on success, error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
