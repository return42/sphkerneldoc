.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_guc_loader.c

.. _`intel_guc_setup`:

intel_guc_setup
===============

.. c:function:: int intel_guc_setup(struct drm_device *dev)

    finish preparing the GuC for activity

    :param struct drm_device \*dev:
        drm device

.. _`intel_guc_setup.description`:

Description
-----------

Called from \ :c:func:`gem_init_hw`\  during driver loading and also after a GPU reset.

The main action required here it to load the GuC uCode into the device.
The firmware image should have already been fetched into memory by the
earlier call to \ :c:func:`intel_guc_init`\ , so here we need only check that worked,
and then transfer the image to the h/w.

.. _`intel_guc_setup.return`:

Return
------

non-zero code on error

.. _`intel_guc_init`:

intel_guc_init
==============

.. c:function:: void intel_guc_init(struct drm_device *dev)

    define parameters and fetch firmware

    :param struct drm_device \*dev:
        drm device

.. _`intel_guc_init.description`:

Description
-----------

Called early during driver load, but after GEM is initialised.

The firmware will be transferred to the GuC's memory later,
when \ :c:func:`intel_guc_setup`\  is called.

.. _`intel_guc_fini`:

intel_guc_fini
==============

.. c:function:: void intel_guc_fini(struct drm_device *dev)

    clean up all allocated resources

    :param struct drm_device \*dev:
        drm device

.. This file was automatic generated / don't edit.

