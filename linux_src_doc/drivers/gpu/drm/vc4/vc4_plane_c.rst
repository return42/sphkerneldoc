.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/vc4/vc4_plane.c

.. _`vc4-plane-module`:

VC4 plane module
================

Each DRM plane is a layer of pixels being scanned out by the HVS.

At atomic modeset check time, we compute the HVS display element
state that would be necessary for displaying the plane (giving us a
chance to figure out if a plane configuration is invalid), then at
atomic flush time the CRTC will ask us to write our element state
into the region of the HVS that it has allocated for us.

.. This file was automatic generated / don't edit.

