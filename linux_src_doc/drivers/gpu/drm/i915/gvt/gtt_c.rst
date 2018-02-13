.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/gtt.c

.. _`intel_vgpu_init_page_track`:

intel_vgpu_init_page_track
==========================

.. c:function:: int intel_vgpu_init_page_track(struct intel_vgpu *vgpu, struct intel_vgpu_page_track *t, unsigned long gfn, int (*handler)(void *, u64, void *, int), void *data)

    init a page track data structure

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param struct intel_vgpu_page_track \*t:
        a page track data structure

    :param unsigned long gfn:
        guest memory page frame number

    :param int (\*handler)(void \*, u64, void \*, int):
        the function will be called when target guest memory page has
        been modified.

    :param void \*data:
        *undescribed*

.. _`intel_vgpu_init_page_track.description`:

Description
-----------

This function is called when a user wants to prepare a page track data
structure to track a guest memory page.

.. _`intel_vgpu_init_page_track.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_clean_page_track`:

intel_vgpu_clean_page_track
===========================

.. c:function:: void intel_vgpu_clean_page_track(struct intel_vgpu *vgpu, struct intel_vgpu_page_track *t)

    release a page track data structure

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param struct intel_vgpu_page_track \*t:
        a page track data structure

.. _`intel_vgpu_clean_page_track.description`:

Description
-----------

This function is called before a user frees a page track data structure.

.. _`intel_vgpu_find_tracked_page`:

intel_vgpu_find_tracked_page
============================

.. c:function:: struct intel_vgpu_page_track *intel_vgpu_find_tracked_page(struct intel_vgpu *vgpu, unsigned long gfn)

    find a tracked guest page

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned long gfn:
        guest memory page frame number

.. _`intel_vgpu_find_tracked_page.description`:

Description
-----------

This function is called when the emulation layer wants to figure out if a
trapped GFN is a tracked guest page.

.. _`intel_vgpu_find_tracked_page.return`:

Return
------

Pointer to page track data structure, NULL if not found.

.. _`intel_vgpu_sync_oos_pages`:

intel_vgpu_sync_oos_pages
=========================

.. c:function:: int intel_vgpu_sync_oos_pages(struct intel_vgpu *vgpu)

    sync all the out-of-synced shadow for vGPU

    :param struct intel_vgpu \*vgpu:
        a vGPU

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

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. _`intel_vgpu_flush_post_shadow.description`:

Description
-----------

This function is called before submitting a guest workload to host,
to flush all the post shadows for a vGPU.

.. _`intel_vgpu_flush_post_shadow.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_destroy_mm`:

intel_vgpu_destroy_mm
=====================

.. c:function:: void intel_vgpu_destroy_mm(struct kref *mm_ref)

    destroy a mm object

    :param struct kref \*mm_ref:
        *undescribed*

.. _`intel_vgpu_destroy_mm.description`:

Description
-----------

This function is used to destroy a mm object for vGPU

.. _`intel_vgpu_create_mm`:

intel_vgpu_create_mm
====================

.. c:function:: struct intel_vgpu_mm *intel_vgpu_create_mm(struct intel_vgpu *vgpu, int mm_type, void *virtual_page_table, int page_table_level, u32 pde_base_index)

    create a mm object for a vGPU

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param int mm_type:
        mm object type, should be PPGTT or GGTT

    :param void \*virtual_page_table:
        page table root pointers. Could be NULL if user wants
        to populate shadow later.

    :param int page_table_level:
        describe the page table level of the mm object

    :param u32 pde_base_index:
        pde root pointer base in GGTT MMIO.

.. _`intel_vgpu_create_mm.description`:

Description
-----------

This function is used to create a mm object for a vGPU.

.. _`intel_vgpu_create_mm.return`:

Return
------

Zero on success, negative error code in pointer if failed.

.. _`intel_vgpu_unpin_mm`:

intel_vgpu_unpin_mm
===================

.. c:function:: void intel_vgpu_unpin_mm(struct intel_vgpu_mm *mm)

    decrease the pin count of a vGPU mm object

    :param struct intel_vgpu_mm \*mm:
        a vGPU mm object

.. _`intel_vgpu_unpin_mm.description`:

Description
-----------

This function is called when user doesn't want to use a vGPU mm object

.. _`intel_vgpu_pin_mm`:

intel_vgpu_pin_mm
=================

.. c:function:: int intel_vgpu_pin_mm(struct intel_vgpu_mm *mm)

    increase the pin count of a vGPU mm object

    :param struct intel_vgpu_mm \*mm:
        *undescribed*

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

    :param struct intel_vgpu_mm \*mm:
        mm object. could be a PPGTT or GGTT mm object

    :param unsigned long gma:
        graphics memory address in this mm object

.. _`intel_vgpu_gma_to_gpa.description`:

Description
-----------

This function is used to translate a graphics memory address in specific
graphics memory space to guest physical address.

.. _`intel_vgpu_gma_to_gpa.return`:

Return
------

Guest physical address on success, INTEL_GVT_INVALID_ADDR if failed.

.. _`intel_vgpu_emulate_gtt_mmio_read`:

intel_vgpu_emulate_gtt_mmio_read
================================

.. c:function:: int intel_vgpu_emulate_gtt_mmio_read(struct intel_vgpu *vgpu, unsigned int off, void *p_data, unsigned int bytes)

    emulate GTT MMIO register read

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned int off:
        register offset

    :param void \*p_data:
        data will be returned to guest

    :param unsigned int bytes:
        data length

.. _`intel_vgpu_emulate_gtt_mmio_read.description`:

Description
-----------

This function is used to emulate the GTT MMIO register read

.. _`intel_vgpu_emulate_gtt_mmio_read.return`:

Return
------

Zero on success, error code if failed.

.. _`intel_vgpu_init_gtt`:

intel_vgpu_init_gtt
===================

.. c:function:: int intel_vgpu_init_gtt(struct intel_vgpu *vgpu)

    initialize per-vGPU graphics memory virulization

    :param struct intel_vgpu \*vgpu:
        a vGPU

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

    :param struct intel_vgpu \*vgpu:
        a vGPU

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

.. c:function:: struct intel_vgpu_mm *intel_vgpu_find_ppgtt_mm(struct intel_vgpu *vgpu, int page_table_level, void *root_entry)

    find a PPGTT mm object

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param int page_table_level:
        PPGTT page table level

    :param void \*root_entry:
        PPGTT page table root pointers

.. _`intel_vgpu_find_ppgtt_mm.description`:

Description
-----------

This function is used to find a PPGTT mm object from mm object pool

.. _`intel_vgpu_find_ppgtt_mm.return`:

Return
------

pointer to mm object on success, NULL if failed.

.. _`intel_vgpu_g2v_create_ppgtt_mm`:

intel_vgpu_g2v_create_ppgtt_mm
==============================

.. c:function:: int intel_vgpu_g2v_create_ppgtt_mm(struct intel_vgpu *vgpu, int page_table_level)

    create a PPGTT mm object from g2v notification

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param int page_table_level:
        PPGTT page table level

.. _`intel_vgpu_g2v_create_ppgtt_mm.description`:

Description
-----------

This function is used to create a PPGTT mm object from a guest to GVT-g
notification.

.. _`intel_vgpu_g2v_create_ppgtt_mm.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_g2v_destroy_ppgtt_mm`:

intel_vgpu_g2v_destroy_ppgtt_mm
===============================

.. c:function:: int intel_vgpu_g2v_destroy_ppgtt_mm(struct intel_vgpu *vgpu, int page_table_level)

    destroy a PPGTT mm object from g2v notification

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param int page_table_level:
        PPGTT page table level

.. _`intel_vgpu_g2v_destroy_ppgtt_mm.description`:

Description
-----------

This function is used to create a PPGTT mm object from a guest to GVT-g
notification.

.. _`intel_vgpu_g2v_destroy_ppgtt_mm.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_gvt_init_gtt`:

intel_gvt_init_gtt
==================

.. c:function:: int intel_gvt_init_gtt(struct intel_gvt *gvt)

    initialize mm components of a GVT device

    :param struct intel_gvt \*gvt:
        GVT device

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

    :param struct intel_gvt \*gvt:
        GVT device

.. _`intel_gvt_clean_gtt.description`:

Description
-----------

This function is called at the driver unloading stage, to clean up the
the mm components of a GVT device.

.. _`intel_vgpu_reset_ggtt`:

intel_vgpu_reset_ggtt
=====================

.. c:function:: void intel_vgpu_reset_ggtt(struct intel_vgpu *vgpu)

    reset the GGTT entry

    :param struct intel_vgpu \*vgpu:
        a vGPU

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

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. _`intel_vgpu_reset_gtt.description`:

Description
-----------

This function is called from vfio core to reset reset all
GTT related status, including GGTT, PPGTT, scratch page.

.. This file was automatic generated / don't edit.

