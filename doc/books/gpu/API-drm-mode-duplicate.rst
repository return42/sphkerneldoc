.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-duplicate:

==================
drm_mode_duplicate
==================

*man drm_mode_duplicate(9)*

*4.6.0-rc5*

allocate and duplicate an existing mode


Synopsis
========

.. c:function:: struct drm_display_mode * drm_mode_duplicate( struct drm_device * dev, const struct drm_display_mode * mode )

Arguments
=========

``dev``
    drm_device to allocate the duplicated mode for

``mode``
    mode to duplicate


Description
===========

Just allocate a new mode, copy the existing mode into it, and return a
pointer to it. Used to create new instances of established modes.


Returns
=======

Pointer to duplicated mode on success, NULL on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
