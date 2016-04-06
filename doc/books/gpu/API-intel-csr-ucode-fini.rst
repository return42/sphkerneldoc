
.. _API-intel-csr-ucode-fini:

====================
intel_csr_ucode_fini
====================

*man intel_csr_ucode_fini(9)*

*4.6.0-rc1*

unload the CSR firmware.


Synopsis
========

.. c:function:: void intel_csr_ucode_fini( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 drm device.


Description
===========

Firmmware unloading includes freeing the internal momory and reset the firmware loading status.
