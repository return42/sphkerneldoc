
.. _API-intel-logical-rings-init:

========================
intel_logical_rings_init
========================

*man intel_logical_rings_init(9)*

*4.6.0-rc1*

allocate, populate and init the Engine Command Streamers


Synopsis
========

.. c:function:: int intel_logical_rings_init( struct drm_device * dev )

Arguments
=========

``dev``
    DRM device.


Description
===========

This function inits the engines for an Execlists submission style (the equivalent in the legacy ringbuffer submission world would be i915_gem_init_rings). It does it only for
those engines that are present in the hardware.


Return
======

non-zero if the initialization failed.
