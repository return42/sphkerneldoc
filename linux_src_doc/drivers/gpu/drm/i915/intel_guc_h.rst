.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/intel_guc.h

.. _`intel_guc_ggtt_offset`:

intel_guc_ggtt_offset
=====================

.. c:function:: u32 intel_guc_ggtt_offset(struct intel_guc *guc, struct i915_vma *vma)

    Get and validate the GGTT offset of \ ``vma``\ 

    :param guc:
        intel_guc structure.
    :type guc: struct intel_guc \*

    :param vma:
        i915 graphics virtual memory area.
    :type vma: struct i915_vma \*

.. _`intel_guc_ggtt_offset.description`:

Description
-----------

GuC does not allow any gfx GGTT address that falls into range
[0, ggtt.pin_bias), which is reserved for Boot ROM, SRAM and WOPCM.
Currently, in order to exclude [0, ggtt.pin_bias) address space from
GGTT, all gfx objects used by GuC are allocated with \ :c:func:`intel_guc_allocate_vma`\ 
and pinned with PIN_OFFSET_BIAS along with the value of ggtt.pin_bias.

.. _`intel_guc_ggtt_offset.return`:

Return
------

GGTT offset of the \ ``vma``\ .

.. This file was automatic generated / don't edit.

