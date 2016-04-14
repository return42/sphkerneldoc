.. -*- coding: utf-8; mode: rst -*-

===========
intel_csr.c
===========

.. _`csr-support-for-dmc`:

csr support for dmc
===================

Display Context Save and Restore (CSR) firmware support added from gen9
onwards to drive newly added DMC (Display microcontroller) in display
engine to save and restore the state of display engine when it enter into
low-power state and comes back to normal.

Firmware loading status will be one of the below states: FW_UNINITIALIZED,
FW_LOADED, FW_FAILED.

Once the firmware is written into the registers status will be moved from
FW_UNINITIALIZED to FW_LOADED and for any erroneous condition status will
be moved to FW_FAILED.


.. _`intel_csr_load_program`:

intel_csr_load_program
======================

.. c:function:: bool intel_csr_load_program (struct drm_i915_private *dev_priv)

    write the firmware from memory to register.

    :param struct drm_i915_private \*dev_priv:
        i915 drm device.


.. _`intel_csr_load_program.description`:

Description
-----------

CSR firmware is read from a .bin file and kept in internal memory one time.
Everytime display comes back from low power state this function is called to
copy the firmware from internal memory to registers.


.. _`intel_csr_ucode_init`:

intel_csr_ucode_init
====================

.. c:function:: void intel_csr_ucode_init (struct drm_i915_private *dev_priv)

    initialize the firmware loading.

    :param struct drm_i915_private \*dev_priv:
        i915 drm device.


.. _`intel_csr_ucode_init.description`:

Description
-----------

This function is called at the time of loading the display driver to read
firmware from a .bin file and copied into a internal memory.


.. _`intel_csr_ucode_fini`:

intel_csr_ucode_fini
====================

.. c:function:: void intel_csr_ucode_fini (struct drm_i915_private *dev_priv)

    unload the CSR firmware.

    :param struct drm_i915_private \*dev_priv:
        i915 drm device.


.. _`intel_csr_ucode_fini.description`:

Description
-----------

Firmmware unloading includes freeing the internal momory and reset the
firmware loading status.

