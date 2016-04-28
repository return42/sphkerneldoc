.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-state-default-release:

================================
drm_atomic_state_default_release
================================

*man drm_atomic_state_default_release(9)*

*4.6.0-rc5*

release memory initialized by drm_atomic_state_init


Synopsis
========

.. c:function:: void drm_atomic_state_default_release( struct drm_atomic_state * state )

Arguments
=========

``state``
    atomic state


Description
===========

Free all the memory allocated by drm_atomic_state_init. This is
useful for drivers that subclass the atomic state.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
