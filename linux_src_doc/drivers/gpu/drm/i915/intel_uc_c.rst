.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_uc.c

.. _`intel_uc_sanitize_options`:

intel_uc_sanitize_options
=========================

.. c:function:: void intel_uc_sanitize_options(struct drm_i915_private *dev_priv)

    sanitize uC related modparam options

    :param struct drm_i915_private \*dev_priv:
        device private

.. _`intel_uc_sanitize_options.description`:

Description
-----------

In case of "enable_guc" option this function will attempt to modify
it only if it was initially set to "auto(-1)". Default value for this
modparam varies between platforms and it is hardcoded in driver code.
Any other modparam value is only monitored against availability of the
related hardware or firmware definitions.

.. _`intel_uc_init_mmio`:

intel_uc_init_mmio
==================

.. c:function:: void intel_uc_init_mmio(struct drm_i915_private *dev_priv)

    setup uC MMIO access

    :param struct drm_i915_private \*dev_priv:
        device private

.. _`intel_uc_init_mmio.description`:

Description
-----------

Setup minimal state necessary for MMIO accesses later in the
initialization sequence.

.. This file was automatic generated / don't edit.

