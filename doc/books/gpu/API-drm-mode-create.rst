.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-create:

===============
drm_mode_create
===============

*man drm_mode_create(9)*

*4.6.0-rc5*

create a new display mode


Synopsis
========

.. c:function:: struct drm_display_mode * drm_mode_create( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device


Description
===========

Create a new, cleared drm_display_mode with kzalloc, allocate an ID
for it and return it.


Returns
=======

Pointer to new mode on success, NULL on error.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
