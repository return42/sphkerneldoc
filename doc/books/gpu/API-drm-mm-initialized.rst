.. -*- coding: utf-8; mode: rst -*-

.. _API-drm-mm-initialized:

==================
drm_mm_initialized
==================

*man drm_mm_initialized(9)*

*4.6.0-rc5*

checks whether an allocator is initialized


Synopsis
========

.. c:function:: bool drm_mm_initialized( struct drm_mm * mm )

Arguments
=========

``mm``
    drm_mm to check


Description
===========

Drivers should use this helpers for proper encapusulation of drm_mm
internals.


Returns
=======

True if the ``mm`` is initialized.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
