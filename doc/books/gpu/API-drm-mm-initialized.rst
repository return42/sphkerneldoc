
.. _API-drm-mm-initialized:

==================
drm_mm_initialized
==================

*man drm_mm_initialized(9)*

*4.6.0-rc1*

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

Drivers should use this helpers for proper encapusulation of drm_mm internals.


Returns
=======

True if the ``mm`` is initialized.
