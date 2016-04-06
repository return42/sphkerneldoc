
.. _API-drm-atomic-get-crtc-state:

=========================
drm_atomic_get_crtc_state
=========================

*man drm_atomic_get_crtc_state(9)*

*4.6.0-rc1*

get crtc state


Synopsis
========

.. c:function:: struct drm_crtc_state ⋆ drm_atomic_get_crtc_state( struct drm_atomic_state * state, struct drm_crtc * crtc )

Arguments
=========

``state``
    global atomic state object

``crtc``
    crtc to get state object for


Description
===========

This function returns the crtc state for the given crtc, allocating it if needed. It will also grab the relevant crtc lock to make sure that the state is consistent.


Returns
=======

Either the allocated state or the error code encoded into the pointer. When the error is EDEADLK then the w/w mutex code has detected a deadlock and the entire atomic sequence must
be restarted. All other errors are fatal.
