.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-atomic-helper-check-planes:

==============================
drm_atomic_helper_check_planes
==============================

*man drm_atomic_helper_check_planes(9)*

*4.6.0-rc5*

validate state object for planes changes


Synopsis
========

.. c:function:: int drm_atomic_helper_check_planes( struct drm_device * dev, struct drm_atomic_state * state )

Arguments
=========

``dev``
    DRM device

``state``
    the driver state object


Description
===========

Check the state object to see if the requested state is physically
possible. This does all the plane update related checks using by calling
into the ->atomic_check hooks provided by the driver.

It also sets crtc_state->planes_changed to indicate that a crtc has
updated planes.

RETURNS Zero for success or -errno


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
