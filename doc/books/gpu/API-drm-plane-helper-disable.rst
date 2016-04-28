.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-plane-helper-disable:

========================
drm_plane_helper_disable
========================

*man drm_plane_helper_disable(9)*

*4.6.0-rc5*

Transitional helper for plane disable


Synopsis
========

.. c:function:: int drm_plane_helper_disable( struct drm_plane * plane )

Arguments
=========

``plane``
    plane to disable


Description
===========

Provides a default plane disable handler using the atomic plane update
functions. It is fully left to the driver to check plane constraints and
handle corner-cases like a fully occluded or otherwise invisible plane.

This is useful for piecewise transitioning of a driver to the atomic
helpers.


RETURNS
=======

Zero on success, error code on failure


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
