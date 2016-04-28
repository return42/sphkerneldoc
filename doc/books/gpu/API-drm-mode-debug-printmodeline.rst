.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mode-debug-printmodeline:

============================
drm_mode_debug_printmodeline
============================

*man drm_mode_debug_printmodeline(9)*

*4.6.0-rc5*

print a mode to dmesg


Synopsis
========

.. c:function:: void drm_mode_debug_printmodeline( const struct drm_display_mode * mode )

Arguments
=========

``mode``
    mode to print


Description
===========

Describe ``mode`` using DRM_DEBUG.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
