
.. _API-intel-bios-init:

===============
intel_bios_init
===============

*man intel_bios_init(9)*

*4.6.0-rc1*

find VBT and initialize settings from the BIOS


Synopsis
========

.. c:function:: int intel_bios_init( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 device instance


Description
===========

Loads the Video BIOS and checks that the VBT exists. Sets scratch registers to appropriate values.

Returns 0 on success, nonzero on failure.
