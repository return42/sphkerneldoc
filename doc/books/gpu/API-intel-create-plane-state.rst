.. -*- coding: utf-8; mode: rst -*-

.. _API-intel-create-plane-state:

========================
intel_create_plane_state
========================

*man intel_create_plane_state(9)*

*4.6.0-rc5*

create plane state object


Synopsis
========

.. c:function:: struct intel_plane_state * intel_create_plane_state( struct drm_plane * plane )

Arguments
=========

``plane``
    drm plane


Description
===========

Allocates a fresh plane state for the given plane and sets some of the
state values to sensible initial values.


Returns
=======

A newly allocated plane state, or NULL on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
