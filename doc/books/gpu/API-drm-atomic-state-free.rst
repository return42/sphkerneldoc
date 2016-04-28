.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-state-free:

=====================
drm_atomic_state_free
=====================

*man drm_atomic_state_free(9)*

*4.6.0-rc5*

free all memory for an atomic state


Synopsis
========

.. c:function:: void drm_atomic_state_free( struct drm_atomic_state * state )

Arguments
=========

``state``
    atomic state to deallocate


Description
===========

This frees all memory associated with an atomic state, including all the
per-object state for planes, crtcs and connectors.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
