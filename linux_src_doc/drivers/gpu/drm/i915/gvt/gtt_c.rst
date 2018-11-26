.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/gtt.c

.. _`is_2mb_gtt_possible`:

is_2MB_gtt_possible
===================

.. c:function:: int is_2MB_gtt_possible(struct intel_vgpu *vgpu, struct intel_gvt_gtt_entry *entry)

    :param vgpu:
        target vgpu
    :type vgpu: struct intel_vgpu \*

    :param entry:
        target pfn's gtt entry
    :type entry: struct intel_gvt_gtt_entry \*

.. _`is_2mb_gtt_possible.description`:

Description
-----------

Return 1 if 2MB huge gtt shadowing is possilbe, 0 if miscondition,
negtive if found err.

.. _`intel_vgpu_sync_oos_pages`:

intel_vgpu_sync_oos_pages
=========================

.. c:function:: int intel_vgpu_sync_oos_pages(struct intel_vgpu *vgpu)

    sync all the out-of-synced shadow for vGPU

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_sync_oos_pages.description`:

Description
-----------

This function is called before submitting a guest workload to host,
to sync all the out-of-synced shadow for vGPU

.. _`intel_vgpu_sync_oos_pages.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_flush_post_shadow`:

intel_vgpu_flush_post_shadow
============================

.. c:function:: int intel_vgpu_flush_post_shadow(struct intel_vgpu *vgpu)

    flush the post shadow transactions

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_flush_post_shadow.description`:

Description
-----------

This function is called before submitting a guest workload to host,
to flush all the post shadows for a vGPU.

.. _`intel_vgpu_flush_post_shadow.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_create_ppgtt_mm`:

intel_vgpu_create_ppgtt_mm
==========================

.. c:function:: struct intel_vgpu_mm *intel_vgpu_create_ppgtt_mm(struct intel_vgpu *vgpu, intel_gvt_gtt_type_t root_entry_type, u64 pdps)

    create a ppgtt mm object for a vGPU

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param root_entry_type:
        ppgtt root entry type
    :type root_entry_type: intel_gvt_gtt_type_t

    :param pdps:
        guest pdps.
    :type pdps: u64

.. _`intel_vgpu_create_ppgtt_mm.description`:

Description
-----------

This function is used to create a ppgtt mm object for a vGPU.

.. _`intel_vgpu_create_ppgtt_mm.return`:

Return
------

Zero on success, negative error code in pointer if failed.

.. _`_intel_vgpu_mm_release`:

\_intel_vgpu_mm_release
=======================

.. c:function:: void _intel_vgpu_mm_release(struct kref *mm_ref)

    destroy a mm object

    :param mm_ref:
        a kref object
    :type mm_ref: struct kref \*

.. _`_intel_vgpu_mm_release.description`:

Description
-----------

This function is used to destroy a mm object for vGPU

.. _`intel_vgpu_unpin_mm`:

intel_vgpu_unpin_mm
===================

.. c:function:: void intel_vgpu_unpin_mm(struct intel_vgpu_mm *mm)

    decrease the pin count of a vGPU mm object

    :param mm:
        a vGPU mm object
    :type mm: struct intel_vgpu_mm \*

.. _`intel_vgpu_unpin_mm.description`:

Description
-----------

This function is called when user doesn't want to use a vGPU mm object

.. _`intel_vgpu_pin_mm`:

intel_vgpu_pin_mm
=================

.. c:function:: int intel_vgpu_pin_mm(struct intel_vgpu_mm *mm)

    increase the pin count of a vGPU mm object

    :param mm:
        target vgpu mm
    :type mm: struct intel_vgpu_mm \*

.. _`intel_vgpu_pin_mm.description`:

Description
-----------

This function is called when user wants to use a vGPU mm object. If this
mm object hasn't been shadowed yet, the shadow will be populated at this
time.

.. _`intel_vgpu_pin_mm.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_gma_to_gpa`:

intel_vgpu_gma_to_gpa
=====================

.. c:function:: unsigned long intel_vgpu_gma_to_gpa(struct intel_vgpu_mm *mm, unsigned long gma)

    translate a gma to GPA

    :param mm:
        mm object. could be a PPGTT or GGTT mm object
    :type mm: struct intel_vgpu_mm \*

    :param gma:
        graphics memory address in this mm object
    :type gma: unsigned long

.. _`intel_vgpu_gma_to_gpa.description`:

Description
-----------

This function is used to translate a graphics memory address in specific
graphics memory space to guest physical address.

.. _`intel_vgpu_gma_to_gpa.return`:

Return
------

Guest physical address on success, INTEL_GVT_INVALID_ADDR if failed.

.. _`intel_vgpu_emulate_ggtt_mmio_read`:

intel_vgpu_emulate_ggtt_mmio_read
=================================

.. c:function:: int intel_vgpu_emulate_ggtt_mmio_read(struct intel_vgpu *vgpu, unsigned int off, void *p_data, unsigned int bytes)

    emulate GTT MMIO register read

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param off:
        register offset
    :type off: unsigned int

    :param p_data:
        data will be returned to guest
    :type p_data: void \*

    :param bytes:
        data length
    :type bytes: unsigned int

.. _`intel_vgpu_emulate_ggtt_mmio_read.description`:

Description
-----------

This function is used to emulate the GTT MMIO register read

.. _`intel_vgpu_emulate_ggtt_mmio_read.return`:

Return
------

Zero on success, error code if failed.

.. _`intel_vgpu_init_gtt`:

intel_vgpu_init_gtt
===================

.. c:function:: int intel_vgpu_init_gtt(struct intel_vgpu *vgpu)

    initialize per-vGPU graphics memory virulization

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_init_gtt.description`:

Description
-----------

This function is used to initialize per-vGPU graphics memory virtualization
components.

.. _`intel_vgpu_init_gtt.return`:

Return
------

Zero on success, error code if failed.

.. _`intel_vgpu_clean_gtt`:

intel_vgpu_clean_gtt
====================

.. c:function:: void intel_vgpu_clean_gtt(struct intel_vgpu *vgpu)

    clean up per-vGPU graphics memory virulization

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_clean_gtt.description`:

Description
-----------

This function is used to clean up per-vGPU graphics memory virtualization
components.

.. _`intel_vgpu_clean_gtt.return`:

Return
------

Zero on success, error code if failed.

.. _`intel_vgpu_find_ppgtt_mm`:

intel_vgpu_find_ppgtt_mm
========================

.. c:function:: struct intel_vgpu_mm *intel_vgpu_find_ppgtt_mm(struct intel_vgpu *vgpu, u64 pdps)

    find a PPGTT mm object

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param pdps:
        pdp root array
    :type pdps: u64

.. _`intel_vgpu_find_ppgtt_mm.description`:

Description
-----------

This function is used to find a PPGTT mm object from mm object pool

.. _`intel_vgpu_find_ppgtt_mm.return`:

Return
------

pointer to mm object on success, NULL if failed.

.. _`intel_vgpu_get_ppgtt_mm`:

intel_vgpu_get_ppgtt_mm
=======================

.. c:function:: struct intel_vgpu_mm *intel_vgpu_get_ppgtt_mm(struct intel_vgpu *vgpu, intel_gvt_gtt_type_t root_entry_type, u64 pdps)

    get or create a PPGTT mm object.

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param root_entry_type:
        ppgtt root entry type
    :type root_entry_type: intel_gvt_gtt_type_t

    :param pdps:
        guest pdps
    :type pdps: u64

.. _`intel_vgpu_get_ppgtt_mm.description`:

Description
-----------

This function is used to find or create a PPGTT mm object from a guest.

.. _`intel_vgpu_get_ppgtt_mm.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_put_ppgtt_mm`:

intel_vgpu_put_ppgtt_mm
=======================

.. c:function:: int intel_vgpu_put_ppgtt_mm(struct intel_vgpu *vgpu, u64 pdps)

    find and put a PPGTT mm object.

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param pdps:
        guest pdps
    :type pdps: u64

.. _`intel_vgpu_put_ppgtt_mm.description`:

Description
-----------

This function is used to find a PPGTT mm object from a guest and destroy it.

.. _`intel_vgpu_put_ppgtt_mm.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_init_gtt`:

intel_gvt_init_gtt
==================

.. c:function:: int intel_gvt_init_gtt(struct intel_gvt *gvt)

    initialize mm components of a GVT device

    :param gvt:
        GVT device
    :type gvt: struct intel_gvt \*

.. _`intel_gvt_init_gtt.description`:

Description
-----------

This function is called at the initialization stage, to initialize
the mm components of a GVT device.

.. _`intel_gvt_init_gtt.return`:

Return
------

zero on success, negative error code if failed.

.. _`intel_gvt_clean_gtt`:

intel_gvt_clean_gtt
===================

.. c:function:: void intel_gvt_clean_gtt(struct intel_gvt *gvt)

    clean up mm components of a GVT device

    :param gvt:
        GVT device
    :type gvt: struct intel_gvt \*

.. _`intel_gvt_clean_gtt.description`:

Description
-----------

This function is called at the driver unloading stage, to clean up the
the mm components of a GVT device.

.. _`intel_vgpu_invalidate_ppgtt`:

intel_vgpu_invalidate_ppgtt
===========================

.. c:function:: void intel_vgpu_invalidate_ppgtt(struct intel_vgpu *vgpu)

    invalidate PPGTT instances

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_invalidate_ppgtt.description`:

Description
-----------

This function is called when invalidate all PPGTT instances of a vGPU.

.. _`intel_vgpu_reset_ggtt`:

intel_vgpu_reset_ggtt
=====================

.. c:function:: void intel_vgpu_reset_ggtt(struct intel_vgpu *vgpu, bool invalidate_old)

    reset the GGTT entry

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param invalidate_old:
        invalidate old entries
    :type invalidate_old: bool

.. _`intel_vgpu_reset_ggtt.description`:

Description
-----------

This function is called at the vGPU create stage
to reset all the GGTT entries.

.. _`intel_vgpu_reset_gtt`:

intel_vgpu_reset_gtt
====================

.. c:function:: void intel_vgpu_reset_gtt(struct intel_vgpu *vgpu)

    reset the all GTT related status

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_reset_gtt.description`:

Description
-----------

This function is called from vfio core to reset reset all
GTT related status, including GGTT, PPGTT, scratch page.

.. This file was automatic generated / don't edit.

