.. -*- coding: utf-8; mode: rst -*-

.. _API-i915-check-vgpu:

===============
i915_check_vgpu
===============

*man i915_check_vgpu(9)*

*4.6.0-rc5*

detect virtual GPU


Synopsis
========

.. c:function:: void i915_check_vgpu( struct drm_device * dev )

Arguments
=========

``dev``
    drm device *


Description
===========

This function is called at the initialization stage, to detect whether
running on a vGPU.


.. ------------------------------------------------------------------------------
.. This file was automatically converted from DocBook-XML with the dbxml
.. library (https://github.com/return42/sphkerneldoc). The origin XML comes
.. from the linux kernel, refer to:
..
.. * https://github.com/torvalds/linux/tree/master/Documentation/DocBook
.. ------------------------------------------------------------------------------
