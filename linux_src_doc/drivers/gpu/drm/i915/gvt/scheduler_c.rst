.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/scheduler.c

.. _`intel_gvt_scan_and_shadow_workload`:

intel_gvt_scan_and_shadow_workload
==================================

.. c:function:: int intel_gvt_scan_and_shadow_workload(struct intel_vgpu_workload *workload)

    audit the workload by scanning and shadow it as well, include ringbuffer,wa_ctx and ctx.

    :param workload:
        an abstract entity for each execlist submission.
    :type workload: struct intel_vgpu_workload \*

.. _`intel_gvt_scan_and_shadow_workload.description`:

Description
-----------

This function is called before the workload submitting to i915, to make
sure the content of the workload is valid.

.. _`intel_vgpu_clean_submission`:

intel_vgpu_clean_submission
===========================

.. c:function:: void intel_vgpu_clean_submission(struct intel_vgpu *vgpu)

    free submission-related resource for vGPU

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_clean_submission.description`:

Description
-----------

This function is called when a vGPU is being destroyed.

.. _`intel_vgpu_reset_submission`:

intel_vgpu_reset_submission
===========================

.. c:function:: void intel_vgpu_reset_submission(struct intel_vgpu *vgpu, unsigned long engine_mask)

    reset submission-related resource for vGPU

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param engine_mask:
        engines expected to be reset
    :type engine_mask: unsigned long

.. _`intel_vgpu_reset_submission.description`:

Description
-----------

This function is called when a vGPU is being destroyed.

.. _`intel_vgpu_setup_submission`:

intel_vgpu_setup_submission
===========================

.. c:function:: int intel_vgpu_setup_submission(struct intel_vgpu *vgpu)

    setup submission-related resource for vGPU

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

.. _`intel_vgpu_setup_submission.description`:

Description
-----------

This function is called when a vGPU is being created.

.. _`intel_vgpu_setup_submission.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_select_submission_ops`:

intel_vgpu_select_submission_ops
================================

.. c:function:: int intel_vgpu_select_submission_ops(struct intel_vgpu *vgpu, unsigned long engine_mask, unsigned int interface)

    select virtual submission interface

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param engine_mask:
        either ALL_ENGINES or target engine mask
    :type engine_mask: unsigned long

    :param interface:
        expected vGPU virtual submission interface
    :type interface: unsigned int

.. _`intel_vgpu_select_submission_ops.description`:

Description
-----------

This function is called when guest configures submission interface.

.. _`intel_vgpu_select_submission_ops.return`:

Return
------

Zero on success, negative error code if failed.

.. _`intel_vgpu_destroy_workload`:

intel_vgpu_destroy_workload
===========================

.. c:function:: void intel_vgpu_destroy_workload(struct intel_vgpu_workload *workload)

    destroy a vGPU workload

    :param workload:
        workload to destroy
    :type workload: struct intel_vgpu_workload \*

.. _`intel_vgpu_destroy_workload.description`:

Description
-----------

This function is called when destroy a vGPU workload.

.. _`intel_vgpu_create_workload`:

intel_vgpu_create_workload
==========================

.. c:function:: struct intel_vgpu_workload *intel_vgpu_create_workload(struct intel_vgpu *vgpu, int ring_id, struct execlist_ctx_descriptor_format *desc)

    create a vGPU workload

    :param vgpu:
        a vGPU
    :type vgpu: struct intel_vgpu \*

    :param ring_id:
        ring index
    :type ring_id: int

    :param desc:
        a guest context descriptor
    :type desc: struct execlist_ctx_descriptor_format \*

.. _`intel_vgpu_create_workload.description`:

Description
-----------

This function is called when creating a vGPU workload.

.. _`intel_vgpu_create_workload.return`:

Return
------

struct intel_vgpu_workload \* on success, negative error code in
pointer if failed.

.. _`intel_vgpu_queue_workload`:

intel_vgpu_queue_workload
=========================

.. c:function:: void intel_vgpu_queue_workload(struct intel_vgpu_workload *workload)

    Qeue a vGPU workload

    :param workload:
        the workload to queue in
    :type workload: struct intel_vgpu_workload \*

.. This file was automatic generated / don't edit.

