.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-set-crtc-for-plane:

=============================
drm_atomic_set_crtc_for_plane
=============================

*man drm_atomic_set_crtc_for_plane(9)*

*4.6.0-rc5*

set crtc for plane


Synopsis
========

.. c:function:: int drm_atomic_set_crtc_for_plane( struct drm_plane_state * plane_state, struct drm_crtc * crtc )

Arguments
=========

``plane_state``
    the plane whose incoming state to update

``crtc``
    crtc to use for the plane


Description
===========

Changing the assigned crtc for a plane requires us to grab the lock and
state for the new crtc, as needed. This function takes care of all these
details besides updating the pointer in the state object itself.


Returns
=======

0 on success or can fail with -EDEADLK or -ENOMEM. When the error is
EDEADLK then the w/w mutex code has detected a deadlock and the entire
atomic sequence must be restarted. All other errors are fatal.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
