.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_uncore.c

.. _`intel_uncore_forcewake_get`:

intel_uncore_forcewake_get
==========================

.. c:function:: void intel_uncore_forcewake_get(struct drm_i915_private *dev_priv, enum forcewake_domains fw_domains)

    grab forcewake domain references

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum forcewake_domains fw_domains:
        forcewake domains to get reference on

.. _`intel_uncore_forcewake_get.description`:

Description
-----------

This function can be used get GT's forcewake domain references.
Normal register access will handle the forcewake domains automatically.
However if some sequence requires the GT to not power down a particular
forcewake domains this function should be called at the beginning of the
sequence. And subsequently the reference should be dropped by symmetric
call to \ :c:func:`intel_unforce_forcewake_put`\ . Usually caller wants all the domains
to be kept awake so the \ ``fw_domains``\  would be then FORCEWAKE_ALL.

.. _`intel_uncore_forcewake_get__locked`:

intel_uncore_forcewake_get__locked
==================================

.. c:function:: void intel_uncore_forcewake_get__locked(struct drm_i915_private *dev_priv, enum forcewake_domains fw_domains)

    grab forcewake domain references

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum forcewake_domains fw_domains:
        forcewake domains to get reference on

.. _`intel_uncore_forcewake_get__locked.description`:

Description
-----------

See \ :c:func:`intel_uncore_forcewake_get`\ . This variant places the onus
on the caller to explicitly handle the dev_priv->uncore.lock spinlock.

.. _`intel_uncore_forcewake_put`:

intel_uncore_forcewake_put
==========================

.. c:function:: void intel_uncore_forcewake_put(struct drm_i915_private *dev_priv, enum forcewake_domains fw_domains)

    release a forcewake domain reference

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum forcewake_domains fw_domains:
        forcewake domains to put references

.. _`intel_uncore_forcewake_put.description`:

Description
-----------

This function drops the device-level forcewakes for specified
domains obtained by \ :c:func:`intel_uncore_forcewake_get`\ .

.. _`intel_uncore_forcewake_put__locked`:

intel_uncore_forcewake_put__locked
==================================

.. c:function:: void intel_uncore_forcewake_put__locked(struct drm_i915_private *dev_priv, enum forcewake_domains fw_domains)

    grab forcewake domain references

    :param struct drm_i915_private \*dev_priv:
        i915 device instance

    :param enum forcewake_domains fw_domains:
        forcewake domains to get reference on

.. _`intel_uncore_forcewake_put__locked.description`:

Description
-----------

See \ :c:func:`intel_uncore_forcewake_put`\ . This variant places the onus
on the caller to explicitly handle the dev_priv->uncore.lock spinlock.

.. _`gen6_reset_engines`:

gen6_reset_engines
==================

.. c:function:: int gen6_reset_engines(struct drm_i915_private *dev_priv, unsigned engine_mask)

    reset individual engines

    :param struct drm_i915_private \*dev_priv:
        i915 device

    :param unsigned engine_mask:
        mask of \ :c:func:`intel_ring_flag`\  engines or ALL_ENGINES for full reset

.. _`gen6_reset_engines.description`:

Description
-----------

This function will reset the individual engines that are set in engine_mask.
If you provide ALL_ENGINES as mask, full global domain reset will be issued.

.. _`gen6_reset_engines.note`:

Note
----

It is responsibility of the caller to handle the difference between
asking full domain reset versus reset for all available individual engines.

Returns 0 on success, nonzero on error.

.. _`intel_uncore_forcewake_for_reg`:

intel_uncore_forcewake_for_reg
==============================

.. c:function:: enum forcewake_domains intel_uncore_forcewake_for_reg(struct drm_i915_private *dev_priv, i915_reg_t reg, unsigned int op)

    which forcewake domains are needed to access a register

    :param struct drm_i915_private \*dev_priv:
        pointer to struct drm_i915_private

    :param i915_reg_t reg:
        register in question

    :param unsigned int op:
        operation bitmask of FW_REG_READ and/or FW_REG_WRITE

.. _`intel_uncore_forcewake_for_reg.description`:

Description
-----------

Returns a set of forcewake domains required to be taken with for example
intel_uncore_forcewake_get for the specified register to be accessible in the
specified mode (read, write or read/write) with raw mmio accessors.

.. _`intel_uncore_forcewake_for_reg.note`:

NOTE
----

On Gen6 and Gen7 write forcewake domain (FORCEWAKE_RENDER) requires the
callers to do FIFO management on their own or risk losing writes.

.. This file was automatic generated / don't edit.

