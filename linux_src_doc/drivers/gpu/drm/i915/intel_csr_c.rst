.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_csr.c

.. _`intel_csr_load_program`:

intel_csr_load_program
======================

.. c:function:: void intel_csr_load_program(struct drm_i915_private *dev_priv)

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

.. c:function:: void intel_csr_ucode_init(struct drm_i915_private *dev_priv)

    initialize the firmware loading.

    :param struct drm_i915_private \*dev_priv:
        i915 drm device.

.. _`intel_csr_ucode_init.description`:

Description
-----------

This function is called at the time of loading the display driver to read
firmware from a .bin file and copied into a internal memory.

.. _`intel_csr_ucode_suspend`:

intel_csr_ucode_suspend
=======================

.. c:function:: void intel_csr_ucode_suspend(struct drm_i915_private *dev_priv)

    prepare CSR firmware before system suspend

    :param struct drm_i915_private \*dev_priv:
        i915 drm device

.. _`intel_csr_ucode_suspend.description`:

Description
-----------

Prepare the DMC firmware before entering system suspend. This includes
flushing pending work items and releasing any resources acquired during
init.

.. _`intel_csr_ucode_resume`:

intel_csr_ucode_resume
======================

.. c:function:: void intel_csr_ucode_resume(struct drm_i915_private *dev_priv)

    init CSR firmware during system resume

    :param struct drm_i915_private \*dev_priv:
        i915 drm device

.. _`intel_csr_ucode_resume.description`:

Description
-----------

Reinitialize the DMC firmware during system resume, reacquiring any
resources released in \ :c:func:`intel_csr_ucode_suspend`\ .

.. _`intel_csr_ucode_fini`:

intel_csr_ucode_fini
====================

.. c:function:: void intel_csr_ucode_fini(struct drm_i915_private *dev_priv)

    unload the CSR firmware.

    :param struct drm_i915_private \*dev_priv:
        i915 drm device.

.. _`intel_csr_ucode_fini.description`:

Description
-----------

Firmmware unloading includes freeing the internal memory and reset the
firmware loading status.

.. This file was automatic generated / don't edit.

