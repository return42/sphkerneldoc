.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_guc.c

.. _`intel_guc_auth_huc`:

intel_guc_auth_huc
==================

.. c:function:: int intel_guc_auth_huc(struct intel_guc *guc, u32 rsa_offset)

    Send action to GuC to authenticate HuC ucode

    :param struct intel_guc \*guc:
        intel_guc structure

    :param u32 rsa_offset:
        rsa offset w.r.t ggtt base of huc vma

.. _`intel_guc_auth_huc.description`:

Description
-----------

Triggers a HuC firmware authentication request to the GuC via intel_guc_send
INTEL_GUC_ACTION_AUTHENTICATE_HUC interface. This function is invoked by
\ :c:func:`intel_huc_auth`\ .

.. _`intel_guc_auth_huc.return`:

Return
------

non-zero code on error

.. _`intel_guc_suspend`:

intel_guc_suspend
=================

.. c:function:: int intel_guc_suspend(struct drm_i915_private *dev_priv)

    notify GuC entering suspend state

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. _`intel_guc_resume`:

intel_guc_resume
================

.. c:function:: int intel_guc_resume(struct drm_i915_private *dev_priv)

    notify GuC resuming from suspend state

    :param struct drm_i915_private \*dev_priv:
        i915 device private

.. _`intel_guc_allocate_vma`:

intel_guc_allocate_vma
======================

.. c:function:: struct i915_vma *intel_guc_allocate_vma(struct intel_guc *guc, u32 size)

    Allocate a GGTT VMA for GuC usage

    :param struct intel_guc \*guc:
        the guc

    :param u32 size:
        size of area to allocate (both virtual space and memory)

.. _`intel_guc_allocate_vma.description`:

Description
-----------

This is a wrapper to create an object for use with the GuC. In order to
use it inside the GuC, an object needs to be pinned lifetime, so we allocate
both some backing storage and a range inside the Global GTT. We must pin
it in the GGTT somewhere other than than [0, GUC_WOPCM_TOP) because that
range is reserved inside GuC.

.. _`intel_guc_allocate_vma.return`:

Return
------

A i915_vma if successful, otherwise an ERR_PTR.

.. This file was automatic generated / don't edit.

