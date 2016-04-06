.. -*- coding: utf-8; mode: rst -*-

===========
intel_csr.c
===========



.. _xref_intel_csr_load_program:

intel_csr_load_program
======================

.. c:function:: bool intel_csr_load_program (struct drm_i915_private * dev_priv)

    write the firmware from memory to register.

    :param struct drm_i915_private * dev_priv:
        i915 drm device.



Description
-----------

CSR firmware is read from a .bin file and kept in internal memory one time.
Everytime display comes back from low power state this function is called to
copy the firmware from internal memory to registers.




.. _xref_intel_csr_ucode_init:

intel_csr_ucode_init
====================

.. c:function:: void intel_csr_ucode_init (struct drm_i915_private * dev_priv)

    initialize the firmware loading.

    :param struct drm_i915_private * dev_priv:
        i915 drm device.



Description
-----------

This function is called at the time of loading the display driver to read
firmware from a .bin file and copied into a internal memory.




.. _xref_intel_csr_ucode_fini:

intel_csr_ucode_fini
====================

.. c:function:: void intel_csr_ucode_fini (struct drm_i915_private * dev_priv)

    unload the CSR firmware.

    :param struct drm_i915_private * dev_priv:
        i915 drm device.



Description
-----------

Firmmware unloading includes freeing the internal momory and reset the
firmware loading status.


