.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-state-clear:

======================
drm_atomic_state_clear
======================

*man drm_atomic_state_clear(9)*

*4.6.0-rc5*

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

When the w/w mutex algorithm detects a deadlock we need to back off and
drop all locks. So someone else could sneak in and change the current
modeset configuration. Which means that all the state assembled in
``state`` is no longer an atomic update to the current state, but to
some arbitrary earlier state. Which could break assumptions the driver's
->atomic_check likely relies on.

Hence we must clear all cached state and completely start over, using
this function.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
