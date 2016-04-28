.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-destroy:

================
drm_mode_destroy
================

*man drm_mode_destroy(9)*

*4.6.0-rc5*

remove a mode


Synopsis
========

.. c:function:: void drm_mode_destroy( struct drm_device * dev, struct drm_display_mode * mode )

Arguments
=========

``dev``
    DRM device

``mode``
    mode to remove


Description
===========

Release ``mode``'s unique ID, then free it ``mode`` structure itself
using kfree.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
