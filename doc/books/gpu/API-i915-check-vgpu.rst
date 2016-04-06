
.. _API-i915-check-vgpu:

===============
i915_check_vgpu
===============

*man i915_check_vgpu(9)*

*4.6.0-rc1*

detect virtual GPU


Synopsis
========

.. c:function:: void i915_check_vgpu( struct drm_device * dev )

Arguments
=========

``dev``
    drm device ⋆


Description
===========

This function is called at the initialization stage, to detect whether running on a vGPU.
