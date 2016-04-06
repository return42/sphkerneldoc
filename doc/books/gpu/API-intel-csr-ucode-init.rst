
.. _API-intel-csr-ucode-init:

====================
intel_csr_ucode_init
====================

*man intel_csr_ucode_init(9)*

*4.6.0-rc1*

initialize the firmware loading.


Synopsis
========

.. c:function:: void intel_csr_ucode_init( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 drm device.


Description
===========

This function is called at the time of loading the display driver to read firmware from a .bin file and copied into a internal memory.
