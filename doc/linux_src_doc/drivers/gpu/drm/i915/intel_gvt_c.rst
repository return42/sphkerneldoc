.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_gvt.c

.. _`intel_gvt_init`:

intel_gvt_init
==============

.. c:function:: int intel_gvt_init(struct drm_i915_private *dev_priv)

    initialize GVT components

    :param struct drm_i915_private \*dev_priv:
        drm i915 private data

.. _`intel_gvt_init.description`:

Description
-----------

This function is called at the initialization stage to create a GVT device.

.. _`intel_gvt_init.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_cleanup`:

intel_gvt_cleanup
=================

.. c:function:: void intel_gvt_cleanup(struct drm_i915_private *dev_priv)

    cleanup GVT components when i915 driver is unloading

    :param struct drm_i915_private \*dev_priv:
        drm i915 private \*

.. _`intel_gvt_cleanup.description`:

Description
-----------

This function is called at the i915 driver unloading stage, to shutdown
GVT components and release the related resources.

.. This file was automatic generated / don't edit.

