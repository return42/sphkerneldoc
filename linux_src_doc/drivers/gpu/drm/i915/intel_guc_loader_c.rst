.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_guc_loader.c

.. _`intel_guc_ucode_load`:

intel_guc_ucode_load
====================

.. c:function:: int intel_guc_ucode_load(struct drm_device *dev)

    load GuC uCode into the device

    :param struct drm_device \*dev:
        drm device

.. _`intel_guc_ucode_load.description`:

Description
-----------

Called from \ :c:func:`gem_init_hw`\  during driver loading and also after a GPU reset.

The firmware image should have already been fetched into memory by the
earlier call to \ :c:func:`intel_guc_ucode_init`\ , so here we need only check that
is succeeded, and then transfer the image to the h/w.

.. _`intel_guc_ucode_load.return`:

Return
------

non-zero code on error

.. _`intel_guc_ucode_init`:

intel_guc_ucode_init
====================

.. c:function:: void intel_guc_ucode_init(struct drm_device *dev)

    define parameters and fetch firmware

    :param struct drm_device \*dev:
        drm device

.. _`intel_guc_ucode_init.description`:

Description
-----------

Called early during driver load, but after GEM is initialised.

The firmware will be transferred to the GuC's memory later,
when \ :c:func:`intel_guc_ucode_load`\  is called.

.. _`intel_guc_ucode_fini`:

intel_guc_ucode_fini
====================

.. c:function:: void intel_guc_ucode_fini(struct drm_device *dev)

    clean up all allocated resources

    :param struct drm_device \*dev:
        drm device

.. This file was automatic generated / don't edit.

