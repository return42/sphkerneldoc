
.. _API-drm-atomic-crtc-state-for-each-plane:

====================================
drm_atomic_crtc_state_for_each_plane
====================================

*man drm_atomic_crtc_state_for_each_plane(9)*

*4.6.0-rc1*

iterate over attached planes in new state


Synopsis
========

.. c:function:: drm_atomic_crtc_state_for_each_plane( plane, crtc_state )

Arguments
=========

``plane``
    the loop cursor

``crtc_state``
    the incoming crtc-state


Description
===========

Similar to ``drm_crtc_for_each_plane``, but iterates the planes that will be attached if the specified state is applied. Useful during (for example) ->``atomic_check`` operations,
to validate the incoming state
