.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-plane-reset:

=============================
drm_atomic_helper_plane_reset
=============================

*man drm_atomic_helper_plane_reset(9)*

*4.6.0-rc5*

default ->reset hook for planes


Synopsis
========

.. c:function:: void drm_atomic_helper_plane_reset( struct drm_plane * plane )

Arguments
=========

``plane``
    drm plane


Description
===========

Resets the atomic state for ``plane`` by freeing the state pointer
(which might be NULL, e.g. at driver load time) and allocating a new
empty state object.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
