.. -*- coding: utf-8; mode: rst -*-
.. src-file: drivers/gpu/drm/i915/gvt/scheduler.c

.. _`intel_gvt_scan_and_shadow_workload`:

intel_gvt_scan_and_shadow_workload
==================================

.. c:function:: int intel_gvt_scan_and_shadow_workload(struct intel_vgpu_workload *workload)

    audit the workload by scanning and shadow it as well, include ringbuffer,wa_ctx and ctx.

    :param struct intel_vgpu_workload \*workload:
        an abstract entity for each execlist submission.

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

    :param struct intel_vgpu \*vgpu:
        a vGPU

.. _`intel_vgpu_clean_submission.description`:

Description
-----------

This function is called when a vGPU is being destroyed.

.. _`intel_vgpu_reset_submission`:

intel_vgpu_reset_submission
===========================

.. c:function:: void intel_vgpu_reset_submission(struct intel_vgpu *vgpu, unsigned long engine_mask)

    reset submission-related resource for vGPU

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned long engine_mask:
        engines expected to be reset

.. _`intel_vgpu_reset_submission.description`:

Description
-----------

This function is called when a vGPU is being destroyed.

.. _`intel_vgpu_setup_submission`:

intel_vgpu_setup_submission
===========================

.. c:function:: int intel_vgpu_setup_submission(struct intel_vgpu *vgpu)

    setup submission-related resource for vGPU

    :param struct intel_vgpu \*vgpu:
        a vGPU

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

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param unsigned long engine_mask:
        *undescribed*

    :param unsigned int interface:
        expected vGPU virtual submission interface

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

    :param struct intel_vgpu_workload \*workload:
        *undescribed*

.. _`intel_vgpu_destroy_workload.description`:

Description
-----------

This function is called when destroy a vGPU workload.

.. _`intel_vgpu_create_workload`:

intel_vgpu_create_workload
==========================

.. c:function:: struct intel_vgpu_workload *intel_vgpu_create_workload(struct intel_vgpu *vgpu, int ring_id, struct execlist_ctx_descriptor_format *desc)

    create a vGPU workload

    :param struct intel_vgpu \*vgpu:
        a vGPU

    :param int ring_id:
        *undescribed*

    :param struct execlist_ctx_descriptor_format \*desc:
        a guest context descriptor

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

    :param struct intel_vgpu_workload \*workload:
        the workload to queue in

.. This file was automatic generated / don't edit.

