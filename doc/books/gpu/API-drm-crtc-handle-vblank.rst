.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-crtc-handle-vblank:

======================
drm_crtc_handle_vblank
======================

*man drm_crtc_handle_vblank(9)*

*4.6.0-rc5*

handle a vblank event


Synopsis
========

.. c:function:: bool drm_crtc_handle_vblank( struct drm_crtc * crtc )

Arguments
=========

``crtc``
    where this event occurred


Description
===========

Drivers should call this routine in their vblank interrupt handlers to
update the vblank counter and send any signals that may be pending.

This is the native KMS version of ``drm_handle_vblank``.


Returns
=======

True if the event was successfully handled, false on failure.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
