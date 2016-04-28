.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-get-plane-state:

==========================
drm_atomic_get_plane_state
==========================

*man drm_atomic_get_plane_state(9)*

*4.6.0-rc5*

get plane state


Synopsis
========

.. c:function:: struct drm_plane_state * drm_atomic_get_plane_state( struct drm_atomic_state * state, struct drm_plane * plane )

Arguments
=========

``state``
    global atomic state object

``plane``
    plane to get state object for


Description
===========

This function returns the plane state for the given plane, allocating it
if needed. It will also grab the relevant plane lock to make sure that
the state is consistent.


Returns
=======

Either the allocated state or the error code encoded into the pointer.
When the error is EDEADLK then the w/w mutex code has detected a
deadlock and the entire atomic sequence must be restarted. All other
errors are fatal.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
