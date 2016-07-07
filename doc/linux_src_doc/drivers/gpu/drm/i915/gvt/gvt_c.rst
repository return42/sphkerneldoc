.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/gvt.c

.. _`intel_gvt_init_host`:

intel_gvt_init_host
===================

.. c:function:: int intel_gvt_init_host( void)

    Load MPT modules and detect if we're running in host

    :param  void:
        no arguments

.. _`intel_gvt_init_host.description`:

Description
-----------

This function is called at the driver loading stage. If failed to find a
loadable MPT module or detect currently we're running in a VM, then GVT-g
will be disabled

.. _`intel_gvt_init_host.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_clean_device`:

intel_gvt_clean_device
======================

.. c:function:: void intel_gvt_clean_device(struct drm_i915_private *dev_priv)

    clean a GVT device

    :param struct drm_i915_private \*dev_priv:
        *undescribed*

.. _`intel_gvt_clean_device.description`:

Description
-----------

This function is called at the driver unloading stage, to free the
resources owned by a GVT device.

.. _`intel_gvt_init_device`:

intel_gvt_init_device
=====================

.. c:function:: int intel_gvt_init_device(struct drm_i915_private *dev_priv)

    initialize a GVT device

    :param struct drm_i915_private \*dev_priv:
        drm i915 private data

.. _`intel_gvt_init_device.description`:

Description
-----------

This function is called at the initialization stage, to initialize
necessary GVT components.

.. _`intel_gvt_init_device.return`:

Return
------

Zero on success, negative error code if failed.

.. This file was automatic generated / don't edit.

