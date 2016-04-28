.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-state-alloc:

======================
drm_atomic_state_alloc
======================

*man drm_atomic_state_alloc(9)*

*4.6.0-rc5*

allocate atomic state


Synopsis
========

.. c:function:: struct drm_atomic_state * drm_atomic_state_alloc( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

This allocates an empty atomic state to track updates.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
