
.. _API-intel-csr-load-program:

======================
intel_csr_load_program
======================

*man intel_csr_load_program(9)*

*4.6.0-rc1*

write the firmware from memory to register.


Synopsis
========

.. c:function:: bool intel_csr_load_program( struct drm_i915_private * dev_priv )

Arguments
=========

``dev_priv``
    i915 drm device.


Description
===========

CSR firmware is read from a .bin file and kept in internal memory one time. Everytime display comes back from low power state this function is called to copy the firmware from
internal memory to registers.
