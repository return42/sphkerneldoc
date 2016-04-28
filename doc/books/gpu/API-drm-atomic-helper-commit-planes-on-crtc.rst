.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-commit-planes-on-crtc:

=======================================
drm_atomic_helper_commit_planes_on_crtc
=======================================

*man drm_atomic_helper_commit_planes_on_crtc(9)*

*4.6.0-rc5*

commit plane state for a crtc


Synopsis
========

.. c:function:: void drm_atomic_helper_commit_planes_on_crtc( struct drm_crtc_state * old_crtc_state )

Arguments
=========

``old_crtc_state``
    atomic state object with the old crtc state


Description
===========

This function commits the new plane state using the plane and atomic
helper functions for planes on the specific crtc. It assumes that the
atomic state has already been pushed into the relevant object state
pointers, since this step can no longer fail.

This function is useful when plane updates should be done crtc-by-crtc
instead of one global step like ``drm_atomic_helper_commit_planes``
does.

This function can only be savely used when planes are not allowed to
move between different CRTCs because this function doesn't handle
inter-CRTC depencies. Callers need to ensure that either no such
depencies exist, resolve them through ordering of commit calls or
through some other means.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
