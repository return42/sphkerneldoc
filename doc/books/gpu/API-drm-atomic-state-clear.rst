
.. _API-drm-atomic-state-clear:

======================
drm_atomic_state_clear
======================

*man drm_atomic_state_clear(9)*

*4.6.0-rc1*

clear state object


Synopsis
========

.. c:function:: void drm_atomic_state_clear( struct drm_atomic_state * state )

Arguments
=========

``state``
    atomic state


Description
===========

When the w/w mutex algorithm detects a deadlock we need to back off and drop all locks. So someone else could sneak in and change the current modeset configuration. Which means
that all the state assembled in ``state`` is no longer an atomic update to the current state, but to some arbitrary earlier state. Which could break assumptions the driver's
->atomic_check likely relies on.

Hence we must clear all cached state and completely start over, using this function.
